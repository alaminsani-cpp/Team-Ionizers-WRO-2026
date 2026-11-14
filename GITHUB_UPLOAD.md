# Upload Team Ionizers repository to GitHub

## What this ZIP is

This archive contains the **files of a GitHub repository at the ZIP root**. It is ready to extract, open in VS Code, and commit/push. It is **not** a pre-existing Git repository with historical commits. GitHub does not automatically extract ZIP files; do not upload the ZIP itself as one repository file.

## Before public submission

**Read `START_HERE.md` and `STATUS.md`.** Replace provisional specifications, add your actual robot controller source code (`src/`), wiring and CAD, clear robot/team photographs, and authentic video links. The included documentation describes planned vs. verified items separately and must not be represented as actual proof of operation.

## Windows / VS Code quick instructions

1. Extract the ZIP into a local folder. Open the extracted folder in VS Code with **File > Open Folder**. The `README.md` file should appear at the top level alongside `src`, `docs`, `schemes`, `video`, etc.
2. On GitHub, create a **new public empty repository** named `Team-Ionizers-WRO-2026`. Do not initialize it with a README or license.
3. Open **Terminal > New Terminal** in VS Code. Paste the commands below, changing `YOUR_GITHUB_USERNAME`:

```powershell
git init
git add .
git commit -m "Add Team Ionizers WRO Future Engineers 2026 documentation"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Team-Ionizers-WRO-2026.git
git push -u origin main
```

If you use an **existing authentic robot-development repository**, do not run `git init` there to replace its history: copy the documentation into that original checkout and commit normally. The required WRO history must remain genuine.

### Troubleshooting

- `git is not recognized`: install Git for Windows and restart VS Code.
- `Please tell me who you are`: set `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"` with **your actual identity**.
- `Repository not found`: check the repository exists and `YOUR_GITHUB_USERNAME` was replaced.
- Authentication prompts: use Git Credential Manager or GitHub's supported sign-in; never paste a personal access token into the repository.
- `remote origin already exists`: inspect `git remote -v` and update deliberately with `git remote set-url origin ...` if needed.

To validate missing submission material locally, run:

```powershell
python tools/check_submission.py
```

See `ROBOT_PROFILE.md` for the organizer's required hardware summary.
