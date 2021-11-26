from tennis import TennisGame


def test_running_score_starts_at_0():
    tennis_game = TennisGame()

    assert tennis_game.score() == "Love"


def test_running_score_goes_0_to_15_when_player_scores_a_point():
    tennis_game = TennisGame()

    tennis_game.leading_player_scored()

    assert tennis_game.score() == "Fifteen"

def test_running_score_goes_0_to_30_when_player_scores_two_points():
     tennis_game = TennisGame()

     tennis_game.leading_player_scored()
     tennis_game.leading_player_scored()

     assert tennis_game.score() == "Thirty"


def test_running_score_goes_0_to_40_when_player_scores_two_points():
    tennis_game = TennisGame()

    tennis_game.leading_player_scored()
    tennis_game.leading_player_scored()
    tennis_game.leading_player_scored()

    assert tennis_game.score() == "Forty"