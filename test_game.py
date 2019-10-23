import pytest
from game import seed_grid, parse_args, print_grid, get_neighbours, live_or_die


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
    grid = seed_grid(4, 4, [(1, 2)])
    print_grid(grid)

    captured = capsys.readouterr()
    assert captured.out == "| | | | |\n| | | | |\n| |L| | |\n| | | | |\n"


def test_neighbours():
    grid = seed_grid(4, 4, [(0, 0), (2, 2)])
    neighbours, live = get_neighbours(grid, (1, 1))
    assert neighbours == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]
    assert live == 2

    grid = seed_grid(4, 4, [])
    neighbours, live = get_neighbours(grid, (3, 2))
    assert neighbours == [
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 3),
        (0, 1),
        (0, 2),
        (0, 3),
    ]
    assert live == 0

    grid = seed_grid(4, 4, [(0, 0), (0, 1)])
    neighbours, live = get_neighbours(grid, (0, 2))
    assert neighbours == [
        (3, 1),
        (3, 2),
        (3, 3),
        (0, 1),
        (0, 3),
        (1, 1),
        (1, 2),
        (1, 3),
    ]
    assert live == 1

    neighbours, _ = get_neighbours(grid, (2, 0))
    assert neighbours == [
        (1, 3),
        (1, 0),
        (1, 1),
        (2, 3),
        (2, 1),
        (3, 3),
        (3, 0),
        (3, 1),
    ]

    neighbours, _ = get_neighbours(grid, (2, 3))
    assert neighbours == [
        (1, 2),
        (1, 3),
        (1, 0),
        (2, 2),
        (2, 0),
        (3, 2),
        (3, 3),
        (3, 0),
    ]


def test_live_or_die():
    assert live_or_die("L", 1) == " "
    assert live_or_die("L", 4) == " "
    assert live_or_die("L", 3) == "L"
    assert live_or_die(" ", 3) == "L"
    assert live_or_die(" ", 2) == " "
