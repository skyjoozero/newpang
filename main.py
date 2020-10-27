import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("game")

clock = pygame.time.Clock()

background = pygame.image.load("images\\background.png")
chracter = pygame.image.load("images\\chracter.png")
stage = pygame.image.load("images\\stage.png")
weapon = pygame.image.load("images\\weapon.png")

ball_images = [
    pygame.image.load("images\\ball1.png"),
    pygame.image.load("images\\ball2.png"),
    pygame.image.load("images\\ball3.png"),
    pygame.image.load("images\\ball4.png")]

ball_y_speed = [-6, -4, -3, -2]

ball_start_x = random.randint(0, screen_width - ball1_width)
ball_start_y = random.randint(0, (screen_height / 2) - ball1_height)
balls = []

balls.append({
    "pos_x" : ball_start_x,
    "pos_y" : ball_start_y,
    "ball_image" : ball_images[0]
})

chracter_size = chracter.get_rect().size
chracter_width = chracter_size[0]
chracter_height = chracter_size[1]

stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# ball1_size = ball1.get_rect().size
# ball1_width = ball1_size[0]
# ball1_height = ball1_size[1]

# ball2_size = ball2.get_rect().size
# ball2_width = ball2_size[0]
# ball2_height = ball2_size[1]

# ball3_size = ball3.get_rect().size
# ball3_width = ball3_size[0]
# ball3_height = ball3_size[1]

# ball4_size = ball4.get_rect().size
# ball4_width = ball4_size[0]
# ball4_height = ball4_size[1]

running = True


class ball1:
    def __init__(self, ball_x, ball_y, ball_speed):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_speed = ball_speed
    def move_ball(self):
        self.ball_x += ball_x_speed[0]
        self.ball_y += ball_y_speed[0]

class ball2:
    def __init__(self, ball_x, ball_y, ball_speed:)
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_speed = ball_speed
    def move_ball(self):
        self.ball_x += ball_x_speed[1]
        self.ball_y += ball_y_speed[1]

class ball3:
    def __init__(self, ball_x, ball_y, ball_speed):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_speed = ball_speed
    def move_ball(self):
        self.ball_x += ball_x_speed[2]
        self.ball_y += ball_y_speed[2]

class ball4:
    def __init__(self, ball_x, ball_y, ball_speed):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_speed = ball_speed
    def move_ball(self):
        self.ball_x += ball_x_speed[3]
        self.ball_y += ball_y_speed[3]


to_x = 0
to_y = 0

chracter_speed = 0.3
chracter_x_pos = (screen_width / 2) - (chracter_width / 2)
chracter_y_pos = screen_height - stage_height - chracter_height

weapon_speed = 3
weapons = []

while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= chracter_speed * dt
            elif event.key == pygame.K_RIGHT:
                to_x += chracter_speed * dt
            elif event.key == pygame.K_SPACE:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    chracter_x_pos += to_x

    if chracter_x_pos < 0:
        chracter_x_pos = 0
    if chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos = screen_width - chracter_width

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(chracter, (chracter_x_pos, chracter_y_pos))

    pygame.display.update()



pygame.quit()