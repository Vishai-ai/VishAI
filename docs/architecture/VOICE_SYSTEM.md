# VishAI Voice System Architecture

## Vision

VishAI should work completely offline and become smarter online.

---

# Voice Pipeline

User
│
▼
Wake Word
│
▼
Speech Recognition
│
▼
NLU Pipeline
│
▼
Brain Engine
│
▼
Service Router
│
▼
Plugins / Skills
│
▼
Response Generator
│
▼
Text To Speech

---

## Components

### Wake Word
Responsible for listening continuously.

Example:
"Hey VishAI"

---

### Speech Recognition

Converts speech to text.

Offline:
- Faster Whisper

Future:
- Cloud Speech

---

### Brain

Already exists.

---

### Service Router

Already exists.

---

### Skills

Already exist.

---

### Text To Speech

Converts text to voice.

Offline:
Piper

---

## Future

Voice Profiles

Noise Cancellation

Streaming Conversation

Multiple Languages

Emotion Detection

Speaker Identification