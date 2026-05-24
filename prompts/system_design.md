# 🧭 System Design (Current Workflow)

---

## ✅ Overview
This document describes the **actual workflow** implemented in `app.py`. The system runs in a **CLI environment** and orchestrates multiple agents in sequence.

---

## 🧩 Workflow Steps (As Implemented)
1. **Ask for customer query** via CLI input.
2. **FAQ Agent** answers using SOP-grounded prompt logic.
3. **Print AI response** to the console.
4. **Escalation Agent** checks the user input and AI response for keyword triggers.
5. **If escalation is detected**, print escalation message and reason.
6. **Log the conversation** to `logs/conversations.txt`.
7. **Lead Qualification Agent** asks three business questions and collects answers.
8. **Store chat history** as a list of formatted messages.
9. **Summary Agent** generates a structured summary using chat history, qualification data, and escalation reason.
10. **Print the final summary** to the console.

---

## 🔁 Workflow Diagram (Text)
```
Customer Query
   ↓
FAQ Agent (SOP-grounded)
   ↓
AI Response
   ↓
Escalation Check
   ↓
Conversation Logging
   ↓
Lead Qualification
   ↓
Summary Generation
   ↓
Final Summary Output
```

---

## 🧷 Related Source Files
- `app.py` — Orchestrates the full CLI workflow
- `agents/faq_agent.py` — SOP-grounded FAQ responses
- `agents/escalation_agent.py` — Keyword-based escalation detection
- `agents/qualification_agent.py` — Lead qualification prompts
- `agents/summary_agent.py` — Structured summary generation

---

## 📌 Notes
- This is a **modular, multi-agent** workflow intended to be beginner-friendly.
- Each step is intentionally simple and easy to extend.
- Prompts are documented in `/prompts` to reflect real, current logic.