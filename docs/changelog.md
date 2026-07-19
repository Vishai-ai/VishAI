# VishAI Changelog

## v0.1 Foundation

### Completed
- Git & GitHub setup
- Professional project structure
- Boot system
- Logger
- Kernel
- Memory Manager
- Knowledge Manager
- Task Manager
- Brain Engine v0.1
- Initial testing setup

### Status
Stable


## v0.2

- Added Service Registry
- Added Application Bootstrap
- Started Dependency Injection Architecture



# VishAI System Contract

## Purpose

This document defines the permanent architecture rules of VishAI.

These rules should never be broken unless the architecture is intentionally redesigned.

---

# Rule 1

BrainEngine is the central coordinator.

It never contains business logic.

---

# Rule 2

Business logic belongs inside services.

---

# Rule 3

Managers directly control modules.

Examples

MemoryManager

AIManager

BrowserManager

VoiceManager

---

# Rule 4

Services communicate with Managers.

Brain communicates with Services.

Brain never communicates directly with Managers.

---

# Rule 5

Every module must have exactly one responsibility.

---

# Rule 6

Every module must have its own test.

---

# Rule 7

No circular imports.

---

# Rule 8

All shared services must be registered inside Service Registry.

---

# Rule 9

Modules communicate using EventBus whenever possible.

---

# Rule 10

Launcher is the only entry point of VishAI.

Brain should never start itself.

---

# Folder Ownership

brain/

Decision Making

memory/

Memory

knowledge/

Knowledge

automation/

Desktop Control

browser/

Browser Control

voice/

Voice

vision/

Vision

services/

Communication Layer

core/

Infrastructure

events/

Messaging

planner/

Planning

router/

Routing

tools/

Utilities

docs/

Documentation

tests/

Testing

---

End of Contract