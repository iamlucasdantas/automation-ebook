"""GoHighLevel CLI — Agent-usable command-line interface to the GHL API."""
from __future__ import annotations

import json
import sys

import click
import requests

from cli_anything.gohighlevel.utils import ghl_client as api

__version__ = "2.1.0"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_json(ctx: click.Context) -> bool:
    return bool((ctx.obj or {}).get("json", False))


def _output(ctx: click.Context, data, label: str = ""):
    """Print data respecting --json flag."""
    if _is_json(ctx):
        click.echo(json.dumps(data, indent=2, default=str, ensure_ascii=False))
    else:
        if label:
            click.echo(f"\n{label}")
            click.echo("-" * len(label))
        click.echo(api.format_output(data))


def _handle_error(e: Exception):
    """Handle API errors with clear messages."""
    if isinstance(e, requests.exceptions.HTTPError) and e.response is not None:
        resp = e.response
        try:
            body = resp.json()
            msg = body.get("message") or body.get("msg") or body.get("error") or json.dumps(body, ensure_ascii=False)
            if isinstance(msg, list):
                msg = "; ".join(str(m) for m in msg)
        except Exception:  # noqa: BLE001
            msg = resp.text[:500]
        hint = ""
        if resp.status_code == 401:
            hint = "\n  Verifique GHL_API_KEY (token expirado ou inválido)."
        elif resp.status_code == 403:
            hint = "\n  O Private Integration Token não tem o escopo necessário para este endpoint."
        elif resp.status_code == 422:
            hint = "\n  Payload rejeitado — confira os campos obrigatórios deste endpoint."
        elif resp.status_code == 429:
            hint = "\n  Rate limit do GHL (100 req/10s). Reduza a concorrência."
        click.echo(f"Erro da API ({resp.status_code}): {msg}{hint}", err=True)
    else:
        click.echo(f"Erro: {e}", err=True)
    sys.exit(1)


def _loc(ctx: click.Context) -> str:
    """Get location ID from context or env."""
    return (ctx.obj or {}).get("location_id") or api._get_location_id()


def _to_epoch_ms(value: str) -> int:
    """Aceita epoch ms, YYYY-MM-DD ou ISO 8601 e devolve epoch em ms.

    O endpoint de free-slots do GHL só aceita epoch em milissegundos.
    """
    from datetime import datetime, timezone

    value = str(value).strip()
    if value.isdigit():
        num = int(value)
        return num * 1000 if num < 10_000_000_000 else num  # segundos -> ms
    text = value.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        raise click.BadParameter(
            f"Data inválida: {value}. Use YYYY-MM-DD, ISO 8601 ou epoch em ms."
        )
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


# ---------------------------------------------------------------------------
# Main CLI Group
# ---------------------------------------------------------------------------

@click.group(invoke_without_command=True)
@click.option("--json", "use_json", is_flag=True, help="Output as JSON")
@click.option("--location-id", envvar="GHL_LOCATION_ID", default=None, help="GHL Location/Sub-account ID")
@click.option("--experimental", is_flag=True, help="Enable experimental commands (internal GHL API)")
@click.version_option(__version__, prog_name="cli-anything-gohighlevel")
@click.pass_context
def cli(ctx, use_json, location_id, experimental):
    """GoHighLevel CLI — manage contacts, workflows, calendars, and more."""
    api.load_env()
    ctx.ensure_object(dict)
    ctx.obj["json"] = use_json
    ctx.obj["location_id"] = location_id
    ctx.obj["experimental"] = experimental
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)


# ---------------------------------------------------------------------------
# REPL Command
# ---------------------------------------------------------------------------

@cli.command(hidden=True)
@click.pass_context
def repl(ctx):
    """Interactive REPL mode."""
    try:
        from cli_anything.gohighlevel.utils.repl_skin import ReplSkin
        skin = ReplSkin("gohighlevel", version=__version__)
        skin.print_banner()
        pt_session = skin.create_prompt_session()

        commands = {
            "contacts": "Manage contacts (list, get, create, update, delete, search, tags)",
            "opportunities": "Manage pipeline opportunities (list, get, create, update, delete)",
            "calendars": "Manage calendars and appointments (list, slots, book)",
            "workflows": "List and manage workflows",
            "conversations": "Manage conversations and messages",
            "emails": "Email campaigns (list, get, send)",
            "payments": "Transactions, invoices, orders",
            "forms": "Forms and submissions",
            "social": "Social media posts and analytics",
            "locations": "Location/sub-account management (tags, custom fields/values)",
            "documents": "Contracts, proposals and templates",
            "users": "Sub-account users",
            "doctor": "Validate credentials, connectivity and scopes",
            "help": "Show this help",
            "exit": "Exit REPL",
        }

        while True:
            try:
                line = skin.get_input(pt_session, project_name="ghl")
                if not line or not line.strip():
                    continue
                parts = line.strip().split()
                cmd = parts[0].lower()

                if cmd in ("exit", "quit", "q"):
                    skin.print_goodbye()
                    break
                elif cmd == "help":
                    skin.help(commands)
                else:
                    # Pass through to Click CLI
                    try:
                        cli.main(parts, standalone_mode=False, obj=ctx.obj)
                    except SystemExit:
                        pass
                    except click.exceptions.UsageError as e:
                        skin.error(str(e))
            except (EOFError, KeyboardInterrupt):
                skin.print_goodbye()
                break
    except ImportError:
        click.echo("REPL requires prompt-toolkit. Install with: pip install prompt-toolkit")
        click.echo("Use subcommands directly instead: ghl contacts list")


# ===========================================================================
# CONTACTS
# ===========================================================================

@cli.group()
@click.pass_context
def contacts(ctx):
    """Manage contacts — list, get, create, update, delete, search, tags."""
    pass


@contacts.command("list")
@click.option("--limit", default=20, help="Number of contacts to return")
@click.option("--start-after-id", default=None,
              help="Contact ID cursor for pagination (GHL não usa offset numérico)")
@click.option("--query", default=None, help="Search query string (nome, email ou telefone)")
@click.option("--all", "fetch_all", is_flag=True, help="Paginar até --max-records")
@click.option("--max-records", default=1000, help="Teto de registros com --all")
@click.pass_context
def contacts_list(ctx, limit, start_after_id, query, fetch_all, max_records):
    """List contacts in the location."""
    try:
        if fetch_all:
            records = api.search_contacts_all(_loc(ctx), max_records=max_records)
            _output(ctx, records, f"Contatos ({len(records)})")
            return
        params = {"locationId": _loc(ctx), "limit": limit}
        if start_after_id:
            params["startAfterId"] = start_after_id
        if query:
            params["query"] = query
        data = api.get("/contacts/", params=params)
        _output(ctx, data.get("contacts", data) if _is_json(ctx) else data, "Contacts")
    except Exception as e:
        _handle_error(e)


