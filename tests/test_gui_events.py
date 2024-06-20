from gui import GameOfLife, SCREEN_SIZE

import pygame
import pytest

N = 10
G = SCREEN_SIZE[0] // N


def test_process_click_1():
    click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(1, G + 1))
    game = GameOfLife(N)
    assert game.grid[0][1] == 0
    game.process_click(click_event)
    assert game.grid[0][1] == 1
    game.process_click(click_event)
    assert game.grid[0][1] == 0


def test_process_click_2():
    click_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, button=1, pos=(9 * G + 1, 9 * G + 1)
    )
    game = GameOfLife(N)
    assert game.grid[9][9] == 0
    game.process_click(click_event)
    assert game.grid[9][9] == 1
    game.process_click(click_event)
    assert game.grid[9][9] == 0


def test_process_click_3():
    click_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, button=1, pos=(-1, -1)
    )
    game = GameOfLife(N)
    with pytest.raises(ValueError):
        game.process_click(click_event)
    
    click_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, button=1, pos=(N * G + 1, G)
    )
    with pytest.raises(ValueError):
        game.process_click(click_event)

