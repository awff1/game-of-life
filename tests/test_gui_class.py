from gui import GameOfLife, SCREEN_SIZE

import pygame
import pytest


def test_initialization():
    game = GameOfLife(30)
    assert game.grid_size == 30
    assert (
        isinstance(game.grid, list)
        and isinstance(game.grid[0], list)
        and isinstance(game.grid[0][0], int)
    )
    assert len(game.grid) == len(game.grid[0]) == 30

    assert isinstance(game.screen, pygame.Surface)
    assert isinstance(game.background, pygame.Surface)


def test_init_grid():
    game = GameOfLife(3)
    assert game.grid == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_make_step():
    game = GameOfLife(3)
    game.make_step()
    assert game.grid == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    game.grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    game.make_step()
    assert game.grid == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


N = 10
G = SCREEN_SIZE[0] // N


@pytest.mark.parametrize(
    "pos, expected",
    [
        ((1, 1), (0, 0)),
        ((G // 2, G // 2), (0, 0)),
        ((G + 1, G + 1), (1, 1)),
        ((G - 1, G + 1), (0, 1)),
        ((G + 1, G - 1), (1, 0)),
        ((2 * G + 1, 2 * G + 1), (2, 2)),
        ((5 * G + 1, 3 * G + 1), (5, 3)),
        ((9 * G + 1, 9 * G + 1), (9, 9)),
    ],
)
def test_cell_clicked(pos, expected):
    game = GameOfLife(N)
    assert game.cell_clicked(pos) == expected


def test_cell_clicked_outside_grid():
    game = GameOfLife(N)

    with pytest.raises(ValueError):
        game.cell_clicked((G, N * G + 1))

    with pytest.raises(ValueError):
        game.cell_clicked((N * G + 1, G))

    with pytest.raises(ValueError):
        game.cell_clicked((-10, 1))
