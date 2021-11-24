def switch_score(a):
    if a == 0:
        return "Amour"
    if a == 1:
        return "Quinze"
    if a == 2:
        return "Trente"
    if a == 3:
        return "Quarante"

def score():
    pass

class TennisGame:
    def __init__(self,scored):
        self.scored = scored
