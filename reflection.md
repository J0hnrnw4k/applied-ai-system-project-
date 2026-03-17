# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The first time I ran the game it appeared to work visually but the logic was wrong in several ways. The hints, score, and input
- Bug 1 - Reversed Hints: The secret number was 15 and I guessed 500, but the game told me "Go HIGHER!" when it should have said "Go LOWER." The high/low hint logic is completely backwards.
- Bug 2 - No Input Validation: The game says guess between 1 and 100,  but it accepted guesses of 200, 500, and even 1000 without any error or warning.
- Bug 3 - Negative Score: Expected the score to stop at 0 but it went into negative numbers (-10, -5), which doesn't make sense for a guessing game.

---

## 2. How did you use AI as a teammate?

- Copilot correctly identified that the Higher/Lower hints were swapped in the check_guess function.It explained that "if guess < target, return Lower" was wrong because you actually need to guess higher. I verified this by playing the game and confirming the hints now make sense.

---

## 3. Debugging and testing your fixes

- HI decided a bug was fixed when both the live game showed correct behavior AND pytest passed. I ran python3 -m pytest and all 5 tests passed including test_guess_too_high, test_guess_too_low, and test_score_never_negative. Copilot helped me understand that the tests were failing because check_guess returns a tuple of two values, not just one string.

---

## 4. What did you learn about Streamlit and state?

- Streamlit reruns the entire Python file from top to bottom every  time a user clicks a button or types input. This means variables  reset every time unless you store them in st.session_state. Session state is like a small memory box that survives each rerun, keeping things like the secret number, score, and attempts intact between interactions.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is adding FIXME comments before touching any code, so I always know exactly where the problems are before I start fixing them. Next time I would read the AI's suggested diff more carefully before accepting it, since Copilot used the wrong outcome string that would have broken the score system silently.This project changed how I think about AI generated code because I  now understand that AI can write plausible looking code that is logically wrong in subtle ways, and a human needs to actually test  and verify every suggestion.
