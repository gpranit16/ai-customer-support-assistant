"""FAQ agent that answers questions using SOP data only."""

from __future__ import annotations

import json
from pathlib import Path


from langchain_core.prompts import PromptTemplate

from utils.groq_helper import get_llm


FALLBACK_MESSAGE = (
	"I don't have information about that. Let me connect you to a human agent."
)


def _get_project_root() -> Path:
	"""Return the project root directory."""

	return Path(__file__).resolve().parents[1]


def _load_sop_data() -> dict:
	"""Load SOP data from sop.json as a dictionary."""

	sop_path = _get_project_root() / "sop.json"
	if not sop_path.exists():
		raise FileNotFoundError(f"SOP file not found at: {sop_path}")

	with sop_path.open("r", encoding="utf-8") as file:
		return json.load(file)


def _build_prompt_template() -> PromptTemplate:
	"""Create a prompt template that restricts answers to SOP data only."""

	template = (
		"You are a helpful FAQ assistant.\n"
		"You MUST answer ONLY using the SOP data provided below.\n"
		"If the answer is not explicitly found in the SOP data, reply exactly:\n"
		f"{FALLBACK_MESSAGE}\n\n"
		"SOP DATA (JSON):\n{safe_sop}\n\n"
		"Question: {question}\n"
		"Answer:"
	)

	return PromptTemplate(
		input_variables=["safe_sop", "question"],
		template=template,
	)


def answer_question(question: str) -> str:
	"""Answer a user question using SOP data only."""

	sop_data = _load_sop_data()
	prompt = _build_prompt_template()

	llm = get_llm()

	rendered_prompt = prompt.format(
		safe_sop=json.dumps(sop_data, ensure_ascii=False, indent=2),
		question=question.strip(),
	)

	response = llm.invoke(rendered_prompt)

	if hasattr(response, "content"):
		return response.content.strip()

	return str(response).strip()
