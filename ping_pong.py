from pygame import *


'''Необхідні класи'''
mixer.init()

font.init()
#text
font1 = font.SysFont('Italic',30)

score1 =  0
score2 =  0 
s = 'Score  ' + str(score1)+' : ' + str(score2)


#music
mixer.music.load('Happy_Bee.mp3')
mixer.music.play()
#sounds
s1 = mixer.Sound('vctr.mp3')
s2 = mixer.Sound('rckandball.mp3')
 
x = 3
y = 3
# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
 
#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
racket1 = Player('racket.png',0,0,10,30,150)
racket2 = Player('racket2.png',570,350,10,30,150)
ball = GameSprite('ball.png',180,180,10,150,100)
pl1wins = transform.scale(image.load('p1wins.png'), (600,500))
pl2wins = transform.scale(image.load('p2wins.png'), (600,500))
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
def starting():
    global game
    global clock
    global finish
    global s1
    global s2
    global score1
    global score2
    global x1, x2, y1, y2
    global pl1wins
    global pl2wins
    global racket1
    global racket2
    global ball
    global x
    global y
    global s 
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
    
    

        
        
        if finish != True:
            window.fill(back)

        racket1.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        racket2.reset()

        ball.rect.x += x
        ball.rect.y += y

        if ball.rect.y > 450 or ball.rect.y < 0:
            y *= -1

        if sprite.collide_rect(ball,racket1):
            x *= -1
            s2.play()
            
        if sprite.collide_rect(ball,racket2):
            x *= -1
            s2.play()

        if ball.rect.x > 510:
            window.blit(pl1wins,(0,0))
            ball.rect.x = 150
            ball.rect.y = 100
        if ball.rect.x < -1:
            window.blit(pl2wins,(0,0))
            ball.rect.x = 150
            ball.rect.y = 100
            
            

        
        
        text = font1.render(s,True,(0,0,0))
        window.blit(text,(100,100))
        

        display.update()
        clock.tick(60)