@contacts.command("get")
@click.argument("contact_id")
@click.pass_context
def contacts_get(ctx, contact_id):
    """Get a single contact by ID."""
    try:
        data = api.get(f"/contacts/{contact_id}")
        _output(ctx, data, "Contact Details")
    except Exception as e:
        _handle_error(e)


@contacts.command("create")
@click.option("--email", default=None, help="Contact email")
@click.option("--phone", default=None, help="Contact phone")
@click.option("--first-name", default=None, help="First name")
@click.option("--last-name", default=None, help="Last name")
@click.option("--name", default=None, help="Full name")
@click.option("--company", "company_name", default=None, help="Company name")
@click.option("--tag", "tags", multiple=True, help="Tags to add (repeatable)")
@click.option("--source", default=None, help="Contact source")
@click.pass_context
def contacts_create(ctx, email, phone, first_name, last_name, name, company_name, tags, source):
    """Create a new contact."""
    try:
        body = {"locationId": _loc(ctx)}
        if email:
            body["email"] = email
        if phone:
            body["phone"] = phone
        if first_name:
            body["firstName"] = first_name
        if last_name:
            body["lastName"] = last_name
        if name:
            body["name"] = name
        if company_name:
            body["companyName"] = company_name
        if tags:
            body["tags"] = list(tags)
        if source:
            body["source"] = source
        data = api.post("/contacts/", data=body)
        _output(ctx, data, "Contact Created")
    except Exception as e:
        _handle_error(e)


@contacts.command("update")
@click.argument("contact_id")
@click.option("--email", default=None)
@click.option("--phone", default=None)
@click.option("--first-name", default=None)
@click.option("--last-name", default=None)
@click.option("--company", "company_name", default=None)
@click.option("--tag", "tags", multiple=True, help="Replace all tags")
@click.pass_context
def contacts_update(ctx, contact_id, email, phone, first_name, last_name, company_name, tags):
    """Update a contact by ID."""
    try:
        body = {}
        if email:
            body["email"] = email
        if phone:
            body["phone"] = phone
        if first_name:
            body["firstName"] = first_name
        if last_name:
            body["lastName"] = last_name
        if company_name:
            body["companyName"] = company_name
        if tags:
            body["tags"] = list(tags)
        data = api.put(f"/contacts/{contact_id}", data=body)
        _output(ctx, data, "Contact Updated")
    except Exception as e:
        _handle_error(e)


@contacts.command("delete")
@click.argument("contact_id")
@click.pass_context
def contacts_delete(ctx, contact_id):
    """Delete a contact by ID."""
    try:
        data = api.delete(f"/contacts/{contact_id}")
        _output(ctx, data, "Contact Deleted")
    except Exception as e:
        _handle_error(e)


@contacts.command("search")
@click.argument("query")
@click.option("--limit", default=20)
@click.option("--field", default=None,
              help="Restringir a um campo (ex.: email, phone, firstNameLowerCase)")
@click.pass_context
def contacts_search(ctx, query, limit, field):
    """Busca contatos por nome, email ou telefone.

    Sem --field, usa a busca ampla do GHL (varre nome, email e telefone).
    """
    try:
        if field:
            body = {
                "locationId": _loc(ctx),
                "pageLimit": limit,
                "filters": [{"field": field, "operator": "contains", "value": query.lower()}],
            }
            data = api.post("/contacts/search", data=body)
        else:
            data = api.get("/contacts/", params={
                "locationId": _loc(ctx), "limit": limit, "query": query,
            })
        _output(ctx, data, f"Busca: '{query}'")
    except Exception as e:
        _handle_error(e)


@contacts.command("add-tag")
@click.argument("contact_id")
@click.argument("tags", nargs=-1, required=True)
@click.pass_context
def contacts_add_tag(ctx, contact_id, tags):
    """Add tags to a contact."""
    try:
        data = api.post(f"/contacts/{contact_id}/tags", data={"tags": list(tags)})
        _output(ctx, data, "Tags Added")
    except Exception as e:
        _handle_error(e)


@contacts.command("remove-tag")
@click.argument("contact_id")
@click.argument("tags", nargs=-1, required=True)
@click.pass_context
def contacts_remove_tag(ctx, contact_id, tags):
    """Remove tags from a contact."""
    try:
        data = api.delete(f"/contacts/{contact_id}/tags", data={"tags": list(tags)})
        _output(ctx, data, "Tags Removed")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# OPPORTUNITIES
# ===========================================================================

@cli.group()
@click.pass_context
def opportunities(ctx):
    """Manage pipeline opportunities — list, get, create, update, delete."""
    pass


@opportunities.command("list")
@click.option("--pipeline-id", default=None, help="Filter by pipeline ID")
@click.option("--stage-id", default=None, help="Filter by pipeline stage ID")
@click.option("--contact-id", default=None, help="Filter by contact ID")
@click.option("--assigned-to", default=None, help="Filter by assigned user ID")
@click.option("--query", "q", default=None, help="Busca textual")
@click.option("--limit", default=20)
@click.option("--page", default=1)
@click.option("--status", default=None, type=click.Choice(["open", "won", "lost", "abandoned", "all"]))
@click.pass_context
def opportunities_list(ctx, pipeline_id, stage_id, contact_id, assigned_to, q, limit, page, status):
    """List opportunities."""
    try:
        # /opportunities/search usa location_id em snake_case (quirk do GHL).
        params = {"location_id": _loc(ctx), "limit": limit, "page": page}
        if pipeline_id:
            params["pipelineId"] = pipeline_id
        if stage_id:
            params["pipelineStageId"] = stage_id
        if contact_id:
            params["contactId"] = contact_id
        if assigned_to:
            params["assignedTo"] = assigned_to
        if q:
            params["q"] = q
        if status:
            params["status"] = status
        data = api.get("/opportunities/search", params=params)
        _output(ctx, data, "Opportunities")
    except Exception as e:
        _handle_error(e)


@opportunities.command("get")
@click.argument("opportunity_id")
@click.pass_context
def opportunities_get(ctx, opportunity_id):
    """Get opportunity details."""
    try:
        data = api.get(f"/opportunities/{opportunity_id}")
        _output(ctx, data, "Opportunity Details")
    except Exception as e:
        _handle_error(e)


@opportunities.command("create")
@click.option("--pipeline-id", required=True, help="Pipeline ID")
@click.option("--stage-id", required=True, help="Stage ID")
@click.option("--name", required=True, help="Opportunity name")
@click.option("--contact-id", required=True, help="Contact ID")
@click.option("--value", "monetary_value", default=None, type=float, help="Monetary value")
@click.option("--status", default="open", type=click.Choice(["open", "won", "lost", "abandoned"]))
@click.pass_context
def opportunities_create(ctx, pipeline_id, stage_id, name, contact_id, monetary_value, status):
    """Create a new opportunity."""
    try:
        body = {
            "locationId": _loc(ctx),
            "pipelineId": pipeline_id,
            "pipelineStageId": stage_id,
            "name": name,
            "contactId": contact_id,
            "status": status,
        }
        if monetary_value is not None:
            body["monetaryValue"] = monetary_value
        data = api.post("/opportunities/", data=body)
        _output(ctx, data, "Opportunity Created")
    except Exception as e:
        _handle_error(e)


