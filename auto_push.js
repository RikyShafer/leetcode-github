const { exec } = require("child_process");

const repoPath = "C:/Users/ריקי שפר/Documents/LeetCode GitHub";

function autoPush() {
  console.log("Checking for changes...");

  exec("git status --porcelain", { cwd: repoPath }, (err, stdout, stderr) => {
    if (err) {
      console.error(`Error: ${err}`);
      return;
    }

    if (stdout.trim().length === 0) {
      console.log("No changes detected. Skipping push.");
      return;
    }

    console.log("Changes detected. Committing and pushing...");

    exec(`git add .`, { cwd: repoPath }, (err) => {
      if (err) {
        console.error(`Error adding files: ${err}`);
        return;
      }

      const commitMessage = `"Auto commit: Update Leetcode solutions - ${new Date().toISOString()}"`;

      exec(`git commit -m ${commitMessage}`, { cwd: repoPath }, (err) => {
        if (err) {
          console.error(`Error committing changes: ${err}`);
          return;
        }

        exec(`git push`, { cwd: repoPath }, (err) => {
          if (err) {
            console.error(`Error pushing changes: ${err}`);
            return;
          }
          console.log("Changes pushed successfully! 🚀");
        });
      });
    });
  });
}

setInterval(autoPush, 5 * 60 * 1000); // כל 5 דקות
