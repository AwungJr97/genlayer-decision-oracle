# GenLayer Decision Oracle

A small GenLayer application that turns a question plus supporting context into a consensus-backed decision.

## What it does

Users provide a proposition and evidence/context. The `DecisionOracle` Intelligent Contract asks GenLayer validators to evaluate the proposition and returns exactly one of `YES`, `NO`, or `UNCERTAIN`.

## GenLayer integration

- Python Intelligent Contract using `gl.Contract`
- Non-deterministic LLM execution through GenLayer
- Equivalence Principle via `prompt_non_comparative`
- Public write method: `resolve()`
- Public view method: `get_decision()`
- Browser frontend using `genlayer-js`

## Run

1. Deploy `contracts/DecisionOracle.py` to a GenLayer network such as Studio Net.
2. Put the deployed contract address into `frontend/index.html`.
3. Serve the `frontend/` directory with any static HTTP server.
4. Enter a proposition and supporting context.
5. Click **Resolve with GenLayer** and wait for validator consensus.

## Example

Question: `Should this proposal be approved?`

Context: `The proposal meets all listed requirements and includes the requested evidence.`

Expected decision: `YES`

## Safety note

This is a demonstration project. Its decision is an AI-assisted consensus result and should not be treated as professional, legal, financial, or safety-critical advice.
