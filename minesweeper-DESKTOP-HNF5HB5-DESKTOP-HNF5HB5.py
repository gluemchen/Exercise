# https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
import random


def minesweeper(n):  # Function to create a minesweeper board
    arr = [  # [0][1][2][3][4]*5
        [0 for row in range(n)]  # fill defined range of row with Zero's
        for column in range(n)  # start a column with 5 rows with defined range
    ]

    y = random.randint(0, 4)
    x = random.randint(0, 4)
    arr[y][x] = "X"
    #                         0    1    2    3    4
    if x >= 1 and x <= 3:  # I this case exists    ['0']['0']['0']['0']['0']

        arr[y][x + 1] += 1  # center right          ['0']['0']['X']['-']['0']
        arr[y][x - 1] += 1  # center left           ['0']['-']['X']['0']['0']

    if x == 0:
        arr[y][x + 1] += 1  # center right          ['0']['0']['0']['0']['0']

    if x == 4:
        arr[y][x - 1] += 1  # center left

    if (x >= 1 and x <= 4) and (y >= 1 and y <= 4):  # top left
        arr[y - 1][x - 1] += 1

    if (x >= 0 and x <= 3) and (y >= 1 and y <= 4):  # top right
        arr[y - 1][x + 1] += 1

    if (x >= 0 and x <= 4) and (y >= 1 and y <= 4):  # top center
        arr[y - 1][x] += 1

    if (x >= 0 and x <= 3) and (y >= 0 and y <= 3):  # bottom right
        arr[y + 1][x + 1] += 1

    if (x >= 1 and x <= 4) and (y >= 0 and y <= 3):  # bottom left
        arr[y + 1][x - 1] += 1

    if (x >= 0 and x <= 4) and (y >= 0 and y <= 3):  # bottom center
        arr[y + 1][x] += 1

    for row in arr:
        print(" ".join(str(cell)) for cell in row)  #
        print("")

        print(arr)


if __name__ == "__main__":
    minesweeper(5)
