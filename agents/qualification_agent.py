"""Lead qualification module using simple CLI prompts."""

from __future__ import annotations

from typing import Dict, List, Tuple


QUESTIONS: List[Tuple[str, str]] = [
	("business_type", "What type of business do you run?"),
	("team_size", "How many team members do you have?"),
	("current_tools", "Which tools are you currently using?"),
]


def _ask_question(prompt: str) -> str:
	"""Ask a single question via CLI and return the user's answer."""

	return input(f"{prompt} ").strip()


def _collect_answers() -> Dict[str, str]:
	"""Ask all qualification questions and return a dictionary of answers."""

	answers: Dict[str, str] = {}
	for key, prompt in QUESTIONS:
		answers[key] = _ask_question(prompt)
	return answers


def run_qualification() -> Dict[str, str]:
	"""Run the qualification flow and return collected answers."""

	print("Let's get to know your business better.")
	return _collect_answers()
