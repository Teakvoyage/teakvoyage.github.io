import pygame

import random

import math




# define constants

WIDTH = 2000

HEIGHT = 1200

FPS = 60




PLAYER_SPEED = 10

BULLET_SPEED = 10

ENEMY_SPEED = 3

ENEMY_SPAWN_RATE = 99




BLACK = (0, 0, 0)

WHITE = (255, 255, 255)




# initialize pygame and create window

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Shooting Game")

clock = pygame.time.Clock()




# define classes

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))

        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.speed_x = 0

        self.speed_y = 0

   

    def update(self):

        self.rect.x += self.speed_x

        self.rect.y += self.speed_y

   

    def shoot(self, target):

        dx = target[0] - self.rect.centerx

        dy = target[1] - self.rect.centery

        distance = math.sqrt(dx**2 + dy**2)

        bullet_speed_x = BULLET_SPEED * dx / distance

        bullet_speed_y = BULLET_SPEED * dy / distance

        bullet = Bullet(self.rect.centerx, self.rect.centery, bullet_speed_x, bullet_speed_y)

        all_sprites.add(bullet)

        bullets.add(bullet)




class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 30))

        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(WIDTH - self.rect.width)

        self.rect.y = -self.rect.height

        self.speed_x = 0

        self.speed_y = ENEMY_SPEED

   

    def update(self):

        dx = player.rect.centerx - self.rect.centerx

        dy = player.rect.centery - self.rect.centery

        distance = math.sqrt(dx**2 + dy**2)

        self.speed_x = ENEMY_SPEED * dx / distance

        self.speed_y = ENEMY_SPEED * dy / distance

        self.rect.x += self.speed_x

        self.rect.y += self.speed_y

        if self.rect.top > HEIGHT:

            self.kill()




class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, speed_x, speed_y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10))

        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.rect.center = (x, y)

        self.speed_x = speed_x

        self.speed_y = speed_y

   

    def update(self):

        self.rect.x += self.speed_x

        self.rect.y += self.speed_y

        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:

            self.kill()

        hits = pygame.sprite.spritecollide(self, enemies, True)

        for hit in hits:

            global SCORE

            SCORE += 1

            hit.kill()

            self.kill()




# create sprite groups

all_sprites = pygame.sprite.Group()

enemies = pygame.sprite.Group()

bullets = pygame.sprite.Group()




# create player and add to sprite group

player = Player()

all_sprites.add(player)




SCORE = 0

running = True

while running:

    # set the frame rate

    clock.tick(FPS)

    # process input

    # process input

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:

                player.speed_y = -PLAYER_SPEED

            elif event.key == pygame.K_s:

                player.speed_y = PLAYER_SPEED

            elif event.key == pygame.K_a:

                player.speed_x = -PLAYER_SPEED

            elif event.key == pygame.K_d:

                player.speed_x = PLAYER_SPEED

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_w and player.speed_y < 0:

                player.speed_y = 0

            elif event.key == pygame.K_s and player.speed_y > 0:

                player.speed_y = 0

            elif event.key == pygame.K_a and player.speed_x < 0:

                player.speed_x = 0

            elif event.key == pygame.K_d and player.speed_x > 0:

                player.speed_x = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                player.shoot(pygame.mouse.get_pos())




    # spawn enemies

    if random.randrange(ENEMY_SPAWN_RATE) == 0:

        enemy = Enemy()

        all_sprites.add(enemy)

        enemies.add(enemy)




    # update sprites

    all_sprites.update()




    # check for collisions

    hits = pygame.sprite.spritecollide(player, enemies, False)

    if hits:

        running = False




    # draw

    screen.fill(BLACK)

    all_sprites.draw(screen)

    font = pygame.font.Font(None, 30)

    text = font.render("Score: " + str(SCORE), True, WHITE)

    screen.blit(text, (10, 10))




    # update display

    pygame.display.update()
