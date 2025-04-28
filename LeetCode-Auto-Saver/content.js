function extractCode() {
    const codeEditor = document.querySelector('.view-lines');
    if (!codeEditor) return null;
  
    const lines = codeEditor.querySelectorAll('div');
    let code = "";
  
    lines.forEach(line => {
      code += line.innerText + "\n";
    });
  
    return code;
  }
  
  function saveCodeToFile(code, fileName) {
    const blob = new Blob([code], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
  
    chrome.runtime.sendMessage({ action: "download", url: url, filename: fileName });
  }
  
  function checkAndSave() {
    const successAlert = document.querySelector('.text-success');
    if (successAlert && successAlert.innerText.includes("Accepted")) {
      const code = extractCode();
      if (code) {
        const problemName = document.querySelector('div[class*="css-v3d350"]').innerText || "solution";
        const safeFileName = problemName.replace(/\s+/g, '_').replace(/[^a-zA-Z0-9_]/g, '') + ".txt";
  
        saveCodeToFile(code, safeFileName);
      }
    }
  }
  
  // כל כמה שניות בודק אם יש הצלחה
  setInterval(checkAndSave, 5000);
  