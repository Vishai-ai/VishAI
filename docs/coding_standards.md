# VishAI Coding Standards

## General Rules

- One class per file whenever possible.
- Every class must have a docstring.
- Every function must have a clear purpose.
- Use snake_case for variables and functions.
- Use PascalCase for classes.
- Avoid duplicate code.
- Write small reusable modules.
- Every new feature must have a test.
- Every completed feature must be committed to Git.

---

## Folder Responsibilities

ai/
Handles AI providers.

brain/
Decision making.

planner/
Breaks goals into steps.

router/
Selects execution path.

tasks/
Executes planned tasks.

automation/
Controls Windows and applications.

memory/
Stores long-term memory.

conversation/
Stores conversation history.

voice/
Speech input/output.

vision/
Image understanding.

plugins/
Future extensions.

---

## Development Workflow

Architecture

↓

Code

↓

Test

↓

Git Commit

↓

Review

↓

Next Feature