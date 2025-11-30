import random
import pygame
def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen_width = 640
        screen_height = 512
        cell_size = 32
        cols = screen_width // cell_size
        rows = screen_height // cell_size
        molec = 0
        moler = 0
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mole_rect = pygame.Rect(molec * cell_size, moler * cell_size, cell_size, cell_size)
                    if mole_rect.collidepoint(event.pos):
                        newc, newr = molec, moler
                        while newc == molec and newr == moler:
                            newc = random.randrange(cols)
                            newr = random.randrange(rows)
                        molec, moler = newc, newr
            screen.fill("light green")
            for col in range(cols + 1):
                x = col * cell_size
                pygame.draw.line(screen, "dark green", (x, 0), (x, screen_height))
            for row in range(rows + 1):
                y = row * cell_size
                pygame.draw.line(screen, "dark green", (0, y), (screen_width, y))
            mole_pos = (molec * cell_size, moler * cell_size)
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
