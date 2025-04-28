chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "download") {
      chrome.downloads.download({
        url: message.url,
        filename: "LeetCode GitHub/" + message.filename,
        conflictAction: "overwrite"
      });
    }
  });
  