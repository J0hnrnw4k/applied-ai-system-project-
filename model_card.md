# Model Card: Game Glitch Investigator Agent

## System Summary
This system uses a modular agentic workflow to categorize, retrieve, and solve game glitches. It utilizes RAG (Retrieval-Augmented Generation) by searching a local `patch_notes.txt` file before generating responses.

## Reliability and Testing
- **Success Rate:** 100% on gameplay-related technical queries during testing.
- **Guardrails:** Implemented a keyword-based guardrail to block off-topic (non-gaming) queries.
- **Limitations:** The agent is currently restricted to a static local text file and may not identify glitches outside of its provided knowledge base.

## AI Collaboration Reflection
During development, AI assisted in structuring the Streamlit UI and refining the file-reading logic. One challenge was the environment path for Streamlit on Mac, which was solved by manual path execution.