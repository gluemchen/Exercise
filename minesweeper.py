# https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
import random


def minesweeper(grid, bomb):  # Function to create a minesweeper board
    arr = [  # [0][1][2][3][4]*5
        [0 for row in range(grid)]  # fill defined range of row with Zero's
        for column in range(grid)  # start a column with 5 rows with defined range
    ]

    for num in range(bomb):
        y = random.randint(0, grid - 1)
        x = random.randint(0, grid - 1)
        arr[y][x] = "X"

        #                           0    1    2    3    4
        if (x >= grid - 5 and x <= grid - 1) and (
            y >= grid - 5 and y <= grid
        ):  # I this case exists    0.['?']['?']['?']['?']['0']
            if arr[y][x + 1] != "X":
                arr[y][x + 1] += 1  # center right          0.['X']['X']['X']['X']['-']

        if (x >= grid - 4 and x <= grid) and (
            y >= grid - 5 and y <= grid
        ):  # I this case exists    0.['0']['?']['?']['?']['?']
            if arr[y][x - 1] != "X":
                arr[y][x - 1] += 1  # center left           0.['-']['X']['X']['X']['X']

        # if x == 0:
        #     arr[y][x + 1] += 1                         # center right            ['0']['0']['0']['0']['0']

        # if x == 4:
        #     arr[y][x - 1] += 1                         # center left

        if (x >= grid - 4 and x <= grid - 1) and (
            y >= grid - 4 and y <= grid - 1
        ):  # top left
            if arr[y - 1][x - 1] != "X":  # skip if X is already placed
                arr[y - 1][x - 1] += 1

        if (x >= grid - 4 and x <= grid - 1) and (
            y >= grid - 3 and y <= grid - 1
        ):  # top right
            if arr[y - 1][x + 1] != "X":  # skip if X is already placed
                arr[y - 1][x + 1] += 1

        if (x >= grid - 4 and x <= grid - 1) and (
            y >= grid - 3 and y <= grid - 1
        ):  # top center
            if arr[y - 1][x] != "X":  # skip if X is already placed
                arr[y - 1][x] += 1

        if (x >= grid - 4 and x <= grid - 2) and (
            y >= grid - 4 and y <= grid - 2
        ):  # bottom right
            if arr[y + 1][x + 1] != "X":  # skip if X is already placed
                arr[y + 1][x + 1] += 1

        if (x >= grid - 3 and x <= grid) and (
            y >= grid - 4 and y <= grid - 1
        ):  # bottom left
            if arr[y + 1][x - 1] != "X":  # skip if X is already placed
                arr[y + 1][x - 1] += 1

        if (x >= grid - 4 and x <= grid - 1) and (
            y >= grid - 4 and y <= grid - 2
        ):  # bottom center
            if arr[y + 1][x] != "X":  # skip if X is already placed
                arr[y + 1][x] += 1

    for row in arr:
        print(" ".join(str(cell) for cell in row))  #
        print("")


if __name__ == "__main__":
    minesweeper(5, 3)  # Beginner
    minesweeper(6, 8)  # Intermediate
    minesweeper(8, 20)  # Expert
