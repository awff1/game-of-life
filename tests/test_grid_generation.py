from source import get_empty_grid, get_random_grid


def test_get_empty_grid():
    grid = get_empty_grid(3, 3)
    assert grid == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    grid = get_empty_grid(2, 2)
    assert grid == [[0, 0], [0, 0]]

    grid = get_empty_grid(2, 3)
    assert grid == [[0, 0, 0], [0, 0, 0]]


def test_get_random_grid():
    grid = get_random_grid(3, 3)
    assert len(grid) == 3
    assert len(grid[0]) == 3

    grid = get_random_grid(2, 2)
    assert len(grid) == 2
    assert len(grid[0]) == 2
