🎮 Game Glitch Investigator: Professional Applied AI System
🚨 The Situation
Originally, I was given an AI-generated "Number Guessing Game" built with Streamlit that was unplayable and full of bugs. I successfully repaired the game mechanics and have now evolved it into a professional AI tool that uses Agentic Workflows and Retrieval-Augmented Generation (RAG) to investigate game glitches.


🚀 Phase 2: Applied AI System (Project 4 Upgrade)
In this version, I've integrated a custom AI Agent that helps developers triage bugs by leveraging local documentation.


🧠 Agentic Workflow & RAG
The system follows a structured 3-step process to ensure accurate and trustworthy results:


*  Categorization: The AI classifies reports into Gameplay or Technical categories.   
*  Retrieval (RAG): The system searches a local knowledge base (patch_notes.txt) to find historical fixes.   
*  Reasoning: The AI combines the retrieved facts with the user's report to provide a verifiable solution.   
🛡️ Reliability & Guardrails
To ensure the system is production-ready, I implemented:
*  Topic Guardrails: A keyword-based filter prevents the AI from answering off-topic queries, such as recipes or general chat.   
*  Process Transparency: The terminal outputs real-time [AGENT] logs, showing the AI's step-by-step thinking for every investigation.   
📊 System Architecture
Figure 1: The system pipeline starting with a Guardrail Check before entering the 3-step reasoning chain.
🛠️ Setup & Usage
* Install dependencies: pip install streamlit
* Launch System: python3 -m streamlit run app.py
*  Use the Investigator: Scroll to Section 2 in the app to report a glitch.   
🕵️‍♂️ Technical Debugging (Phase 1)
I stabilized the core game engine by fixing several critical bugs:
* Reversed Logic: Fixed check_guess() so hints (Higher/Lower) are actually correct.
* Data Integrity: Removed a bug where the secret number was being converted to a string.
* Scoring: Repaired update_score() so points never drop below 0.
* Difficulty Scaling: Adjusted Hard mode to a 1-200 range for proper scaling.
Tests Passed:
✅ test_winning_guess | ✅ test_guess_too_high | ✅ test_guess_too_low
✅ test_score_never_negative | ✅ test_correct_hint_message
📺 Final Demo & Walkthrough
* Professional Presentation (4 min): [Watch Link](https://www.loom.com/share/b0b032267a9f4b64b413a597c9ac6b94)
* Live Demonstration (2 min): [Watch Link](https://www.loom.com/share/b0b032267a9f4b64b413a597c9ac6b94)
In these videos, I demonstrate a successful game run, an AI glitch investigation using local data, and the guardrail system blocking an off-topic question.


📈 Reflection
This project demonstrates my ability to take an unreliable prototype and turn it into a verifiable, reliable AI system. As a student focused on Technical Product Management, I prioritized grounding and reliability—ensuring the AI agent provides solutions based on a local knowledge base rather than hallucinating responses.


