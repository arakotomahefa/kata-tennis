class TennisGame:

    def __init__(self):
        self.current_score = "Love"

    def leading_player_scored(self):
        if self.current_score == "Love":
            self.current_score ="Fifteen"
        elif self.current_score == "Fifteen":
            self.current_score = "Thirty"
        elif self.current_score =="Thirty":
            self.current_score ="Forty"

    def score(self):
        return self.current_score