@opportunities.command("update")
@click.argument("opportunity_id")
@click.option("--name", default=None)
@click.option("--stage-id", default=None, help="Move to stage")
@click.option("--status", default=None, type=click.Choice(["open", "won", "lost", "abandoned"]))
@click.option("--value", "monetary_value", default=None, type=float)
@click.pass_context
def opportunities_update(ctx, opportunity_id, name, stage_id, status, monetary_value):
    """Update an opportunity."""
    try:
        body = {}
        if name:
            body["name"] = name
        if stage_id:
            body["pipelineStageId"] = stage_id
        if status:
            body["status"] = status
        if monetary_value is not None:
            body["monetaryValue"] = monetary_value
        data = api.put(f"/opportunities/{opportunity_id}", data=body)
        _output(ctx, data, "Opportunity Updated")
    except Exception as e:
        _handle_error(e)


@opportunities.command("delete")
@click.argument("opportunity_id")
@click.pass_context
def opportunities_delete(ctx, opportunity_id):
    """Delete an opportunity."""
    try:
        data = api.delete(f"/opportunities/{opportunity_id}")
        _output(ctx, data, "Opportunity Deleted")
    except Exception as e:
        _handle_error(e)


@opportunities.command("pipelines")
@click.pass_context
def opportunities_pipelines(ctx):
    """List all pipelines."""
    try:
        data = api.get("/opportunities/pipelines", params={"locationId": _loc(ctx)})
        _output(ctx, data, "Pipelines")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# CALENDARS
# ===========================================================================

@cli.group()
@click.pass_context
def calendars(ctx):
    """Manage calendars, appointments, and availability slots."""
    pass


@calendars.command("list")
@click.pass_context
def calendars_list(ctx):
    """List all calendars."""
    try:
        data = api.get("/calendars/", params={"locationId": _loc(ctx)})
        _output(ctx, data, "Calendars")
    except Exception as e:
        _handle_error(e)


@calendars.command("get")
@click.argument("calendar_id")
@click.pass_context
def calendars_get(ctx, calendar_id):
    """Get calendar details."""
    try:
        data = api.get(f"/calendars/{calendar_id}")
        _output(ctx, data, "Calendar Details")
    except Exception as e:
        _handle_error(e)


@calendars.command("slots")
@click.argument("calendar_id")
@click.option("--start", required=True, help="Start date (YYYY-MM-DD or epoch ms)")
@click.option("--end", required=True, help="End date (YYYY-MM-DD or epoch ms)")
@click.option("--timezone", default=None,
              help="IANA timezone (default: GHL_TIMEZONE ou America/Sao_Paulo)")
@click.pass_context
def calendars_slots(ctx, calendar_id, start, end, timezone):
    """Get available appointment slots."""
    try:
        import os
        params = {
            # o endpoint exige epoch em milissegundos
            "startDate": _to_epoch_ms(start),
            "endDate": _to_epoch_ms(end),
            "timezone": timezone or os.environ.get("GHL_TIMEZONE", "America/Sao_Paulo"),
        }
        data = api.get(f"/calendars/{calendar_id}/free-slots", params=params)
        _output(ctx, data, "Available Slots")
    except Exception as e:
        _handle_error(e)


@calendars.command("appointments")
@click.option("--calendar-id", default=None, help="Filter by calendar ID")
@click.option("--contact-id", default=None, help="Filter by contact ID")
@click.option("--start", default=None, help="Start date filter")
@click.option("--end", default=None, help="End date filter")
@click.pass_context
def calendars_appointments(ctx, calendar_id, contact_id, start, end):
    """List appointments."""
    try:
        params = {"locationId": _loc(ctx)}
        if calendar_id:
            params["calendarId"] = calendar_id
        if contact_id:
            params["contactId"] = contact_id
        if start:
            params["startTime"] = start
        if end:
            params["endTime"] = end
        data = api.get("/calendars/events/appointments", params=params)
        _output(ctx, data, "Appointments")
    except Exception as e:
        _handle_error(e)


@calendars.command("book")
@click.option("--calendar-id", required=True, help="Calendar ID")
@click.option("--contact-id", required=True, help="Contact ID")
@click.option("--start", required=True, help="Start time (ISO 8601)")
@click.option("--end", default=None, help="End time (ISO 8601). Omitido = duração do calendário")
@click.option("--title", default=None, help="Appointment title")
@click.option("--assigned-user-id", default=None, help="Usuário responsável")
@click.option("--status", "appointment_status", default="confirmed",
              type=click.Choice(["new", "confirmed", "showed", "noshow", "cancelled"]))
@click.option("--ignore-free-slots", is_flag=True,
              help="Agendar mesmo fora da disponibilidade configurada")
@click.pass_context
def calendars_book(ctx, calendar_id, contact_id, start, end, title,
                   assigned_user_id, appointment_status, ignore_free_slots):
    """Book an appointment."""
    try:
        body = {
            "calendarId": calendar_id,
            "locationId": _loc(ctx),
            "contactId": contact_id,
            "startTime": start,
            "appointmentStatus": appointment_status,
        }
        if end:
            body["endTime"] = end
        if assigned_user_id:
            body["assignedUserId"] = assigned_user_id
        if ignore_free_slots:
            body["ignoreFreeSlotValidation"] = True
        if title:
            body["title"] = title
        data = api.post("/calendars/events/appointments", data=body)
        _output(ctx, data, "Appointment Booked")
    except Exception as e:
        _handle_error(e)


@calendars.command("groups")
@click.pass_context
def calendars_groups(ctx):
    """List calendar groups."""
    try:
        data = api.get("/calendars/groups", params={"locationId": _loc(ctx)})
        _output(ctx, data, "Calendar Groups")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# WORKFLOWS
# ===========================================================================

def _require_experimental(ctx: click.Context):
    """Guard: exit if --experimental flag not set."""
    if not ctx.obj.get("experimental"):
        click.echo(
            "Error: This command requires --experimental flag (uses internal GHL API).\n"
            "Usage: ghl --experimental workflows create ...",
            err=True,
        )
        sys.exit(1)


def _get_internal_client(ctx: click.Context):
    """Get an InternalGHLClient (lazy import to avoid dep when not needed)."""
    from cli_anything.gohighlevel.utils.ghl_internal_client import TokenManager, InternalGHLClient
    token_mgr = TokenManager()
    return InternalGHLClient(token_mgr, _loc(ctx))


@cli.group()
@click.pass_context
def workflows(ctx):
    """List and manage workflows. Create commands require --experimental."""
    pass


