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


def seed_grid(x_axis, y_axis, cells):
    grid = [[" " for y in range(y_axis)] for x in range(x_axis)]
    for cell in cells:
        grid[cell[0]][cell[1]] = "L"

    return grid


def print_grid(data):
    os.system("clear")
    for y, row in enumerate(data):
        for x, _ in enumerate(row):
            print("|" + data[x][y], end="")
        print("|")


def adjust_overlap(coord, count):
    if coord == count:
        coord = 0
    if coord < 0:
        coord = count - 1

    return coord


def get_neighbours(data, cell):
    neighbours = []
    live_neighbours = 0
    for x in range(cell[0] - 1, cell[0] + 2):
        for y in range(cell[1] - 1, cell[1] + 2):
            if not (x == cell[0] and y == cell[1]):
                x = adjust_overlap(x, len(data))
                y = adjust_overlap(y, len(data[0]))

                neighbours.append((x, y))
                if data[x][y] == "L":
                    live_neighbours += 1

    return neighbours, live_neighbours


def live_or_die(status, live_neighbours):
    if status == "L":
        if live_neighbours < 2 or live_neighbours > 3:
            return " "
    else:
        if live_neighbours == 3:
            return "L"

    return status


def generate(data):
    next_gen = copy.deepcopy(data)
    for x, row in enumerate(data):
        for y, status in enumerate(row):
            cell = (x, y)
            _, live_neighbours = get_neighbours(data, cell)
            next_gen[x][y] = live_or_die(status, live_neighbours)

    return next_gen


def main():
    args = parse_args(sys.argv[1:])
    data = seed_grid(args.x, args.y, args.cells)

    starttime = time.time()
    while True:
        print_grid(data)
        data = generate(data)

        time.sleep(1.0 - ((time.time() - starttime) % 1.0))


if __name__ == "__main__":
    main()
