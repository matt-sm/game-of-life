from game import seed_grid


def test_seed():
    grid = seed_grid(10, 20)
    assert len(grid) == 20
    assert len(grid[0]) == 10

    grid = seed_grid(5, 2)
    assert len(grid) == 2
    assert len(grid[0]) == 5