@workflows.command("list")
@click.pass_context
def workflows_list(ctx):
    """List all workflows."""
    try:
        data = api.get("/workflows/", params={"locationId": _loc(ctx)})
        _output(ctx, data, "Workflows")
    except Exception as e:
        _handle_error(e)


@workflows.command("enroll")
@click.option("--contact-id", required=True, help="Contact ID to enroll")
@click.option("--workflow-id", required=True, help="Workflow ID")
@click.pass_context
def workflows_enroll(ctx, contact_id, workflow_id):
    """Enroll a contact in a workflow (public API)."""
    try:
        data = api.post(f"/contacts/{contact_id}/workflow/{workflow_id}")
        _output(ctx, data, "Contact Enrolled")
    except Exception as e:
        _handle_error(e)


@workflows.command("remove")
@click.option("--contact-id", required=True, help="Contact ID to remove")
@click.option("--workflow-id", required=True, help="Workflow ID")
@click.pass_context
def workflows_remove(ctx, contact_id, workflow_id):
    """Remove a contact from a workflow (public API)."""
    try:
        data = api.delete(f"/contacts/{contact_id}/workflow/{workflow_id}")
        _output(ctx, data, "Contact Removed from Workflow")
    except Exception as e:
        _handle_error(e)


@workflows.command("create")
@click.option("--name", required=True, help="Workflow name")
@click.option("--folder", default=None, help="Folder name (created if needed)")
@click.option("--from-json", "json_file", required=True, type=click.Path(exists=True),
              help="Campaign JSON file path")
@click.option("--force", is_flag=True,
              help="Criar mesmo com erros de validação (não recomendado)")
@click.pass_context
def workflows_create(ctx, name, folder, json_file, force):
    """Create workflows from a campaign JSON file (experimental, internal API).

    The JSON file should contain a campaign dict where each key is a workflow
    with 'name', 'templates' (linked steps), and optional 'tag' (trigger).
    """
    _require_experimental(ctx)
    try:
        from cli_anything.gohighlevel.utils.workflow_builder import CampaignBuilder

        with open(json_file) as f:
            campaign = json.load(f)

        client = _get_internal_client(ctx)
        builder = CampaignBuilder(client)
        stats = builder.build(campaign, folder or name, strict=not force)

        if _is_json(ctx):
            click.echo(json.dumps(stats, indent=2, default=str))
        else:
            click.echo(builder.format_summary())
    except Exception as e:
        _handle_error(e)


@workflows.command("create-step")
@click.option("--type", "step_type", required=True,
              type=click.Choice(["email", "sms", "wait", "tag", "webhook", "ai"]))
@click.option("--name", required=True, help="Step name")
@click.option("--output-file", "out_file", required=True, type=click.Path(),
              help="JSON file to append step to")
@click.option("--subject", default=None, help="Email subject (email type)")
@click.option("--body", default=None, help="Message body (email/sms type)")
@click.option("--from-name", default="", help="Sender name (email type)")
@click.option("--value", default=None, type=int, help="Wait value (wait type)")
@click.option("--unit", default="days", type=click.Choice(["minutes", "hours", "days"]),
              help="Wait unit (wait type)")
@click.option("--tags", default=None, help="Comma-separated tags (tag type)")
@click.option("--remove-tags", is_flag=True, help="Remove tags instead of add (tag type)")
@click.option("--url", default=None, help="Webhook URL (webhook type)")
@click.option("--method", default="POST", help="HTTP method (webhook type)")
@click.option("--prompt", default=None, help="AI prompt (ai type)")
@click.option("--model", default="gpt-4o", help="AI model (ai type)")
@click.pass_context
def workflows_create_step(ctx, step_type, name, out_file, subject, body, from_name,
                          value, unit, tags, remove_tags, url, method, prompt, model):
    """Build a workflow step and append to a JSON file (experimental).

    Use repeatedly to build up a workflow step-by-step, then pass the
    file to 'workflows create --from-json'.
    """
    _require_experimental(ctx)
    try:
        from cli_anything.gohighlevel.utils import workflow_builder as wb

        if step_type == "email":
            if not subject or not body:
                click.echo("Error: --subject and --body required for email step", err=True)
                sys.exit(1)
            step = wb.email_step(name, subject, body, from_name)
        elif step_type == "sms":
            if not body:
                click.echo("Error: --body required for sms step", err=True)
                sys.exit(1)
            step = wb.sms_step(name, body)
        elif step_type == "wait":
            if value is None:
                click.echo("Error: --value required for wait step", err=True)
                sys.exit(1)
            step = wb.wait_step(name, value, unit)
        elif step_type == "tag":
            if not tags:
                click.echo("Error: --tags required for tag step", err=True)
                sys.exit(1)
            step = wb.tag_step(name, [t.strip() for t in tags.split(",")], remove=remove_tags)
        elif step_type == "webhook":
            if not url:
                click.echo("Error: --url required for webhook step", err=True)
                sys.exit(1)
            step = wb.webhook_step(name, url, method)
        elif step_type == "ai":
            if not prompt:
                click.echo("Error: --prompt required for ai step", err=True)
                sys.exit(1)
            step = wb.ai_step(name, prompt, model)
        else:
            click.echo(f"Error: Unknown step type: {step_type}", err=True)
            sys.exit(1)

        # Load existing or start fresh
        import os
        if os.path.exists(out_file):
            with open(out_file) as f:
                steps = json.load(f)
        else:
            steps = []

        steps.append(step)

        # Auto-link all steps
        linked = wb.link_steps(steps)
        with open(out_file, "w") as f:
            json.dump(linked, f, indent=2)

        if _is_json(ctx):
            click.echo(json.dumps(step, indent=2))
        else:
            click.echo(f"Step added: {step['name']} ({step['type']})")
            click.echo(f"Total steps in {out_file}: {len(linked)}")
    except Exception as e:
        _handle_error(e)


@workflows.command("create-n8n")
@click.option("--name", required=True, help="Workflow name")
@click.option("--webhook-url", required=True, help="n8n webhook URL")
@click.option("--tag", default=None, help="Trigger tag (creates tag trigger)")
@click.option("--folder", default=None, help="Folder name")
@click.pass_context
def workflows_create_n8n(ctx, name, webhook_url, tag, folder):
    """Create a minimal GHL workflow that triggers an n8n webhook (experimental).

    Creates: [tag trigger] → [webhook POST to n8n URL]
    """
    _require_experimental(ctx)
    try:
        from cli_anything.gohighlevel.utils import workflow_builder as wb

        # A tag vira GATILHO (campo "tag" da campanha), não uma ação do fluxo.
        steps = [wb.webhook_step(f"n8n: {name}", webhook_url, "POST")]
        linked = wb.link_steps(steps)
        campaign = {
            "n8n_bridge": {
                "name": name,
                "templates": linked,
                "tag": tag,
            }
        }

        from cli_anything.gohighlevel.utils.workflow_builder import CampaignBuilder
        client = _get_internal_client(ctx)
        builder = CampaignBuilder(client)
        stats = builder.build(campaign, folder or f"n8n-{name}")

        if _is_json(ctx):
            click.echo(json.dumps(stats, indent=2, default=str))
        else:
            click.echo(builder.format_summary())
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# DOCUMENTS / CONTRACTS
# ===========================================================================

