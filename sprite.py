#!/Python27/python
import pygame
import sys
pygame.init()
window = pygame.display.set_mode((1024, 768))
screen = pygame.display.get_surface()
bgcolor = (120, 195, 128)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load("m1.png"))
        self.images.append(pygame.image.load("m2.png"))
        self.images.append(pygame.image.load("m3.png"))
        self.image = self.images[0]
        self.frame = 0
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 1
        self.frame = (self.frame + 1) % len(self.images)
        self.image = self.images[self.frame]

player = Player()
active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)
while True:
    screen.fill(bgcolor)
    active_sprite_list.update()
    active_sprite_list.draw(screen)
    pygame.display.flip()
    event = pygame.event.poll()
    clock.tick(30)
    if event.type == pygame.QUIT:
        sys.exit(0)