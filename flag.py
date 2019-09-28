import pygame

pygame.init()

size = (400, 600)
screen = pygame.display.set_mode(size)


def draw():
    pygame.draw.rect(screen, pygame.Color('brown'), [(0, 0), (20, 600)], 0)
    pygame.draw.rect(screen, pygame.Color('blue'), [(20, 150), (380, 150)], 0)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()


pygame.quit()