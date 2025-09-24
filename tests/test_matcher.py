from models.job_matcher import calculate_match_score

def test_score_range():
    score = calculate_match_score("Python developer", "Looking for Python engineer")
    assert 0 <= score <= 100
