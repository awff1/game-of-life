from gui import GameOfLife, SCREEN_SIZE

import pygame
import pytest

N = 10
G = SCREEN_SIZE[0] // N


def test_process_click_1():
    pos = 1, G + 1
    click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos)
    pygame.mouse.get_pos = lambda: pos
    game = GameOfLife(N)
    assert game.grid[1][0] == 0
    game.process_click(click_event)
    assert game.grid[1][0] == 1
    game.process_click(click_event)
    assert game.grid[1][0] == 0


def test_process_click_2():
    pos = 9 * G + 1, 9 * G + 1
    click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos)
    pygame.mouse.get_pos = lambda: pos
    game = GameOfLife(N)
    assert game.grid[9][9] == 0
    game.process_click(click_event)
    assert game.grid[9][9] == 1
    game.process_click(click_event)
    assert game.grid[9][9] == 0


def test_process_click_3():
    pos = -1, -1
    click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos)
    pygame.mouse.get_pos = lambda: pos
    game = GameOfLife(N)
    with pytest.raises(ValueError):
        game.process_click(click_event)

    pos = N * G + 1, G
    click_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, button=1, pos=pos
    )
    pygame.mouse.get_pos = lambda: pos
    with pytest.raises(ValueError):
        game.process_click(click_event)


def test_process_keydown():
    space_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    game = GameOfLife(N)
    assert game.grid == [[0] * N for _ in range(N)]
    game.grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    game.process_keydown(space_event)
    assert game.grid == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    