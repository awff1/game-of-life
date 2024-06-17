import pygame


def run_pygame_showcase():
    pygame.init()
    pygame.display.set_caption("My First Pygame Window")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
    background.fill("black")

    running = True
    while running:  # main game loop
        time_delta = clock.tick(60) * 0.001  # this is time in seconds between frames

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
