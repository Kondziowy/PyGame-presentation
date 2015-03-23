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
        self.change_x = 0
        self.change_y = 1

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.frame = self.rect.x % len(self.images)
        self.image = self.images[self.frame]


player = Player()
active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)
while True:
    clock.tick(30)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit(0)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.change_x = -10
        if event.key == pygame.K_RIGHT:
            player.change_x = 10
    if event.type == pygame.KEYUP:
            player.change_x = 0
    screen.fill(bgcolor)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0,35, 500, 35), 0)
    active_sprite_list.update()
    active_sprite_list.draw(screen)
    pygame.display.flip()
