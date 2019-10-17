import sys
from terminaltables import AsciiTable
import argparse
from ast import literal_eval as make_tuple


def parse_cells_arg(s):
    try:
        return list(make_tuple(s.strip()))
    except:
        raise argparse.ArgumentTypeError("Cells must be x,y")


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-x", type=int, required=True)
    parser.add_argument("-y", type=int, required=True)
    parser.add_argument("-c", help="Cells", dest="cells", type=parse_cells_arg)
    return parser.parse_args(args)


def seed_grid(x_axis, y_axis):
    return [["" for x in range(x_axis)] for y in range(y_axis)]


def print_grid(data):
    table = AsciiTable(data)
    table.inner_heading_row_border = False
    print(table.table)


def main():
    args = parse_args(sys.argv[1:])
    data = seed_grid(args.x, args.y)
    print_grid(data)


if __name__ == "__main__":
    main()
