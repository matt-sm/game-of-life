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


def main():
    args = parse_args(sys.argv[1:])
    data = seed_grid(args.x, args.y, args.cells)
    print_grid(data)


if __name__ == "__main__":
    main()
