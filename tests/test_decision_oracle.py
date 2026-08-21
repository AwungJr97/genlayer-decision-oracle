def test_end_to_end_request_persists_inputs_and_decision(direct_vm, direct_deploy):
    """Submit browser-style inputs, resolve consensus, and verify persisted state."""
    direct_vm.mock_llm(r"Question:.*Context:.*", "YES")

    contract = direct_deploy("contracts/DecisionOracle.py")
    question = "Should this proposal be approved?"
    context = "The proposal satisfies every listed requirement and includes the requested evidence."

    contract.resolve(question, context)

    request = contract.get_request()
    assert request["question"] == question
    assert request["context"] == context
    assert request["decision"] in {"YES", "NO", "UNCERTAIN"}
    assert request["decision"] == "YES"
    assert contract.get_decision() == "YES"


def test_invalid_model_output_is_safe_uncertain(direct_vm, direct_deploy):
    direct_vm.mock_llm(r"Question:.*Context:.*", "MAYBE, because the evidence is incomplete")

    contract = direct_deploy("contracts/DecisionOracle.py")
    contract.resolve("Is the proposition supported?", "The evidence is ambiguous.")

    assert contract.get_decision() == "UNCERTAIN"
