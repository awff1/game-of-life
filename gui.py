import pygame
from pygame import Color
from utils import visualize_grid

from source import Grid, step, get_empty_grid, get_random_grid


SCREEN_SIZE = (800, 800)
assert SCREEN_SIZE[0] == SCREEN_SIZE[1], "Only square screens are supported"

BACKGROUND_COLOR = Color("#303030")
ALIVE_CELL_COLOR = Color("white")


class GameOfLife:
    def __init__(self, grid_size: int):
        self.grid_size = grid_size

        # initialize the grid with empty cells
        self.grid: Grid = get_empty_grid(grid_size, grid_size)
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
        self.background: pygame.Surface = pygame.Surface(SCREEN_SIZE)

        self.render_grid_lines()

        self.running = True
        self.paused = False  # for running the simulation steps manually

    def make_step(self) -> None:
        """Make one step of the Game of Life simulation.
        Overwrite the current grid with the next one."""
        self.grid = step(self.grid)

    def cell_clicked(self, pos: tuple[int, int]) -> tuple[int, int]:
        """Return cell coordinates by mouse click position.
        Raise ValueError if the click is outside of the grid."""

        if 0 <= pos[0] <= SCREEN_SIZE[0] and 0 <= pos[1] <= SCREEN_SIZE[0]:
            cell_size = SCREEN_SIZE[1] / self.grid_size
            return (int(pos[0] // cell_size), int(pos[1] // cell_size))
        else:
            raise ValueError

    def render_grid_lines(self) -> None:
        """Draw grid lines on the background surface
        such that we don't need to draw them every frame.

        Hint: there are `self.grid_size - 1` lines in each direction."""
        cell_size = SCREEN_SIZE[1] // self.grid_size  # TODO: was `/`, changed to `//`
        for i in range(0, SCREEN_SIZE[1], cell_size):
            pygame.draw.line(self.background, "white", (i, 0), (i, SCREEN_SIZE[1]))
        for i in range(0, SCREEN_SIZE[1], cell_size):
            pygame.draw.line(self.background, "white", (0, i), (SCREEN_SIZE[1], i))

    def render_grid(self) -> None:
        """Draw all cells on the screen surface
        using the current grid state."""
        pygame.draw.rect(self.screen, ALIVE_CELL_COLOR, pygame.Rect(100,150,500,100))

    def process_click(self, event: pygame.event.Event) -> None:
        """Process mouse click event."""
        pos = pygame.mouse.get_pos()
        cell_click = self.cell_clicked(pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.grid[cell_click[1]][cell_click[0]] = 1 - self.grid[cell_click[1]][cell_click[0]]
            print(f"Mouse button pressed at {pos}", self.cell_clicked(pos))

    def process_keydown(self, event: pygame.event.Event) -> None:
        """Process keydown event."""
        if event.key == pygame.K_SPACE:
            self.make_step()
        elif event.key == pygame.K_d:
            visualize_grid(self.grid)

    def process_event(self, event: pygame.event.Event) -> None:
        """Process one event in the event loop.

        Logically splits the event handling into separate methods."""
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            self.process_keydown(event)
        elif event.type in {pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL}:
            self.process_click(event)

    def run(self):
        """Run the main game loop."""
        pygame.init()
        pygame.display.set_caption("Game of Life")

        clock = pygame.time.Clock()
        while self.running:
            _time_delta = clock.tick(60) * 0.001

            for event in pygame.event.get():
                self.process_event(event)

            self.screen.blit(self.background, (0, 0))
            self.render_grid()
            pygame.display.flip()
        pygame.quit()


def run_pygame_showcase():
    pygame.init()
    pygame.display.set_caption("My First Pygame Window")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 800))
    background = pygame.Surface((800, 800))
    background.fill("black")

    running = True
    while running:  # main game loop
        _time_delta = clock.tick(60) * 0.001  # this is time in seconds between frames

        # do all simulation updates here
        # ...

        for event in pygame.event.get():
            # handle events
            if event.type == pygame.QUIT:
                # if the 'X' button is clicked
                running = False
                break
            # handle all other events

            # -- keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                elif event.key == pygame.K_SPACE:
                    print("Space key pressed")

            # -- mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"Mouse button pressed at {pos}")

        # render all graphics here
        # ...

        screen.blit(background, (0, 0))

        pygame.display.flip()
    pygame.quit()
