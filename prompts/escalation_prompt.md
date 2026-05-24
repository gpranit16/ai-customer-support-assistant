# 🚨 Escalation Detection Rules

---

## ✅ Overview
This project uses **keyword-based escalation detection** (not an LLM prompt) to flag sensitive, risky, or out-of-scope conversations. The detection logic checks both the **user input** and the **AI response** and escalates if any keyword is found.

---

## 🔍 How Matching Works
- The system normalizes the combined text to lowercase.
- It scans for predefined keywords by category.
- The **first match** determines the escalation reason.
- If no match is found, escalation is not triggered.

---

## 📌 Escalation Categories & Keywords

### 😠 Angry Customer
- angry
- furious
- upset
- mad
- outraged
- frustrated
- annoyed
- terrible service
- worst

### 📝 Complaint
- complaint
- complain
- issue
- problem
- not working
- broken
- unacceptable

### 💳 Refund
- refund
- money back
- chargeback
- return
- cancel and refund

### 💰 Pricing Negotiation
- discount
- lower price
- cheaper
- price match
- negotiate
- special rate
- deal

### 🩺 Medical Question
- medical
- diagnosis
- symptom
- treatment
- prescription
- doctor
- medicine
- health

### 🚫 Out-of-Scope Query
- legal advice
- investment
- tax
- politics
- religion
- surgery
- hair transplant
- programming
- code
- hack

---

## ✅ Escalation Output Format
When a keyword is detected, the system returns:

```json
{
  "escalate": true,
  "reason": "Detected <category> (keyword: '<matched_keyword>')."
}
```

If no keyword is detected:

```json
{
  "escalate": false,
  "reason": "No escalation triggers detected."
}
```

---

## 🧩 Source of Truth
These rules are derived directly from `agents/escalation_agent.py` and match the current implementation.