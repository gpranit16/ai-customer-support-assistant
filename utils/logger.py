"""Simple conversation logger."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


def _get_logs_path() -> Path:
	"""Return the path to the logs directory."""

	return Path(__file__).resolve().parents[1] / "logs"


def _ensure_logs_folder() -> Path:
	"""Ensure the logs folder exists and return its path."""

	logs_path = _get_logs_path()
	logs_path.mkdir(parents=True, exist_ok=True)
	return logs_path


def _format_entry(
	timestamp: str,
	user_message: str,
	ai_response: str,
	escalation_reason: str,
) -> str:
	"""Format a log entry for storage."""

	return (
		f"Timestamp: {timestamp}\n"
		f"User: {user_message}\n"
		f"AI: {ai_response}\n"
		f"Escalation Reason: {escalation_reason}\n"
		+ "-" * 60
		+ "\n"
	)


def log_conversation(
	user_message: str,
	ai_response: str,
	escalation_reason: str,
) -> None:
	"""Append a conversation log entry to logs/conversations.txt."""

	logs_path = _ensure_logs_folder()
	log_file = logs_path / "conversations.txt"

	timestamp = datetime.now().isoformat(timespec="seconds")
	entry = _format_entry(timestamp, user_message, ai_response, escalation_reason)

	with log_file.open("a", encoding="utf-8") as file:
		file.write(entry)
