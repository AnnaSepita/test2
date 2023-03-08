from pygame import*
from random import*
font.init() #підключать шрифт
font = font.SysFont("Arial", 30)
lost = 0 #підрахунок пропущених
score = 0
win_widht = 700
win_height = 500
cootdinates = [90, 170, 250, 320, 699, 174, 625, 378, 583]
clock = time.Clock()
window = display.set_mode((win_widht, win_height))
display.set_caption('Майнер')
background = transform.scale(image.load('bgg.jpg'),(win_widht, win_height))
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 100:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 450:
            lost +=1
            self.rect.y = 0
            self.rect.x = choice(cootdinates)
player = Player("cyborg.png",400,370,100,100,7)
bitcoins = sprite.Group()
for i in range(2):
    bitcoin = Enemy('1515.png',choice(cootdinates), -40, 40, 40, randint(1,2))
    bitcoins.add(bitcoin)
start = True
while start:
    window.blit(background,(0,0))#фон
    for e in event.get():
        if e.type == QUIT:
            start = False
    collision = sprite.spritecollide(player,bitcoins, True)
    for c in collision:
        score += 1
        bitcoin = Enemy('1515.png', choice(cootdinates), -40, 40, 40, randint(1,2))
        bitcoins.add(bitcoin)
    text1 = font.render("Пропущено : " + str(lost), True, ("#594daa"))

    window.blit(text1,(10, 60))
    text2 = font.render("Зловлено : " + str(score), True, ("#594daa"))

    window.blit(text2, (10, 20))

    bitcoins.draw(window)
    bitcoins.update()
    player.reset()
    player.update()
    if score >=10:
        start = False
        win = transform.scale(image.load("win.jpg"),(win_widht, win_height))
        window.blit(win, (0, 0))
        display.update()
        time.wait(3000)
    if lost >= 4:
        start = False
        win = transform.scale(image.load("lose.png"), (win_widht, win_height))
        window.blit(win, (0, 0))
        display.update()
        time.wait(3000)
    clock.tick(90)
    display.update()






