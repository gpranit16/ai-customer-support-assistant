"""Groq LangChain helper.

Loads environment variables from .env and provides a reusable LLM factory.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


def _load_env() -> None:
	"""Load environment variables from a .env file."""

	load_dotenv()


def _get_required_env_var(name: str) -> str:
	"""Get a required environment variable or raise a clear error."""

	value = os.getenv(name)
	if not value:
		raise ValueError(
			f"Missing required environment variable: {name}. "
			"Please set it in your .env file."
		)
	return value


def get_llm() -> ChatGroq:
	"""Create and return a ChatGroq LLM instance."""

	_load_env()

	api_key = _get_required_env_var("GROQ_API_KEY")
	model_name = _get_required_env_var("GROQ_MODEL_NAME")

	llm = ChatGroq(
		api_key=api_key,
		model=model_name,
		temperature=0.3,
	)

	return llm
