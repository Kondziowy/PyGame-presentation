#!/Python27/python
import pygame, sys

bgcolor = (255, 255, 255)
colorkey = (120, 195, 128)

pygame.init()

window = pygame.display.set_mode((1024, 768))
screen = pygame.display.get_surface()

image = pygame.image.load("manga-sprites.png")
#image.set_colorkey(colorkey)
x_pos = 300
y_pos = 0

while True:
    screen.fill(bgcolor)
    #screen.blit(image, (x_pos, y_pos))
    #y_pos += 1
    #screen.blit(image, (x_pos, y_pos), (0, 0, 27, 32))
    pygame.display.flip()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit(0)