@cli.group()
@click.pass_context
def documents(ctx):
    """Documents, contracts, and proposals — list, send, templates."""
    pass


@documents.command("list")
@click.option("--status", default=None, type=click.Choice(["draft", "sent", "viewed", "completed", "accepted"]))
@click.option("--payment-status", default=None, type=click.Choice(["waiting_for_payment", "paid", "no_payment"]))
@click.option("--limit", default=20)
@click.option("--offset", "skip", default=0)
@click.option("--query", default=None, help="Search by name")
@click.pass_context
def documents_list(ctx, status, payment_status, limit, skip, query):
    """List documents/contracts."""
    try:
        params = {"locationId": _loc(ctx), "limit": limit, "skip": skip}
        if status:
            params["status"] = status
        if payment_status:
            params["paymentStatus"] = payment_status
        if query:
            params["query"] = query
        data = api.get("/proposals/document", params=params)
        _output(ctx, data, "Documents")
    except Exception as e:
        _handle_error(e)


@documents.command("templates")
@click.option("--type", "template_type", default=None, type=click.Choice(["proposal", "estimate", "contentLibrary"]))
@click.option("--name", default=None, help="Filter by template name")
@click.option("--limit", default=20)
@click.pass_context
def documents_templates(ctx, template_type, name, limit):
    """List document/contract templates."""
    try:
        params = {"locationId": _loc(ctx), "limit": limit}
        if template_type:
            params["type"] = template_type
        if name:
            params["name"] = name
        data = api.get("/proposals/templates", params=params)
        _output(ctx, data, "Document Templates")
    except Exception as e:
        _handle_error(e)


@documents.command("send")
@click.option("--document-id", required=True, help="Document ID to send")
@click.option("--sent-by", required=True, help="User ID of sender")
@click.option("--medium", default="email", type=click.Choice(["email", "link"]), help="Delivery method")
@click.option("--name", "document_name", default=None, help="Document name override")
@click.pass_context
def documents_send(ctx, document_id, sent_by, medium, document_name):
    """Send an existing document to its recipients."""
    try:
        body = {
            "locationId": _loc(ctx),
            "documentId": document_id,
            "sentBy": sent_by,
            "medium": medium,
        }
        if document_name:
            body["documentName"] = document_name
        data = api.post("/proposals/document/send", data=body)
        _output(ctx, data, "Document Sent")
    except Exception as e:
        _handle_error(e)


@documents.command("send-template")
@click.option("--template-id", required=True, help="Template ID")
@click.option("--contact-id", required=True, help="Contact ID to send to")
@click.option("--user-id", required=True, help="User ID (sender)")
@click.option("--opportunity-id", default=None, help="Link to opportunity")
@click.option("--send/--no-send", "send_document", default=True, help="Send immediately or just create")
@click.pass_context
def documents_send_template(ctx, template_id, contact_id, user_id, opportunity_id, send_document):
    """Create and send a contract from a template."""
    try:
        body = {
            "templateId": template_id,
            "contactId": contact_id,
            "userId": user_id,
            "locationId": _loc(ctx),
            "sendDocument": send_document,
        }
        if opportunity_id:
            body["opportunityId"] = opportunity_id
        data = api.post("/proposals/templates/send", data=body)
        _output(ctx, data, "Template Sent")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# CONVERSATIONS
# ===========================================================================

@cli.group()
@click.pass_context
def conversations(ctx):
    """Manage conversations and messages."""
    pass


@conversations.command("list")
@click.option("--limit", default=20)
@click.option("--status", default=None, type=click.Choice(["all", "read", "unread", "starred"]))
@click.option("--type", "msg_type", default=None,
              type=click.Choice(["Email", "SMS", "WhatsApp", "GMB", "IG", "FB", "Live_Chat", "Custom"]),
              help="Filter by last message type")
@click.pass_context
def conversations_list(ctx, limit, status, msg_type):
    """List conversations. Use --type Email to see email conversations."""
    try:
        # API uses TYPE_EMAIL format for lastMessageType filter
        TYPE_MAP = {
            "Email": "TYPE_EMAIL", "SMS": "TYPE_SMS", "WhatsApp": "TYPE_WHATSAPP",
            "GMB": "TYPE_GMB", "IG": "TYPE_INSTAGRAM", "FB": "TYPE_FACEBOOK",
            "Live_Chat": "TYPE_LIVE_CHAT", "Custom": "TYPE_CUSTOM",
        }
        params = {"locationId": _loc(ctx), "limit": limit}
        if status:
            params["status"] = status
        if msg_type:
            params["lastMessageType"] = TYPE_MAP.get(msg_type, f"TYPE_{msg_type.upper()}")
        data = api.get("/conversations/search", params=params)
        _output(ctx, data, "Conversations")
    except Exception as e:
        _handle_error(e)


@conversations.command("get")
@click.argument("conversation_id")
@click.pass_context
def conversations_get(ctx, conversation_id):
    """Get conversation details."""
    try:
        data = api.get(f"/conversations/{conversation_id}")
        _output(ctx, data, "Conversation Details")
    except Exception as e:
        _handle_error(e)


@conversations.command("messages")
@click.argument("conversation_id")
@click.option("--limit", default=20)
@click.option("--type", "msg_type", default=None,
              type=click.Choice(["Email", "SMS", "WhatsApp", "GMB", "IG", "FB", "Live_Chat", "Custom"]),
              help="Filter messages by type")
@click.pass_context
def conversations_messages(ctx, conversation_id, limit, msg_type):
    """Get messages in a conversation. Use --type Email for email messages only."""
    try:
        TYPE_MAP = {
            "Email": "TYPE_EMAIL", "SMS": "TYPE_SMS", "WhatsApp": "TYPE_WHATSAPP",
            "GMB": "TYPE_GMB", "IG": "TYPE_INSTAGRAM", "FB": "TYPE_FACEBOOK",
            "Live_Chat": "TYPE_LIVE_CHAT", "Custom": "TYPE_CUSTOM",
        }
        params = {"limit": limit}
        if msg_type:
            params["type"] = TYPE_MAP.get(msg_type, f"TYPE_{msg_type.upper()}")
        data = api.get(f"/conversations/{conversation_id}/messages", params=params)
        _output(ctx, data, "Messages")
    except Exception as e:
        _handle_error(e)


