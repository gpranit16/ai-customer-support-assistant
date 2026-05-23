# 🤖 AI Customer Support Assistant

---

## 📘 Overview
A professional, CLI-based AI customer support assistant built with **Python**, **LangChain**, and the **Groq API**. It grounds every response in your Standard Operating Procedures (SOP) to minimize hallucinations, automatically detects escalation signals, qualifies leads, summarizes conversations, and logs every interaction.

---

## ✨ Features
- **SOP-grounded FAQ agent** to answer only what’s in your playbook
- **Escalation detection** for sensitive or out-of-scope requests
- **Lead qualification** via guided CLI questions
- **Conversation summary generator** for clean handoffs
- **Conversation logging** to `logs/conversations.txt`
- **Modular multi-agent architecture** for easy extension

---

## 🧭 Architecture & Workflow
```
User Query → FAQ Agent → AI Response → Escalation Check → Logging
                                            ↓
                                      Lead Qualification
                                            ↓
                                    Conversation Summary
```

**How it works:**
1. User submits a customer query via CLI.
2. FAQ agent answers strictly from `sop.json`.
3. Escalation agent detects risk signals and flags issues.
4. All interactions are logged.
5. Qualification questions collect business details.
6. Summary agent compiles a professional final summary.

---

## 📸 Demo Screenshots
Below is a real CLI run from this project that demonstrates the full flow (FAQ response → escalation check → qualification → summary). The screenshot in this submission matches the output format shown here:

```text
AI Customer Support Assistant
============================================================
Please enter the customer query: What are Botox prices?

FAQ Response
============================================================
Botox starts from £200.

Escalation Check
============================================================
No escalation needed.

Lead Qualification
============================================================
Let's get to know your business better.
What type of business do you run? salon
How many team members do you have? 10
Which tools are you currently using? excel

Conversation Summary
============================================================
Customer intent: Inquire about Botox prices.
Key details collected: Botox prices start from £200.
Escalation status: No escalation triggers detected.
Recommended next action: Provide additional information about Botox services.
```

### FAQ + Conversation Summary Workflow
![FAQ and Summary Demo](assests/faq_summmary.png)

*Shows the SOP-grounded FAQ response alongside the structured conversation summary output for a complete end-to-end demo.*

### Conversation Logging System
![Logs Demo](assests/logs.png)

*Shows the persisted conversation entry inside `logs/conversations.txt`, including timestamp, user input, AI response, and escalation reason.*

---

## 🧠 AI Concepts Used
This project demonstrates practical, production-style AI patterns that are easy to understand and extend:
- **Prompt Engineering** to drive structured, reliable outputs
- **SOP Grounding** to ensure answers remain policy-aligned
- **Hallucination Prevention** via strict SOP-only responses
- **Multi-Agent Workflow** for separation of concerns and clarity
- **Escalation Detection** to flag sensitive or risky requests
- **Lead Qualification** to capture business context
- **LLM-based Summarization** for clean, professional handoffs
- **Modular AI Architecture** to simplify future expansion

---

## 🧰 Tech Stack
- **Python 3**
- **LangChain**
- **Groq API (ChatGroq)**
- **python-dotenv**

---

## 🗂️ Folder Structure
```
ai-support-agent/
├─ agents/
│  ├─ escalation_agent.py
│  ├─ faq_agent.py
│  ├─ qualification_agent.py
│  └─ summary_agent.py
├─ utils/
│  ├─ groq_helper.py
│  └─ logger.py
├─ logs/
│  └─ conversations.txt
├─ sop.json
├─ app.py
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Installation
1. **Clone or download** this repository.
2. **Create a virtual environment** (optional but recommended).
3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables
Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL_NAME=your_groq_model_name
```

---

## ▶️ How to Run
```bash
python app.py
```

---

## 🧪 Example Test Cases
**Case 1 — SOP-based answer**
- **Input:** “What are your support hours?”
- **Expected:** Answer is pulled directly from `sop.json`.

**Case 2 — Out-of-scope request**
- **Input:** “Do you provide hair transplant surgery?”
- **Expected:** Escalation triggered with reason “Detected out-of-scope query ...”

**Case 3 — Refund request**
- **Input:** “I want a refund.”
- **Expected:** Escalation triggered with reason “Detected refund ...”

---

## 🛡️ Hallucination Prevention
The FAQ agent is **explicitly constrained** to answer using **only SOP data**. If the answer is missing, it returns:

> “I don't have information about that. Let me connect you to a human agent.”

This ensures predictable, policy-safe responses suitable for real support workflows.

---

## 🚨 Escalation Handling
Escalation logic uses keyword-based detection for:
- Angry or frustrated customers
- Complaints
- Refund requests
- Pricing negotiation
- Medical questions
- Out-of-scope service requests

When detected, the system logs the reason and flags the conversation for human review.

---

## 🚀 Future Improvements
- Add sentiment scoring for better escalation accuracy
- Connect to a CRM for automated ticket creation
- Support multi-turn chat history in FAQ grounding
- Add unit tests and CI workflow
- Add a web UI (optional)

---

## 👤 Author
**Gupta** — AI Support Assistant Project

---

If you’d like a web-based version, analytics dashboard, or additional agents (billing, onboarding, compliance), I can help you extend this system.
