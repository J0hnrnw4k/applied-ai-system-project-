from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_score_never_negative():
    # Score should never go below 0
    result = update_score(0, "Too High", 1)
    assert result >= 0

def test_correct_hint_message():
    # Verify hint messages are correct after our fix
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
