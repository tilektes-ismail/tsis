import json

def save_score(score):
    data = {"score": score}
    with open("leaderboard.json", "w") as f:
        json.dump(data, f)
