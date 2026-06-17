# AH CompSci GitHub + Codespaces Starter

This repo is a short warm-up before you begin the main SDD project.

The goal is for you to practise:
- opening a repository in GitHub Codespaces
- editing files in VS Code
- running Python in the terminal
- making commits with clear messages
- pushing a branch and opening a pull request

## What You Will Build

You will complete 3 tiny tasks:
1. `tasks/01_hello.py`: fix a name and print output.
2. `tasks/02_calculator.py`: complete simple functions.
3. `tasks/03_words.py`: process a list of words.

Each file has `TODO` comments showing what to change.

## Classroom Workflow (Your Instructions)

1. Open this repo on GitHub.
2. Click **Fork** and create a copy in your own GitHub account.
3. Open your forked repo (not the original class repo).
4. In your fork, click **Code** -> **Codespaces** -> **Create codespace on main**.
5. Wait for VS Code to open in browser.
6. Open the terminal (`Ctrl+` `).
7. Create a new branch in Source Control, e.g. `student-firstname-starter`.
8. Complete Task 1:

- Run `python3 tasks/01_hello.py`.
- Edit `tasks/01_hello.py` to complete the TODO.
- Re-run `python3 tasks/01_hello.py` and check output.
- Commit with a clear message, e.g. `Complete task 1 hello`.
- Push your branch to your fork on GitHub.
- Open your repo on github.com and review the changed file and latest commit.

9. Complete Task 2:

- Run `python3 tasks/02_calculator.py`.
- Edit `tasks/02_calculator.py` to complete all TODOs.
- Re-run `python3 tasks/02_calculator.py` and check output.
- Commit with a clear message, e.g. `Complete task 2 calculator`.
- Push your branch to your fork on GitHub.
- Open your repo on github.com and review the changed file and latest commit.

10. Complete Task 3:

- Run `python3 tasks/03_words.py`.
- Edit `tasks/03_words.py` to complete all TODOs.
- Re-run `python3 tasks/03_words.py` and check output.
- Commit with a clear message, e.g. `Complete task 3 words`.
- Push your branch to your fork on GitHub.
- Open your repo on github.com and review the changed file and latest commit.

11. Open a Pull Request from your branch into `main`.
12. Check the Pull Request "Files changed" tab to review all commits together.

### Helpful Git Commands (Terminal)

If you prefer terminal commands for commit and push:

```bash
git add tasks/01_hello.py
git commit -m "Complete task 1 hello"
git push
```

Repeat this for each task file using the matching commit message.

## Success Checklist

Before you commit, tick each item:

- [ ] I created my own branch before starting.
- [ ] I forked the repo to my own GitHub account first.
- [ ] I completed and ran Task 1, then committed and pushed.
- [ ] I checked github.com and reviewed my Task 1 commit.
- [ ] I completed and ran Task 2, then committed and pushed.
- [ ] I checked github.com and reviewed my Task 2 commit.
- [ ] I completed and ran Task 3, then committed and pushed.
- [ ] I checked github.com and reviewed my Task 3 commit.
- [ ] I opened one Pull Request into `main`.

## Extension Tasks (Optional)

- Add one new word challenge to `tasks/03_words.py`.
- Improve output formatting using f-strings.
- Ask a partner to review your PR and leave one comment.

## Teacher Notes

Suggested sequence for one short lesson:
1. Demonstrate Codespaces launch and first run.
2. Students complete task files independently/in pairs.
3. Students commit + push + create PR.
4. Teacher reviews PRs and gives quick feedback on commit messages and code style.

If you want stricter checking later, add unit tests in a follow-up lesson.