@conversations.command("get-email")
@click.argument("email_message_id")
@click.pass_context
def conversations_get_email(ctx, email_message_id):
    """Get full email details (subject, body, headers, attachments).

    Two-step workflow: list conversations --type Email → get message IDs → get-email <id>
    """
    try:
        data = api.get(f"/conversations/messages/email/{email_message_id}")
        _output(ctx, data, "Email Details")
    except Exception as e:
        _handle_error(e)


@conversations.command("send")
@click.option("--contact-id", default=None, help="Contact ID (forma preferida)")
@click.option("--conversation-id", default=None,
              help="Conversation ID — o contato é resolvido automaticamente")
@click.option("--type", "msg_type", default="SMS",
              type=click.Choice(["SMS", "Email", "WhatsApp", "GMB", "IG", "FB", "Live_Chat", "Custom"]))
@click.option("--message", required=True, help="Message text")
@click.option("--subject", default=None, help="Assunto (apenas type=Email)")
@click.option("--html", default=None, help="Corpo HTML (apenas type=Email)")
@click.option("--attachment", "attachments", multiple=True, help="URL de anexo (repetível)")
@click.pass_context
def conversations_send(ctx, contact_id, conversation_id, msg_type, message,
                       subject, html, attachments):
    """Envia mensagem para um contato.

    A API do GHL envia por contactId, não por conversationId. Se você só tem o
    ID da conversa, passe --conversation-id que o CLI resolve o contato.
    """
    try:
        if not contact_id and not conversation_id:
            raise click.UsageError("Informe --contact-id ou --conversation-id.")
        if not contact_id:
            convo = api.get(f"/conversations/{conversation_id}")
            payload = convo.get("conversation", convo)
            contact_id = payload.get("contactId")
            if not contact_id:
                raise click.ClickException(
                    f"Não foi possível resolver o contato da conversa {conversation_id}."
                )
        body = {"type": msg_type, "message": message, "contactId": contact_id}
        if msg_type == "Email":
            if subject:
                body["subject"] = subject
            if html:
                body["html"] = html
        if attachments:
            body["attachments"] = list(attachments)
        data = api.post("/conversations/messages", data=body)
        _output(ctx, data, "Message Sent")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# EMAILS
# ===========================================================================

@cli.group()
@click.pass_context
def emails(ctx):
    """Email campaigns and templates."""
    pass


@emails.command("list-campaigns")
@click.option("--status", default=None, help="Filter by status")
@click.pass_context
def emails_list_campaigns(ctx, status):
    """List email campaigns. Note: Uses the campaigns API."""
    try:
        params = {"locationId": _loc(ctx)}
        if status:
            params["status"] = status
        data = api.get("/campaigns/", params=params)
        _output(ctx, data, "Email Campaigns")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# PAYMENTS
# ===========================================================================

@cli.group()
@click.pass_context
def payments(ctx):
    """Payments, invoices, transactions, and orders."""
    pass


@payments.command("transactions")
@click.option("--limit", default=20)
@click.option("--offset", default=0)
@click.option("--contact-id", default=None)
@click.pass_context
def payments_transactions(ctx, limit, offset, contact_id):
    """List transactions."""
    try:
        params = {"altId": _loc(ctx), "altType": "location", "limit": limit, "offset": offset}
        if contact_id:
            params["contactId"] = contact_id
        data = api.get("/payments/transactions", params=params)
        _output(ctx, data, "Transactions")
    except Exception as e:
        _handle_error(e)


@payments.command("orders")
@click.option("--limit", default=20)
@click.option("--offset", default=0)
@click.pass_context
def payments_orders(ctx, limit, offset):
    """List orders."""
    try:
        params = {"altId": _loc(ctx), "altType": "location", "limit": limit, "offset": offset}
        data = api.get("/payments/orders", params=params)
        _output(ctx, data, "Orders")
    except Exception as e:
        _handle_error(e)


@payments.command("invoices")
@click.option("--limit", default=20)
@click.option("--offset", default=0)
@click.option("--status", default=None, type=click.Choice(["draft", "sent", "paid", "void"]))
@click.option("--contact-id", default=None)
@click.pass_context
def payments_invoices(ctx, limit, offset, status, contact_id):
    """List invoices."""
    try:
        params = {"altId": _loc(ctx), "altType": "location", "limit": limit, "offset": offset}
        if status:
            params["status"] = status
        if contact_id:
            params["contactId"] = contact_id
        data = api.get("/invoices/", params=params)
        _output(ctx, data, "Invoices")
    except Exception as e:
        _handle_error(e)


@payments.command("create-invoice")
@click.option("--contact-id", required=True, help="Contact ID")
@click.option("--name", required=True, help="Nome/título da fatura")
@click.option("--amount", default=None, type=float,
              help="Valor do item único (na moeda, não em centavos)")
@click.option("--item", "items", multiple=True,
              help='Item no formato "Descrição:valor:qtd" (repetível)')
@click.option("--due-date", required=True, help="Vencimento (YYYY-MM-DD)")
@click.option("--issue-date", default=None, help="Emissão (YYYY-MM-DD). Default: hoje")
@click.option("--currency", default=None, help="Default: GHL_CURRENCY ou BRL")
@click.option("--draft", is_flag=True, help="Criar como rascunho (não envia)")
@click.pass_context
def payments_create_invoice(ctx, contact_id, name, amount, items, due_date,
                            issue_date, currency, draft):
    """Cria uma fatura.

    A API exige contactDetails, items e datas — o CLI resolve os dados do
    contato automaticamente a partir do --contact-id.
    """
    try:
        import os
        from datetime import date

        if not items and amount is None:
            raise click.UsageError("Informe --amount ou pelo menos um --item.")

        parsed_items = []
        for raw in items:
            parts = raw.split(":")
            if len(parts) < 2:
                raise click.UsageError(f'Item inválido: "{raw}". Use "Descrição:valor:qtd".')
            qty = int(parts[2]) if len(parts) > 2 and parts[2] else 1
            parsed_items.append({
                "name": parts[0].strip(),
                "currency": currency or os.environ.get("GHL_CURRENCY", "BRL"),
                "amount": float(parts[1]),
                "qty": qty,
            })
        if not parsed_items:
            parsed_items = [{
                "name": name,
                "currency": currency or os.environ.get("GHL_CURRENCY", "BRL"),
                "amount": float(amount),
                "qty": 1,
            }]

        contact = api.get(f"/contacts/{contact_id}")
        c = contact.get("contact", contact)
        contact_details = {
            "id": contact_id,
            "name": c.get("contactName") or " ".join(
                filter(None, [c.get("firstName"), c.get("lastName")])
            ) or c.get("email", ""),
            "email": c.get("email", ""),
        }
        if c.get("phone"):
            contact_details["phoneNo"] = c["phone"]

        body = {
            "altId": _loc(ctx),
            "altType": "location",
            "name": name,
            "title": name,
            "currency": currency or os.environ.get("GHL_CURRENCY", "BRL"),
            "contactDetails": contact_details,
            "items": parsed_items,
            "issueDate": issue_date or date.today().isoformat(),
            "dueDate": due_date,
            "liveMode": not draft,
            "businessDetails": {"name": os.environ.get("GHL_BUSINESS_NAME", name)},
        }
        data = api.post("/invoices/", data=body)
        _output(ctx, data, "Invoice Created")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# FORMS
