"""Main CLI workflow for the AI customer support assistant."""

from __future__ import annotations

from agents.escalation_agent import check_escalation
from agents.faq_agent import answer_question
from agents.qualification_agent import run_qualification
from agents.summary_agent import generate_summary
from utils.logger import log_conversation


def _print_header(title: str) -> None:
	"""Print a formatted section header."""

	print("\n" + "=" * 60)
	print(title)
	print("=" * 60)


def _get_customer_query() -> str:
	"""Prompt the user for a customer query."""

	return input("Please enter the customer query: ").strip()


def main() -> None:
	"""Run the full assistant workflow."""

	_print_header("AI Customer Support Assistant")

	customer_query = _get_customer_query()
	if not customer_query:
		print("No query provided. Exiting.")
		return

	_print_header("FAQ Response")
	ai_response = answer_question(customer_query)
	print(ai_response)

	_print_header("Escalation Check")
	escalation_result = check_escalation(customer_query, ai_response)
	if escalation_result.get("escalate"):
		print("Escalation detected.")
		print(f"Reason: {escalation_result.get('reason')}")
	else:
		print("No escalation needed.")

	log_conversation(
		user_message=customer_query,
		ai_response=ai_response,
		escalation_reason=escalation_result.get("reason", ""),
	)

	_print_header("Lead Qualification")
	qualification_data = run_qualification()

	chat_history = [
		f"Customer: {customer_query}",
		f"Assistant: {ai_response}",
	]

	_print_header("Conversation Summary")
	summary = generate_summary(
		chat_history=chat_history,
		qualification_data=qualification_data,
		escalation_reason=escalation_result.get("reason", ""),
	)
	print(summary)


if __name__ == "__main__":
	main()
