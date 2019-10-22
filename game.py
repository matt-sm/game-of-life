import sys
import argparse
from ast import literal_eval as make_tuple


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
    grid = [[" " for x in range(y_axis)] for y in range(x_axis)]

    for cell in cells:
        grid[cell[0]][cell[1]] = "L"

    return grid


def print_grid(data):
    for x in data:
        for y in x:
            print("|" + y, end="")
        print("|")


def get_neighbours(data, cell):
    neighbours = []
    for x in range(cell[0] - 1, cell[0] + 2):
        for y in range(cell[1] - 1, cell[1] + 2):
            if x == cell[0] and y == cell[1]:
                continue
            if x == len(data):
                x = 0
            if x < 0:
                x = len(data) - 1
            if y < 0:
                y = len(data[0]) - 1
            if y == len(data[0]):
                y = 0

            neighbours.append((x, y))

    return neighbours


def main():
    args = parse_args(sys.argv[1:])
    data = seed_grid(args.x, args.y, args.cells)
    print_grid(data)


if __name__ == "__main__":
    main()
