"""Escalation detection using simple keyword-based rules."""

from __future__ import annotations

from typing import Dict, List, Tuple


ESCALATION_CATEGORIES: Dict[str, List[str]] = {
	"angry customer": [
		"angry",
		"furious",
		"upset",
		"mad",
		"outraged",
		"frustrated",
		"annoyed",
		"terrible service",
		"worst",
	],
	"complaint": [
		"complaint",
		"complain",
		"issue",
		"problem",
		"not working",
		"broken",
		"unacceptable",
	],
	"refund": [
		"refund",
		"money back",
		"chargeback",
		"return",
		"cancel and refund",
	],
	"pricing negotiation": [
		"discount",
		"lower price",
		"cheaper",
		"price match",
		"negotiate",
		"special rate",
		"deal",
	],
	"medical question": [
		"medical",
		"diagnosis",
		"symptom",
		"treatment",
		"prescription",
		"doctor",
		"medicine",
		"health",
	],
	"out-of-scope query": [
		"legal advice",
		"investment",
		"tax",
		"politics",
		"religion",
		"surgery",
		"hair transplant",
		"programming",
		"code",
		"hack",
	],
}


def _normalize_text(text: str) -> str:
	"""Normalize text for matching."""

	return (text or "").lower()


def _find_matches(text: str) -> List[Tuple[str, str]]:
	"""Return a list of (category, keyword) matches for the given text."""

	matches: List[Tuple[str, str]] = []
	for category, keywords in ESCALATION_CATEGORIES.items():
		for keyword in keywords:
			if keyword in text:
				matches.append((category, keyword))
	return matches


def _build_reason(matches: List[Tuple[str, str]]) -> str:
	"""Create a readable reason from matches."""

	if not matches:
		return "No escalation triggers detected."

	category, keyword = matches[0]
	return f"Detected {category} (keyword: '{keyword}')."


def check_escalation(user_input: str, ai_response: str) -> dict:
	"""Check if a conversation should be escalated.

	Returns a dictionary:
	{
		"escalate": True/False,
		"reason": "..."
	}
	"""

	combined_text = f"{user_input}\n{ai_response}"
	normalized = _normalize_text(combined_text)

	matches = _find_matches(normalized)
	escalate = len(matches) > 0

	return {
		"escalate": escalate,
		"reason": _build_reason(matches),
	}
