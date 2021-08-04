# https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
import random


def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    # x = random.randint(0, 4)
    # y = random.randint(0, 4)
    # arr[x][y] = "X"

    for row in arr:
        print(" ".join(str(cell)) for cell in row)
        print("")


if __name__ == "__main__":
    minesweeper(5)
