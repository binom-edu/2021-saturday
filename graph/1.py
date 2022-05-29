import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
    def update(self):
        self.rect.x += 5
        
WIDTH = 360
HEIGHT = 420
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Привет')
clock = pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

gameOn = True
while gameOn:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # обновление
    all_sprites.update()
    # рендеринг
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()