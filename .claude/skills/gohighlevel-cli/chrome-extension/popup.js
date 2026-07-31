// Captura o refresh token E a API key do Firebase da sessão logada do GHL.
// A API key fica embutida na chave do IndexedDB: firebase:authUser:<API_KEY>:[DEFAULT]
// Os dois valores são necessários para o CLI renovar o ID token sozinho.

let creds = null;

const grabBtn = document.getElementById("grabBtn");
const copyBtn = document.getElementById("copyBtn");
const status = document.getElementById("status");
const preview = document.getElementById("preview");

function setStatus(msg, type) {
  status.textContent = msg;
  status.className = type;
}

function envBlock(c) {
  return `GHL_FIREBASE_REFRESH_TOKEN=${c.refreshToken}\nGHL_FIREBASE_API_KEY=${c.apiKey || ""}`;
}

grabBtn.addEventListener("click", async () => {
  grabBtn.disabled = true;
  setStatus("Lendo IndexedDB...", "info");

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    if (!tab?.url?.startsWith("http")) {
      setStatus("Abra uma página do GHL logada primeiro.", "error");
      grabBtn.disabled = false;
      return;
    }

    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: extractToken,
      world: "MAIN",
    });

    const result = results?.[0]?.result;

    if (result?.refreshToken) {
      creds = result;
      const semKey = !result.apiKey;
      setStatus(
        semKey
          ? "Token capturado, mas a API key não foi encontrada — preencha manualmente."
          : "Token e API key capturados!",
        semKey ? "info" : "success"
      );
      preview.textContent = envBlock(result).replace(
        result.refreshToken,
        result.refreshToken.substring(0, 24) + "..." + result.refreshToken.slice(-12)
      );
      preview.style.display = "block";
      copyBtn.disabled = false;
    } else if (result?.error) {
      setStatus("Erro: " + result.error, "error");
    } else {
      setStatus("Nenhum token encontrado. Confirme que você está logado no GHL.", "error");
    }
  } catch (err) {
    setStatus("Erro: " + err.message, "error");
  }

  grabBtn.disabled = false;
});

copyBtn.addEventListener("click", async () => {
  if (!creds) return;
  const text = envBlock(creds);
  try {
    await navigator.clipboard.writeText(text);
  } catch {
    const ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    ta.remove();
  }
  setStatus("Copiado! Cole as duas linhas no seu .env.", "success");
});

// Roda no contexto da PÁGINA (não da extensão)
function extractToken() {
  return new Promise((resolve) => {
    try {
      const request = indexedDB.open("firebaseLocalStorageDb");

      request.onerror = () => resolve({ error: "Não foi possível abrir o IndexedDB" });

      request.onsuccess = (event) => {
        const db = event.target.result;

        if (!db.objectStoreNames.contains("firebaseLocalStorage")) {
          resolve({ error: "Store firebaseLocalStorage não encontrada" });
          return;
        }

        const tx = db.transaction("firebaseLocalStorage", "readonly");
        const store = tx.objectStore("firebaseLocalStorage");
        const getAll = store.getAll();
        const getKeys = store.getAllKeys();

        let entries = null;
        let keys = null;

        const finish = () => {
          if (entries === null || keys === null) return;

          for (let i = 0; i < entries.length; i++) {
            const entry = entries[i];
            const val = entry?.value || entry;
            const stm = val?.stsTokenManager;
            if (!stm?.refreshToken) continue;

            // A API key está na chave do registro ou no próprio entry
            const rawKey = String(entry?.fbase_key || keys[i] || "");
            const match = rawKey.match(/firebase:authUser:([^:]+):/);
            const apiKey = (match && match[1]) || val?.apiKey || "";

            resolve({
              refreshToken: stm.refreshToken,
              apiKey,
              accessToken: stm.accessToken,
              expirationTime: stm.expirationTime,
              uid: val.uid,
            });
            return;
          }
          resolve({ error: "Nenhum stsTokenManager.refreshToken encontrado" });
        };

        getAll.onsuccess = () => { entries = getAll.result; finish(); };
        getKeys.onsuccess = () => { keys = getKeys.result; finish(); };
        getAll.onerror = () => resolve({ error: "Falha ao ler os registros" });
        getKeys.onerror = () => resolve({ error: "Falha ao ler as chaves" });
      };
    } catch (err) {
      resolve({ error: err.message });
    }
  });
}
