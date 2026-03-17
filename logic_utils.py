def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Hard difficulty corrected to 1-200 to be actually harder
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an int guess."""
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message)."""
    # FIX: Higher/Lower messages were swapped, now corrected
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score. Score never goes below 0."""
    # FIX: Score no longer goes negative or gains points for wrong guesses
    if outcome == "Win":
        points = max(100 - 10 * attempt_number, 10)
        return current_score + points
    return max(current_score - 5, 0)
