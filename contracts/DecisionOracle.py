# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
from genlayer.gl import *


class DecisionOracle(gl.Contract):
    """Decentralized decision oracle powered by GenLayer validator consensus."""

    question: str
    context: str
    decision: str

    def __init__(self, question: str, context: str):
        self.question = question
        self.context = context
        self.decision = "PENDING"

    @gl.public.write
    def resolve(self):
        prompt = f"""
You are a neutral decision oracle.

Question:
{self.question}

Context:
{self.context}

Return exactly one of:
YES
NO
UNCERTAIN

Choose YES only when the context clearly supports the proposition.
Choose NO only when the context clearly contradicts it.
Choose UNCERTAIN when the available context is insufficient or ambiguous.
"""
        result = gl.eq_principle.prompt_non_comparative(prompt)
        self.decision = result.strip().upper()

    @gl.public.view
    def get_decision(self) -> str:
        return self.decision
