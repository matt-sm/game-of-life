from terminaltables import AsciiTable
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-x", type=int, required=True)
    parser.add_argument("-y", type=int, required=True)

    args = parser.parse_args()

    table_data = []
    for _ in range(0, args.y):
        table_data.append([""] * args.x)

    table = AsciiTable(table_data)
    table.inner_heading_row_border = False
    print(table.table)


if __name__ == "__main__":
    main()
