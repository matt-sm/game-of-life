import pytest
from game import seed_grid, parse_args


def test_parser():
    with pytest.raises(BaseException):
        parse_args(["-x", "-y"])

    args = parse_args(["-x 10", "-y 20"])
    assert args.x == 10
    assert args.y == 20


def test_seed():
    grid = seed_grid(10, 20)
    assert len(grid) == 20
    assert len(grid[0]) == 10

    grid = seed_grid(5, 2)
    assert len(grid) == 2
    assert len(grid[0]) == 5
