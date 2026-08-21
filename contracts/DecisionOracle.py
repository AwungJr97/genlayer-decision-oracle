# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
from genlayer.gl import *


class DecisionOracle(gl.Contract):
    """Decentralized decision oracle powered by GenLayer validator consensus."""

    question: str
    context: str
    decision: str

    def __init__(self, question: str = "", context: str = ""):
        self.question = question
        self.context = context
        self.decision = "PENDING"

    @gl.public.write
    def resolve(self, question: str, context: str):
        # Persist the exact browser inputs for this request before invoking consensus.
        self.question = question
        self.context = context
        self.decision = "PENDING"

        def get_input() -> str:
            return f"Question: {self.question}\nContext: {self.context}"

        result = gl.eq_principle.prompt_non_comparative(
            get_input,
            task=(
                "Act as a neutral decision oracle. Classify the proposition using "
                "the supplied question and context. Return exactly one token: YES, "
                "NO, or UNCERTAIN."
            ),
            criteria=(
                "The output must be exactly YES, NO, or UNCERTAIN. Return YES only "
                "when the context clearly supports the proposition, NO only when "
                "the context clearly contradicts it, and UNCERTAIN when the context "
                "is insufficient or ambiguous."
            ),
        )

        # Normalize defensively so contract state always contains an allowed decision.
        normalized = str(result).strip().upper()
        if normalized not in ("YES", "NO", "UNCERTAIN"):
            normalized = "UNCERTAIN"
        self.decision = normalized

    @gl.public.view
    def get_decision(self) -> str:
        return self.decision

    @gl.public.view
    def get_request(self) -> dict:
        return {
            "question": self.question,
            "context": self.context,
            "decision": self.decision,
        }
