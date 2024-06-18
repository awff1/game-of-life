from collections import Counter

from source import get_empty_grid, get_random_grid


def test_get_empty_grid():
    grid = get_empty_grid(3, 3)
    assert grid == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    grid = get_empty_grid(2, 2)
    assert grid == [[0, 0], [0, 0]]

    grid = get_empty_grid(2, 3)
    assert grid == [[0, 0, 0], [0, 0, 0]]


def test_get_random_grid_dimensions():
    grid = get_random_grid(6, 6)
    assert len(grid) == 6
    assert len(grid[0]) == 6

    grid = get_random_grid(2, 10)
    assert len(grid) == 2
    assert len(grid[0]) == 10


def test_get_random_grid_randomness():
    # get a big enough random grid
    grid = get_random_grid(120, 80)
    counter = Counter([cell for row in grid for cell in row])

    # check that only 0s and 1s are present
    assert counter.keys() == {0, 1}
    # check that the number of cells is correct
    assert counter[0] + counter[1] == 120 * 80
    # check that the distribution of 0s and 1s is roughly equal
    assert abs(counter[0] - counter[1]) / (120 * 80) < 0.1
