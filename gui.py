import pygame

from source import Grid, step, get_empty_grid, get_random_grid


SCREEN_SIZE = (800, 800)
assert SCREEN_SIZE[0] == SCREEN_SIZE[1], "Only square screens are supported"

BACKGROUND_COLOR = "#303030"
ALIVE_CELL_COLOR = "white"


class GameOfLife:
    def __init__(self, grid_size: int):
        self.grid_size = grid_size

        self.grid: Grid = ...
        self.screen: pygame.Surface = ...
        self.background: pygame.Surface = ...

        self.render_grid_lines()

        self.running = True
        self.paused = False  # for running the simulation steps manually

    def make_step(self) -> None:
        """Make one step of the Game of Life simulation.
        Overwrite the current grid with the next one."""
        ...

    def cell_clicked(self, pos: tuple[int, int]) -> tuple[int, int]:
        """Return cell coordinates by mouse click position.

        Raise ValueError if the click is outside of the grid."""
        ...

    def render_grid_lines(self) -> None:
        """Draw grid lines on the background surface
        such that we don't need to draw them every frame.

        Hint: there are `self.grid_size - 1` lines in each direction."""
        ...

    def render_grid(self) -> None:
        """Draw all cells on the screen surface
        using the current grid state."""
        ...

    def process_click(self, event: pygame.event.Event) -> None:
        """Process mouse click event."""
        ...

    def process_keydown(self, event: pygame.event.Event) -> None:
        """Process keydown event."""
        ...

    def process_event(self, event: pygame.event.Event) -> None:
        """Process one event in the event loop.

        Logically splits the event handling into separate methods."""
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            self.process_keydown(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.process_click(event)

    def run(self):
        """Run the main game loop."""
        pygame.init()
        pygame.display.set_caption("Game of Life")
        ...


def run_pygame_showcase():
    pygame.init()
    pygame.display.set_caption("My First Pygame Window")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
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
