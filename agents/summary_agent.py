"""Conversation summary generator using LangChain."""

from __future__ import annotations

import json
from typing import Any, Dict, List
from langchain_core.prompts import PromptTemplate

from utils.groq_helper import get_llm


def _build_prompt_template() -> PromptTemplate:
	"""Create the prompt template for structured summaries."""

	template = (
		"You are a helpful assistant that writes concise conversation summaries.\n"
		"Return the summary in the exact format below.\n\n"
		"Format:\n"
		"Customer intent: <text>\n"
		"Key details collected: <text>\n"
		"Escalation status: <text>\n"
		"Recommended next action: <text>\n\n"
		"Chat history:\n{chat_history}\n\n"
		"Qualification data (JSON):\n{qualification_data}\n\n"
		"Escalation reason:\n{escalation_reason}\n\n"
		"Summary:"
	)

	return PromptTemplate(
		input_variables=["chat_history", "qualification_data", "escalation_reason"],
		template=template,
	)


def _stringify_chat_history(chat_history: Any) -> str:
	"""Convert chat history to a readable string."""

	if isinstance(chat_history, str):
		return chat_history.strip()

	if isinstance(chat_history, list):
		return "\n".join(str(item) for item in chat_history).strip()

	return str(chat_history).strip()


def _stringify_qualification_data(qualification_data: Any) -> str:
	"""Convert qualification data to a JSON string when possible."""

	if isinstance(qualification_data, (dict, list)):
		return json.dumps(qualification_data, ensure_ascii=False, indent=2)

	return str(qualification_data).strip()


def generate_summary(
	chat_history: Any,
	qualification_data: Dict[str, Any],
	escalation_reason: str,
) -> str:
	"""Generate a structured conversation summary."""

	prompt = _build_prompt_template()
	llm = get_llm()

	rendered_prompt = prompt.format(
		chat_history=_stringify_chat_history(chat_history),
		qualification_data=_stringify_qualification_data(qualification_data),
		escalation_reason=str(escalation_reason).strip(),
	)

	response = llm.invoke(rendered_prompt)

	if hasattr(response, "content"):
		return response.content.strip()

	return str(response).strip()
