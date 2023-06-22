from pygame import * 
from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = "1"

font.init()
font2 = font.Font(None, 36)

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
count_l = 0
count_r = 0
rel_time = False

kick_ball = 0

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
        global count_l 
        global count_r
        #исчезновение 
        if self.rect.x > win_width-51:
            count_l += 1
            self.rect.x = 750
            self.rect.y = 350
            kick_ball = 0
            self.speed_x = -1 
        elif self.rect.x < 5:
            count_r += 1
            self.rect.x = 500/2
            self.rect.y = 350
            kick_ball = 0
            self.speed_x = +1
        elif self.rect.y > win_height-51:
            self.speed_y *= -1 
        elif self.rect.y < 5:
            self.speed_y *= -1 
    def kick(self):
        if self.rect.x < 500:
            self.rect.x += 5 
        elif self.rect.x > 500:
            self.rect.x -=5 
        self.speed_x *= -1
    def speed_kick(self):
        if self.speed_x < 0:
            self.speed_x -= 1
        elif self.speed_x > 0:
            self.speed_x += 1



background = transform.scale(image.load(img_back), (win_width, win_height))
# platform1 = transform.scale(image.load(img_platform1), (70, 20))

#создание героя
platform_l = platform_L(img_platform1, 0, win_height/2, 30, 130, 2, 0, 0)
platform_r = platform_R(img_platform2, 970, win_height/2, 30, 130, 2, 0, 0)
ball = ball(img_ball, 475,win_height/2,50,50,0,1,1)
while run:
    for e in event.get():
        if e.type == QUIT :
            run = False

    if finish != True:
        if sprite.collide_rect(ball, platform_l) or sprite.collide_rect(ball, platform_r):            
                ball.kick()
                kick_ball += 1
        if kick_ball > 3:
            ball.speed_kick()
            kick_ball = 0

        

        window.blit(background, (0,0))

        text = font2.render('Счет: '+str(count_l)+":"+str(count_r),1,(255,255,255))
        window.blit(text,(10,20))

        platform_l.reset()
        platform_l.update()

        platform_r.reset()
        platform_r.update()

        ball.reset()
        ball.update()
    display.update()

    time.delay(2)