# ===========================================================================

@cli.group()
@click.pass_context
def forms(ctx):
    """Forms and form submissions."""
    pass


@forms.command("list")
@click.option("--limit", default=20)
@click.option("--offset", "skip", default=0)
@click.option("--type", "form_type", default=None, help="Form type filter")
@click.pass_context
def forms_list(ctx, limit, skip, form_type):
    """List forms."""
    try:
        params = {"locationId": _loc(ctx), "limit": limit, "skip": skip}
        if form_type:
            params["type"] = form_type
        data = api.get("/forms/", params=params)
        _output(ctx, data, "Forms")
    except Exception as e:
        _handle_error(e)


@forms.command("submissions")
@click.argument("form_id")
@click.option("--limit", default=20)
@click.option("--page", default=1)
@click.pass_context
def forms_submissions(ctx, form_id, limit, page):
    """Get form submissions."""
    try:
        params = {"locationId": _loc(ctx), "limit": limit, "page": page}
        data = api.get(f"/forms/submissions", params={"formId": form_id, **params})
        _output(ctx, data, f"Submissions for form {form_id}")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# SOCIAL MEDIA
# ===========================================================================

@cli.group()
@click.pass_context
def social(ctx):
    """Social media posts and analytics."""
    pass


@social.command("accounts")
@click.pass_context
def social_accounts(ctx):
    """List connected social media accounts."""
    try:
        data = api.get(f"/social-media-posting/{_loc(ctx)}/accounts")
        _output(ctx, data, "Social Accounts")
    except Exception as e:
        _handle_error(e)


@social.command("posts")
@click.option("--limit", default=20)
@click.option("--offset", "skip", default=0)
@click.option("--type", "post_type", default=None, help="Filter by post type")
@click.pass_context
def social_posts(ctx, limit, skip, post_type):
    """List social media posts."""
    try:
        params = {"locationId": _loc(ctx), "limit": limit, "skip": skip}
        if post_type:
            params["type"] = post_type
        data = api.post(f"/social-media-posting/{_loc(ctx)}/posts/list", data=params)
        _output(ctx, data, "Social Posts")
    except Exception as e:
        _handle_error(e)


@social.command("create-post")
@click.option("--account-id", required=True, multiple=True, help="Social account IDs (repeatable)")
@click.option("--text", required=True, help="Post text content")
@click.option("--media-url", default=None, multiple=True, help="Media URLs (repeatable)")
@click.option("--schedule", default=None, help="Schedule time (ISO 8601)")
@click.pass_context
def social_create_post(ctx, account_id, text, media_url, schedule):
    """Create a social media post."""
    try:
        body = {
            "locationId": _loc(ctx),
            "accountIds": list(account_id),
            "summary": text,
        }
        if media_url:
            body["media"] = [{"url": u, "type": "image"} for u in media_url]
        if schedule:
            body["scheduledAt"] = schedule
        data = api.post(f"/social-media-posting/{_loc(ctx)}/posts", data=body)
        _output(ctx, data, "Post Created")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# LOCATIONS
# ===========================================================================

@cli.group()
@click.pass_context
def locations(ctx):
    """Location/sub-account management."""
    pass


@locations.command("get")
@click.pass_context
def locations_get(ctx):
    """Get current location details."""
    try:
        data = api.get(f"/locations/{_loc(ctx)}")
        _output(ctx, data, "Location Details")
    except Exception as e:
        _handle_error(e)


@locations.command("search")
@click.option("--company-id", required=True, help="Company/Agency ID")
@click.option("--limit", default=20)
@click.option("--offset", "skip", default=0)
@click.option("--query", default=None, help="Search query")
@click.pass_context
def locations_search(ctx, company_id, limit, skip, query):
    """Search locations (requires company-level access)."""
    try:
        params = {"companyId": company_id, "limit": limit, "skip": skip}
        if query:
            params["query"] = query
        data = api.get("/locations/search", params=params)
        _output(ctx, data, "Locations")
    except Exception as e:
        _handle_error(e)


@locations.command("tags")
@click.pass_context
def locations_tags(ctx):
    """List tags for current location."""
    try:
        data = api.get(f"/locations/{_loc(ctx)}/tags")
        _output(ctx, data, "Location Tags")
    except Exception as e:
        _handle_error(e)


@locations.command("custom-fields")
@click.pass_context
def locations_custom_fields(ctx):
    """List custom fields for current location."""
    try:
        data = api.get(f"/locations/{_loc(ctx)}/customFields")
        _output(ctx, data, "Custom Fields")
    except Exception as e:
        _handle_error(e)


@locations.command("custom-values")
@click.pass_context
def locations_custom_values(ctx):
    """List custom values for current location."""
    try:
        data = api.get(f"/locations/{_loc(ctx)}/customValues")
        _output(ctx, data, "Custom Values")
    except Exception as e:
        _handle_error(e)


@locations.command("create-tag")
@click.argument("name")
@click.pass_context
def locations_create_tag(ctx, name):
    """Cria uma tag na subconta."""
    try:
        data = api.post(f"/locations/{_loc(ctx)}/tags", data={"name": name})
        _output(ctx, data, "Tag criada")
    except Exception as e:
        _handle_error(e)


DATA_TYPES = [
    "TEXT", "LARGE_TEXT", "NUMERICAL", "PHONE", "MONETORY", "CHECKBOX",
    "SINGLE_OPTIONS", "MULTIPLE_OPTIONS", "DATE", "TEXTBOX_LIST",
    "FILE_UPLOAD", "RADIO", "EMAIL",
]


@locations.command("create-custom-field")
@click.option("--name", required=True, help="Nome do campo (ex.: CF_DRIVE_LINK)")
@click.option("--data-type", default="TEXT", type=click.Choice(DATA_TYPES))
@click.option("--model", default="contact", type=click.Choice(["contact", "opportunity"]))
@click.option("--placeholder", default=None)
@click.option("--option", "options", multiple=True,
              help="Opção de lista (repetível — para SINGLE_OPTIONS/MULTIPLE_OPTIONS/RADIO)")
@click.pass_context
def locations_create_custom_field(ctx, name, data_type, model, placeholder, options):
    """Cria um custom field na subconta."""
    try:
        body = {"name": name, "dataType": data_type, "model": model}
        if placeholder:
            body["placeholder"] = placeholder
        if options:
            body["options"] = list(options)
        data = api.post(f"/locations/{_loc(ctx)}/customFields", data=body)
        _output(ctx, data, "Custom field criado")
    except Exception as e:
        _handle_error(e)


