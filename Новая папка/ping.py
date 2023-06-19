from pygame import * 
from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = "1"

img_back = "background.jpg" 
img_platform1 = "platform_left.png" 
img_platform2 = "platform_right.png" 
img_ball = 'ball.png'

#Экран
win_width = 1000
win_height = 700
display.set_caption('ping-pong')
window = display.set_mode((win_width, win_height))

finish = False
run = True
num_fire = 0
rel_time = False

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, player_speed_x, player_speed_y): 
        sprite.Sprite.__init__(self) 
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))  
class platform_R(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 750: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 965: 
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 135: 
            self.rect.y += self.speed 
class platform_L(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_a] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_d] and self.rect.x < 470/2: 
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height - 135: 
            self.rect.y += self.speed 
class ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #исчезновение 
        if self.rect.x > win_width-50:
            self.speed_x *= -1 
        elif self.rect.x < 5:
            self.speed_x *= -1
        elif self.rect.y > win_height-50:
            self.speed_y *= -1 
        elif self.rect.y < 5:
            self.speed_y *= -1 
         

background = transform.scale(image.load(img_back), (win_width, win_height))
# platform1 = transform.scale(image.load(img_platform1), (70, 20))

#создание героя
platform_l = platform_L(img_platform1, 50, win_height/2, 30, 130, 2, 0, 0)
platform_r = platform_R(img_platform2, 920, win_height/2, 30, 130, 2, 0, 0)
ball = ball(img_ball, 475,win_height/2,50,50,0,1,1)
while run:
    for e in event.get():
        if e.type == QUIT :
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    # fire_sound.play()
                    ship.fire()
                elif num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

                    
    if finish != True:
        window.blit(background, (0,0))
        platform_l.reset()
        platform_l.update()

        platform_r.reset()
        platform_r.update()

        ball.reset()
        ball.update()
    display.update()

    time.delay(2)