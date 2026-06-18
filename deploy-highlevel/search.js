/* Global search overlay for the HighLevel guide.
 * Loads search-index.json on first open, then fuzzy-matches against
 * the trigger/action name (PT + EN), category, tags, and the
 * data-name keyword list. ⌘K / Ctrl+K opens it. Esc closes.
 */
(function () {
  'use strict';

  const STYLE = `
.mf-search-fab {
  position: fixed; bottom: 24px; right: 24px; z-index: 9998;
  background: var(--brand-accent, #FEB902); color: #0B223F;
  border: none; border-radius: 999px;
  padding: 12px 18px; font: 600 14px/1 'Poppins', sans-serif;
  cursor: pointer; box-shadow: 0 8px 24px rgba(0,0,0,0.35);
  display: flex; align-items: center; gap: 8px;
  transition: transform .15s ease, box-shadow .15s ease;
}
.mf-search-fab:hover { transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0,0,0,0.45); }
.mf-search-fab kbd {
  background: rgba(11,34,63,0.15); padding: 2px 6px; border-radius: 4px;
  font: 600 11px/1 'JetBrains Mono', monospace; color: inherit;
}
.mf-search-overlay {
  position: fixed; inset: 0; z-index: 10000;
  background: rgba(8, 17, 32, 0.85); backdrop-filter: blur(6px);
  display: none; align-items: flex-start; justify-content: center;
  padding-top: 12vh;
}
.mf-search-overlay[data-open="1"] { display: flex; }
.mf-search-modal {
  width: min(720px, 92vw);
  background: #0E1E37; border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; overflow: hidden;
  box-shadow: 0 32px 80px rgba(0,0,0,0.5);
  font-family: 'Poppins', sans-serif;
}
.mf-search-header {
  display: flex; align-items: center; gap: 12px;
  padding: 16px 18px; border-bottom: 1px solid rgba(255,255,255,0.06);
}
.mf-search-icon { font-size: 18px; opacity: 0.7; color: #FEB902; }
.mf-search-input {
  flex: 1; background: transparent; border: 0; outline: 0;
  color: #fff; font-size: 16px; font-family: inherit;
}
.mf-search-input::placeholder { color: rgba(255,255,255,0.45); }
.mf-search-clear {
  background: rgba(255,255,255,0.06); border: 0; color: rgba(255,255,255,0.6);
  padding: 4px 10px; border-radius: 4px; cursor: pointer;
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
}
.mf-search-results {
  max-height: 56vh; overflow-y: auto;
}
.mf-search-empty {
  padding: 32px 20px; text-align: center; color: rgba(255,255,255,0.45);
  font-size: 13px;
}
.mf-search-section {
  padding: 8px 18px 4px; font: 500 11px/1 'JetBrains Mono', monospace;
  letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.4);
}
.mf-search-item {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 18px; cursor: pointer;
  border-left: 3px solid transparent;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
}
.mf-search-item.active,
.mf-search-item:hover {
  background: rgba(91, 155, 255, 0.08);
  border-left-color: var(--brand-accent, #FEB902);
}
.mf-search-badge {
  font: 600 10px/1 'JetBrains Mono', monospace;
  padding: 4px 8px; border-radius: 4px;
  text-transform: uppercase; letter-spacing: 0.08em;
  flex-shrink: 0;
}
.mf-search-badge.gat { background: rgba(139,92,246,0.18); color: #c4b5fd; }
.mf-search-badge.acao { background: rgba(91,155,255,0.16); color: #93c5fd; }
.mf-search-text { flex: 1; min-width: 0; }
.mf-search-title { font-size: 14px; font-weight: 500; color: #fff; }
.mf-search-title mark { background: rgba(254,185,2,0.25); color: inherit; padding: 0 2px; border-radius: 2px; }
.mf-search-meta {
  font-size: 11px; color: rgba(255,255,255,0.45);
  display: flex; gap: 8px; align-items: center; margin-top: 2px;
}
.mf-search-meta .dot { opacity: 0.5; }
.mf-search-footer {
  display: flex; gap: 16px; align-items: center; justify-content: flex-end;
  padding: 10px 18px; border-top: 1px solid rgba(255,255,255,0.06);
  background: rgba(0,0,0,0.18);
  font-size: 11px; color: rgba(255,255,255,0.45);
}
.mf-search-footer kbd {
  background: rgba(255,255,255,0.08); padding: 2px 6px; border-radius: 3px;
  font-family: 'JetBrains Mono', monospace; color: rgba(255,255,255,0.7);
  margin-right: 4px;
}
@media (max-width: 640px) {
  .mf-search-fab { padding: 12px 14px; }
  .mf-search-fab .label { display: none; }
  .mf-search-overlay { padding-top: 6vh; }
}
`;

  let index = null;
  let indexPromise = null;

  function loadIndex() {
    if (indexPromise) return indexPromise;
    const here = location.pathname.replace(/[^/]+$/, '');
    indexPromise = fetch(here + 'search-index.json')
      .then(r => r.json())
      .then(d => { index = d.items || []; return index; })
      .catch(() => { index = []; return index; });
    return indexPromise;
  }

  // Simple fuzzy: case-insensitive, all query tokens must appear somewhere
  // in the haystack (name + en + category + tags + keywords). Scoring favours
  // matches in name, then en, then keywords.
  function search(q) {
    if (!q.trim()) return [];
    const tokens = q.toLowerCase().split(/\s+/).filter(Boolean);
    const out = [];
    for (const item of index) {
      const name = (item.name || '').toLowerCase();
      const en = (item.en || '').toLowerCase();
      const cat = (item.category || '').toLowerCase();
      const tags = (item.tags || []).join(' ').toLowerCase();
      const kw = (item.keywords || '').toLowerCase();
      const desc = (item.description || '').toLowerCase();
      const hay = [name, en, cat, tags, kw, desc].join(' ');
      if (!tokens.every(t => hay.includes(t))) continue;
      let score = 0;
      for (const t of tokens) {
        if (name.startsWith(t)) score += 50;
        else if (name.includes(t)) score += 30;
        if (en.toLowerCase().startsWith(t)) score += 25;
        else if (en.includes(t)) score += 15;
        if (kw.includes(t)) score += 8;
        if (tags.includes(t)) score += 5;
      }
      out.push({ item, score });
    }
    out.sort((a, b) => b.score - a.score);
    return out.slice(0, 24).map(x => x.item);
  }

  function highlight(text, q) {
    if (!q.trim()) return text;
    const tokens = q.trim().split(/\s+/).filter(Boolean);
    let out = text;
    for (const t of tokens) {
      const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
      out = out.replace(re, '<mark>$1</mark>');
    }
    return out;
  }

  function render(results, q) {
    if (!q.trim()) {
      return `<div class="mf-search-empty">Digite pra buscar entre <strong>${index ? index.length : '—'}</strong> gatilhos e ações.</div>`;
    }
    if (!results.length) {
      return `<div class="mf-search-empty">Nada encontrado pra <em>"${q.replace(/</g, '&lt;')}"</em>.</div>`;
    }
    const groups = { Gatilho: [], 'Ação': [] };
    results.forEach(r => groups[r.type].push(r));
    let html = '';
    let idx = 0;
    for (const t of ['Gatilho', 'Ação']) {
      if (!groups[t].length) continue;
      html += `<div class="mf-search-section">${t === 'Gatilho' ? 'Gatilhos' : 'Ações'} · ${groups[t].length}</div>`;
      for (const r of groups[t]) {
        const badge = t === 'Gatilho' ? 'gat' : 'acao';
        html += `<a class="mf-search-item" data-i="${idx}" href="${r.href}">
  <span class="mf-search-badge ${badge}">${t}</span>
  <div class="mf-search-text">
    <div class="mf-search-title">${highlight(r.name, q)}${r.en ? ` <span style="opacity:0.5;font-weight:400;">· ${highlight(r.en, q)}</span>` : ''}</div>
    <div class="mf-search-meta"><span>${r.category || ''}</span>${r.tags && r.tags.length ? `<span class="dot">·</span><span>${r.tags.join(' · ')}</span>` : ''}</div>
  </div>
</a>`;
        idx++;
      }
    }
    return html;
  }

  function build() {
    const style = document.createElement('style');
    style.textContent = STYLE;
    document.head.appendChild(style);

    const fab = document.createElement('button');
    fab.className = 'mf-search-fab';
    fab.innerHTML = '<span>🔍</span><span class="label">Buscar</span><kbd>⌘K</kbd>';
    fab.setAttribute('aria-label', 'Abrir busca');
    document.body.appendChild(fab);

    const overlay = document.createElement('div');
    overlay.className = 'mf-search-overlay';
    overlay.innerHTML = `
<div class="mf-search-modal" role="dialog" aria-label="Buscar gatilhos e ações">
  <div class="mf-search-header">
    <span class="mf-search-icon">🔍</span>
    <input class="mf-search-input" placeholder="Buscar gatilho ou ação..." autocomplete="off" spellcheck="false">
    <button class="mf-search-clear" type="button">esc</button>
  </div>
  <div class="mf-search-results"></div>
  <div class="mf-search-footer">
    <span><kbd>↑↓</kbd>navegar</span>
    <span><kbd>↵</kbd>abrir</span>
    <span><kbd>esc</kbd>fechar</span>
  </div>
</div>`;
    document.body.appendChild(overlay);

    const input = overlay.querySelector('.mf-search-input');
    const results = overlay.querySelector('.mf-search-results');
    const clearBtn = overlay.querySelector('.mf-search-clear');
    let active = 0;

    function show() {
      overlay.setAttribute('data-open', '1');
      loadIndex().then(() => {
        update();
        input.focus();
      });
    }
    function hide() {
      overlay.removeAttribute('data-open');
      input.value = '';
      active = 0;
    }
    function update() {
      const q = input.value;
      const r = q.trim() ? search(q) : [];
      results.innerHTML = render(r, q);
      active = 0;
      const items = results.querySelectorAll('.mf-search-item');
      if (items[0]) items[0].classList.add('active');
    }
    function move(delta) {
      const items = results.querySelectorAll('.mf-search-item');
      if (!items.length) return;
      items[active] && items[active].classList.remove('active');
      active = (active + delta + items.length) % items.length;
      items[active].classList.add('active');
      items[active].scrollIntoView({ block: 'nearest' });
    }
    function open() {
      const items = results.querySelectorAll('.mf-search-item');
      if (items[active]) items[active].click();
    }

    fab.addEventListener('click', show);
    clearBtn.addEventListener('click', hide);
    overlay.addEventListener('click', (e) => { if (e.target === overlay) hide(); });
    input.addEventListener('input', update);
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') { hide(); e.preventDefault(); }
      else if (e.key === 'ArrowDown') { move(1); e.preventDefault(); }
      else if (e.key === 'ArrowUp') { move(-1); e.preventDefault(); }
      else if (e.key === 'Enter') { open(); e.preventDefault(); }
    });
    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        overlay.getAttribute('data-open') === '1' ? hide() : show();
      } else if (e.key === '/' && document.activeElement === document.body) {
        e.preventDefault();
        show();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