@locations.command("create-custom-value")
@click.option("--name", required=True, help="Nome do custom value")
@click.option("--value", required=True, help="Conteúdo")
@click.pass_context
def locations_create_custom_value(ctx, name, value):
    """Cria um custom value na subconta."""
    try:
        data = api.post(f"/locations/{_loc(ctx)}/customValues",
                        data={"name": name, "value": value})
        _output(ctx, data, "Custom value criado")
    except Exception as e:
        _handle_error(e)


@locations.command("bootstrap-fields")
@click.option("--from-file", "file_path", required=True, type=click.Path(exists=True),
              help='JSON: [{"name":"CF_DRIVE_LINK","dataType":"TEXT"}, ...]')
@click.option("--dry-run", is_flag=True, help="Só mostra o que seria criado")
@click.pass_context
def locations_bootstrap_fields(ctx, file_path, dry_run):
    """Cria vários custom fields de uma vez a partir de um arquivo JSON.

    Campos já existentes são pulados — o comando é idempotente.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            wanted = json.load(f)
        if not isinstance(wanted, list):
            raise click.UsageError("O arquivo deve conter uma lista de objetos.")

        existing_raw = api.get(f"/locations/{_loc(ctx)}/customFields")
        existing = {
            (f.get("name") or "").strip().lower()
            for f in existing_raw.get("customFields", [])
        }

        created, skipped, failed = [], [], []
        for item in wanted:
            name = (item.get("name") or "").strip()
            if not name:
                failed.append({"item": item, "error": "sem 'name'"})
                continue
            if name.lower() in existing:
                skipped.append(name)
                continue
            if dry_run:
                created.append(name)
                continue
            body = {
                "name": name,
                "dataType": item.get("dataType", "TEXT"),
                "model": item.get("model", "contact"),
            }
            if item.get("options"):
                body["options"] = item["options"]
            if item.get("placeholder"):
                body["placeholder"] = item["placeholder"]
            try:
                api.post(f"/locations/{_loc(ctx)}/customFields", data=body)
                created.append(name)
            except Exception as exc:  # noqa: BLE001
                failed.append({"item": name, "error": str(exc)})

        result = {"created": created, "skipped": skipped, "failed": failed,
                  "dry_run": dry_run}
        if _is_json(ctx):
            click.echo(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            prefixo = "[dry-run] " if dry_run else ""
            click.echo(f"{prefixo}Criados: {len(created)} | Já existiam: {len(skipped)} | Falhas: {len(failed)}")
            for n in created:
                click.echo(f"  + {n}")
            for n in skipped:
                click.echo(f"  = {n} (já existia)")
            for f in failed:
                click.echo(f"  ! {f['item']}: {f['error']}", err=True)
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# USERS
# ===========================================================================

@cli.group()
@click.pass_context
def users(ctx):
    """Usuários da subconta (para atribuição de responsável)."""
    pass


@users.command("list")
@click.pass_context
def users_list(ctx):
    """Lista usuários da subconta."""
    try:
        data = api.get("/users/", params={"locationId": _loc(ctx)})
        _output(ctx, data, "Usuários")
    except Exception as e:
        _handle_error(e)


# ===========================================================================
# DOCTOR — validação de setup
# ===========================================================================

@cli.command()
@click.pass_context
def doctor(ctx):
    """Valida credenciais, conectividade e escopos antes de você depender do CLI."""
    import os

    api.load_env()
    checks: list[tuple[str, str, str]] = []  # (status, item, detalhe)

    key = os.environ.get("GHL_API_KEY", "").strip()
    if not key:
        checks.append(("FALHA", "GHL_API_KEY", "não definida no .env"))
    elif not key.startswith("pit-"):
        checks.append(("AVISO", "GHL_API_KEY", "não parece um Private Integration Token (pit-...)"))
    else:
        checks.append(("OK", "GHL_API_KEY", f"...{key[-6:]}"))

    loc = (ctx.obj or {}).get("location_id") or os.environ.get("GHL_LOCATION_ID", "").strip()
    if not loc:
        checks.append(("FALHA", "GHL_LOCATION_ID", "não definida"))
    else:
        checks.append(("OK", "GHL_LOCATION_ID", loc))

    if key and loc:
        probes = [
            ("locations", lambda: api.get(f"/locations/{loc}")),
            ("contacts", lambda: api.get("/contacts/", params={"locationId": loc, "limit": 1})),
            ("opportunities", lambda: api.get("/opportunities/search", params={"location_id": loc, "limit": 1})),
            ("calendars", lambda: api.get("/calendars/", params={"locationId": loc})),
            ("workflows", lambda: api.get("/workflows/", params={"locationId": loc})),
            ("custom fields", lambda: api.get(f"/locations/{loc}/customFields")),
        ]
        for label, fn in probes:
            try:
                fn()
                checks.append(("OK", f"escopo: {label}", "leitura autorizada"))
            except requests.exceptions.HTTPError as exc:
                code = exc.response.status_code if exc.response is not None else "?"
                detalhe = "sem escopo no token" if code in (401, 403) else f"HTTP {code}"
                checks.append(("FALHA", f"escopo: {label}", detalhe))
            except Exception as exc:  # noqa: BLE001
                checks.append(("FALHA", f"escopo: {label}", str(exc)[:80]))

    refresh = os.environ.get("GHL_FIREBASE_REFRESH_TOKEN", "").strip()
    fb_key = os.environ.get("GHL_FIREBASE_API_KEY", "").strip()
    if not refresh or not fb_key:
        checks.append(("AVISO", "API interna", "sem token Firebase — criação de workflow indisponível"))
    else:
        try:
            from cli_anything.gohighlevel.utils.ghl_internal_client import (
                InternalGHLClient, TokenManager,
            )
            client = InternalGHLClient(TokenManager(), loc)
            result = client.ping()
            if result.get("_error"):
                checks.append(("FALHA", "API interna", result["_error"]))
            else:
                checks.append(("OK", "API interna", "token válido — criação de workflow liberada"))
        except Exception as exc:  # noqa: BLE001
            checks.append(("FALHA", "API interna", str(exc).splitlines()[0][:100]))

    if _is_json(ctx):
        click.echo(json.dumps(
            [{"status": s, "item": i, "detail": d} for s, i, d in checks],
            indent=2, ensure_ascii=False,
        ))
    else:
        icons = {"OK": "✓", "AVISO": "!", "FALHA": "✗"}
        click.echo("\nDiagnóstico do setup")
        click.echo("-" * 20)
        for status, item, detail in checks:
            click.echo(f" {icons[status]} {item}: {detail}")
        falhas = sum(1 for s, _, _ in checks if s == "FALHA")
        click.echo(f"\n{len(checks) - falhas}/{len(checks)} verificações OK")

    if any(s == "FALHA" for s, _, _ in checks):
        sys.exit(1)


# ===========================================================================
# Entry point
# ===========================================================================

def main():
    cli(obj={})


if __name__ == "__main__":
    main()
