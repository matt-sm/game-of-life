import pytest
from game import seed_grid, parse_args, print_grid


def test_parser():
    with pytest.raises(BaseException):
        parse_args(["-x", "-y", "-c"])

    args = parse_args(["-x 10", "-y 20", "-c (1,1),(2,2),(5,4)"])
    assert args.x == 10
    assert args.y == 20
    assert args.cells == [[(1, 1), (2, 2), (5, 4)]]


def test_seed():
    grid = seed_grid(10, 20, [(0, 0), (9, 19)])
    assert len(grid) == 10
    assert len(grid[0]) == 20
    assert grid[0][0] == "L"
    assert grid[9][19] == "L"
    assert grid[1][19] == " "


def test_print(capsys):
    grid = seed_grid(2, 2, [(0, 0)])
    print_grid(grid)

    captured = capsys.readouterr()
    assert captured.out == "|L| |\n| | |\n"
