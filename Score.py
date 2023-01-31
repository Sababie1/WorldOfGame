from pathlib import Path


def add_score(difficulty):
    POINTS_OF_WINNING = str((difficulty * 3) + 5)
    # The function will read the current score in the scores file,
    # if it fails it will create a new one and will save the current score.
    try:
        with open(Path("Scores.txt"), "a") as score:
            score.write(f"{POINTS_OF_WINNING}, ")
            score.close()
    except FileNotFoundError:
        with open(Path("Scores.txt"), "x") as score:
            score.write(POINTS_OF_WINNING)
            score.close()