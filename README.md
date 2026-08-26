# PythonQuest

**Learn Python by building and playing a retro-inspired RPG.**

PythonQuest is an open-source educational game designed to teach Python fundamentals through interactive coding challenges. Instead of simply reading tutorials, players progress through chapters, solve programming puzzles, and master core concepts one step at a time.

---

## Vision

The goal of PythonQuest is simple:

> **Learn Python through practice, not just theory.**

Every chapter focuses on a fundamental programming concept, and every boss represents a real coding challenge that validates the knowledge acquired.

---

## Current Status

 **In Development - Version 1.0**

Planned features:

- Dialogue-based progression
- Retro-style static scenes
- Interactive Python exercises
- Chapter progression system
- Simple save/load functionality

---

## Project Structure

```text
PythonQuest/
├── assets/
├── docs/
├── src/
│   ├── main.py
│   │
│   ├── states/
│   │   ├── menu.py
│   │   ├── chapter.py
│   │   └── story.py
│   │
│   ├── systems/
│   │   ├── dialogue.py
│   │   └── typewriter.py
│   │
│   └── content/
│       ├── story_data.py
│       ├── chapter_data.py
│       └── dialogue_data.py
│
├── README.md
├── requirements.txt
└── CHANGELOG.md
```
```markdown
states/   → Game states and their display logic
systems/  → Reusable game systems
content/  → Game content and data
main.py   → Main game loop and orchestration

---

## Creator

Created by **Anthony Allard** as part of a personal journey into software development and artificial intelligence.

---

## License

This project is released under the **MIT License**.