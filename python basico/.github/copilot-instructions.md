# Copilot / AI Agent Instructions — Python exercises repo

Purpose
- This repository is a collection of small, standalone Python exercise scripts (learning material). Most files are single-file exercises named in Spanish (e.g. `ejercicio_diccionarios5.py`). Agents should treat changes as lightweight, exercise-focused edits rather than large refactors.

Big picture
- Flat repo layout: no packages or CI. Each `ejercicio_*.py` file is a self-contained script demonstrating a single concept (sintaxis, iterables, diccionarios, etc.). Typical files: `ejercicio_diccionarios5.py`, `ejercicio_iterables_y_listas3.py`, `python_list_dictionary.py`.
- No long-running services or external integrations. There are no tests, build system, or dependency manifests (e.g., requirements.txt) present by default.

How to run and validate
- Run a single exercise locally with the system Python: `python ejercicio_diccionarios5.py` (Windows PowerShell or cmd). Use the Python terminal available in the workspace for quick checks.
- If you modify a script, run that script directly to validate behavior. Avoid introducing third-party dependencies unless the user explicitly approves.

Repository conventions and patterns
- Filenames and identifiers often use Spanish. Preserve the naming style and avoid renaming files without user consent.
- Scripts are small and imperative. Prefer minimal, targeted edits: fix bugs, add small helper functions, or improve clarity.
- Keep code simple and dependency-free. If multiple files become related, propose a small refactor and get confirmation before changing file layout.

Agent workflow and constraints
- Use the repo's `apply_patch` workflow for changes (create focused patches). Provide a short reasoning note with any non-trivial edit.
- After edits, run the modified script to confirm no obvious runtime errors. Share the command you ran and the output if relevant.
- Do not add tests or CI automatically — propose them first.
- Ask before renaming files, adding package structure, or introducing new dependencies.

Examples and pointers
- Fix a bug: patch `ejercicio_diccionarios5.py` and run `python ejercicio_diccionarios5.py` to validate the fix.
- Small enhancement: extract repeated logic into a helper function inside the same file rather than creating new modules.

When to escalate to the user
- Changes that require adding dependencies, creating packages, or renaming files.
- Any behavioral change beyond local correctness (e.g., change exercise intent, change printed outputs expected by a course).

Summary for agents
- Keep edits minimal, runnable, and easy to review. Prefer to run single-file scripts for validation and always ask before broader structural changes.

Files to inspect first
- ejercicio_diccionarios5.py
- ejercicio_iterables_y_listas3.py
- python_list_dictionary.py
- python1.py

If anything in this file is unclear, ask the repo owner which files are canonical examples to follow.
