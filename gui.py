import pygame
from pygame import Color
from utils import visualize_grid

from source import Grid, step, get_empty_grid, get_random_grid


SCREEN_SIZE = (800, 800)
assert SCREEN_SIZE[0] == SCREEN_SIZE[1], "Only square screens are supported"

BACKGROUND_COLOR = Color("#303030")
ALIVE_CELL_COLOR = Color("white")
MARGIN = 1


class GameOfLife:
    def __init__(self, grid_size: int):
        self.grid_size = grid_size

        # initialize the grid with empty cells
        self.grid: Grid = get_empty_grid(grid_size, grid_size)
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
        self.background: pygame.Surface = pygame.Surface(SCREEN_SIZE)
        self.cell_size = SCREEN_SIZE[1] // self.grid_size
        self.render_grid_lines()

        self.running = True
        self.paused = True  # for running the simulation steps manually

    def make_step(self) -> None:
        """Make one step of the Game of Life simulation.
        Overwrite the current grid with the next one."""
        self.grid = step(self.grid)

    def cell_clicked(self, pos: tuple[int, int]) -> tuple[int, int]:
        """Return cell coordinates by mouse click position.
        Raise ValueError if the click is outside of the grid."""

        if 0 <= pos[0] <= SCREEN_SIZE[0] and 0 <= pos[1] <= SCREEN_SIZE[0]:
            return (int(pos[0] // self.cell_size), int(pos[1] // self.cell_size))
        else:
            raise ValueError

    def render_grid_lines(self) -> None:
        """Draw grid lines on the background surface
        such that we don't need to draw them every frame.

        Hint: there are `self.grid_size - 1` lines in each direction."""
        for i in range(0, SCREEN_SIZE[1], self.cell_size):
            pygame.draw.line(self.background, "white", (i, 0), (i, SCREEN_SIZE[1]))
        for i in range(0, SCREEN_SIZE[1], self.cell_size):
            pygame.draw.line(self.background, "white", (0, i), (SCREEN_SIZE[1], i))

    def render_grid(self) -> None:
        """Draw all cells on the screen surface
        using the current grid state."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(
                        self.screen,
                        ALIVE_CELL_COLOR,
                        pygame.Rect(
                            (j * self.cell_size + MARGIN, i * self.cell_size + MARGIN),
                            (self.cell_size - MARGIN * 2, self.cell_size - MARGIN * 2),
                        ),
                    )

    def process_click(self, event: pygame.event.Event) -> None:
        """Process mouse click event."""
        pos = pygame.mouse.get_pos()
        cell_click = self.cell_clicked(pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.grid[cell_click[1]][cell_click[0]] = (
                1 - self.grid[cell_click[1]][cell_click[0]]
            )
            print(f"Mouse button pressed at {pos}", self.cell_clicked(pos))
    
    def clear_grid(self) -> None:
        self.grid = get_empty_grid(self.grid_size, self.grid_size)

    def process_keydown(self, event: pygame.event.Event) -> None:
        """Process keydown event."""
        if event.key == pygame.K_SPACE:
            self.make_step()
        elif event.key == pygame.K_d:
            visualize_grid(self.grid)
        elif event.key == pygame.K_c:
            self.clear_grid()
        elif event.key == pygame.K_r:
            self.grid = get_random_grid(self.grid_size, self.grid_size)
        elif event.key == pygame.K_p:
            self.paused = not self.paused

    def process_event(self, event: pygame.event.Event) -> None:
        """Process one event in the event loop.

        Logically splits the event handling into separate methods."""
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            self.process_keydown(event)
        elif event.type in {
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEWHEEL,
        }:
            self.process_click(event)

    def run(self):
        """Run the main game loop."""
        pygame.init()
        pygame.display.set_caption("Game of Life")

        clock = pygame.time.Clock()
        timer = 0
        while self.running:
            time_delta = clock.tick(60) * 0.001
            timer += time_delta
            if not self.paused and timer > 0.2:
                self.make_step()
                timer = 0
            
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
