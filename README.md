# Generative AI Programming Portfolio

This repository captures hands-on labs using AI coding assistants (e.g., GitHub Copilot).  
For each lab you will find:
- **code_before** (input/context before asking the LLM)
- **llm_output** (raw suggestions from the LLM / assistant)
- **code_after** (accepted/edited final code)
- A short **notes** section with reflections (what helped, what to improve)
- Optional **recording** (screen capture video) and a **PPT**

## Quick start
```bash
# 1) Create repo and push
git init
git add .
git commit -m "chore: bootstrap portfolio structure"
git branch -M main
# Create remote and push (replace URL)
git remote add origin <YOUR_GIT_REMOTE_URL>
git push -u origin main

# 2) (Optional) Enable Git LFS for large files like videos
git lfs install
git lfs track "*.mp4" "*.mov" "*.mkv" "*.avi"
git add .gitattributes
git commit -m "chore: track videos with Git LFS"
git push
```

## Structure
```
.
├─ docs/
│  ├─ portfolio_overview.md
│  ├─ experiment_template.md
│  └─ presentation_outline.md
├─ labs/
│  └─ class01/
│     ├─ labA_completion/
│     │  ├─ code_before.py
│     │  ├─ prompt_input.md
│     │  ├─ llm_output.md
│     │  ├─ code_after.py
│     │  └─ notes.md
│     └─ labB_nes/
│        ├─ code_before.py
│        ├─ prompt_input.md
│        ├─ llm_output.md
│        ├─ code_after.py
│        └─ notes.md
├─ ppt/
│  └─ template_presentation.md
├─ scripts/
│  └─ save_session.py
├─ .vscode/
│  └─ settings.json
├─ .gitignore
├─ .gitattributes
├─ LICENSE
└─ requirements.txt
```

### Workflow per lab
1. Write **code_before.py** (or paste the minimal context / comments).
2. Trigger the assistant and copy raw suggestions into **llm_output.md** (add timestamp + tool version).
3. Save the final accepted code in **code_after.py**.
4. Add quick reflections in **notes.md** (what worked / what didn’t, pitfalls).
5. (Optional) Record a short video of the flow and put it under `recording/`.
6. Commit with a meaningful message:
   - `feat(labA): initial completion example`
   - `docs(labB): add raw LLM output`
   - `refactor(labB): adopt 3D point and fix logic`
