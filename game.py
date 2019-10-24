import sys
import argparse
from ast import literal_eval as make_tuple
import time
import copy
import os


def parse_cells_arg(s):
    try:
        return list(make_tuple(s.strip()))
    except:
        raise argparse.ArgumentTypeError("Cells must be 'x,y x,y,...")


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-x", type=int, required=True)
    parser.add_argument("-y", type=int, required=True)
    parser.add_argument(
        "-c", help="Cells", dest="cells", type=parse_cells_arg, required=True, nargs="*"
    )

    return parser.parse_args(args)


def seed_grid(x, y, cells):
    life = [[" " for i in range(y)] for i in range(x)]

    for cell in cells:
        life[cell[0]][cell[1]] = "L"

    return life


def print_grid(life):
    os.system("clear")
    for i in range(len(life)):
        for j in range(len(life[i])):
            print("|" + life[j][i], end="")
        print("|")


def adjust_overlap(coord, count):
    if coord == count:
        coord = 0
    if coord < 0:
        coord = count - 1

    return coord


def get_neighbours(life, x, y):
    live_neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y):
                i = adjust_overlap(i, len(life))
                j = adjust_overlap(j, len(life[0]))

                if life[i][j] == "L":
                    live_neighbours += 1

    return live_neighbours


def live_or_die(status, live_neighbours):
    if status == "L":
        if live_neighbours < 2 or live_neighbours > 3:
            return " "
    else:
        if live_neighbours == 3:
            return "L"

    return status


def generate(life):
    next_gen = copy.deepcopy(life)

    for i in range(len(life)):
        for j in range(len(life[i])):
            live_neighbours = get_neighbours(life, i, j)
            next_gen[i][j] = live_or_die(life[i][j], live_neighbours)

    return next_gen


def main():
    args = parse_args(sys.argv[1:])
    life = seed_grid(args.x, args.y, args.cells)

    starttime = time.time()
    while True:
        print_grid(life)
        life = generate(life)

        time.sleep(1.0 - ((time.time() - starttime) % 1.0))


if __name__ == "__main__":
    main()
