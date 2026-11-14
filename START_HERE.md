# START HERE — 14 November 2026 submission handoff

This archive is a thorough documentation **draft** with honest gaps. It is **not yet a full WRO-compliant repository** because original software, physical evidence, recorded test results, hardware-specific CAD and historical commits were not provided.

## Highest-priority actions today

- [ ] Check **ROBOT_PROFILE.md** against the actual assembled car; replace all `TO VERIFY` values. The National Organizer needs **controllers, building materials, and programming languages**.
- [ ] Check the actual source on the vehicle; copy **all original competition code** and relevant configuration/model files into `src/`, preserving filenames and history wherever possible.
- [ ] Replace `schemes/pinmap.csv` with the true wiring; add an actual electrical schematic. Current SVGs are only conceptual designs.
- [ ] Add clear six-side vehicle photos and team photo.
- [ ] Insert actual two YouTube video links in `video/README.md`, one per challenge with at least 30 s of autonomous driving.
- [ ] Add authentic CAD/STL files where used and the actual parts list / dimensions.
- [ ] Run `python tools/check_submission.py` locally. Address all missing evidence.
- [ ] Create or update a **PUBLIC** GitHub repository, using genuine commit authors/dates; never fake historical milestones.
- [ ] Send GitHub repository URL and robot profile to the Bangladesh National Organizer **by the date communicated in the team's email: 14 Nov 2026**.

## Submission integrity

WRO's original rules specified that first/second/third meaningful commits were required by two months, one month and two weeks before the event. A newly created repo **cannot magically satisfy** October / early November commit requirements. If you have prior authentic project repositories or commits, use their true history as evidence. Do not modify timestamps to simulate compliance. Ask your National Organizer how late/new repository history will be treated.

## Simple upload workflow (replace username and repository)

1. Unzip this package, review the content, and remove any unsupported claims.
2. Copy in your **own actual competition source files** and evidence.
3. `git init && git add . && git commit -m "Document Team Ionizers WRO 2026 engineering"`
4. Create a new empty **public** repository in your GitHub account named `Team-Ionizers-WRO-2026`.
5. `git branch -M main`
6. `git remote add origin https://github.com/YOUR_USERNAME/Team-Ionizers-WRO-2026.git`
7. `git push -u origin main`

If there is an existing original robot repo, **do not reinitialize it** or discard its previous commits. Add these documentation files there and preserve the genuine development history.
