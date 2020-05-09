import pygame
from pygame import mixer
import time
import random
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Battle")
run=True
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
mixer.music.load('background.wav')
mixer.music.play(-1)

ship=pygame.image.load('space-invaders.png')
plrx=370
plry=500
plrxc=0

enemyimg=[]
enemyx=[]
enemyy=[]
enex_ch=[]
eney_ch=[]
numofene=6
a=1
enemyimg1=pygame.image.load('alien.png')

for i in range(numofene):
    enemyimg.append(pygame.image.load('alien (1).png'))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(50,150))
    enex_ch.append(a)
    eney_ch.append(40)

bckgrnd=pygame.image.load('backgnd.jpg')

bullet=pygame.image.load('bullet.png')
bulx=plrx
buly=500
bulych=0
bul_state='ready'

bomb=pygame.image.load('bomb.png')
box=50
boy=50
boch=2
bost='ready'
# score=0

score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
gameovr=pygame.font.Font('freesansbold.ttf',72)

def show_scores(x,y):
    score = font.render("Score : " + str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def gameovrtxt():
    gmetxt=gameovr.render("GAME OVER",True,(255,255,255))
    screen.blit(gmetxt,(180, 240))
g=0
def player(plrx,plry):
    screen.blit(ship,(plrx,plry))


def enemy(enemy1,plrx,plry):
    screen.blit(enemy1,(plrx,plry))

def enemybomb(x,y):
    global bost
    bost='fire'
    screen.blit(bomb, (x,y))

def fire(x,y):
    global bul_state
    bul_state='fire'
    screen.blit(bullet,(x+16,y+10))


blast=pygame.image.load('flame.png')

#level
starttime=pygame.time.get_ticks()
cre=pygame.font.Font('freesansbold.ttf',32)




#game loop
while run:




    screen.fill((0, 0, 0))
    screen.blit(bckgrnd, (0, 0))
    secs = (pygame.time.get_ticks() - starttime) // 1000
    if secs <=2:
        screen.blit(cre.render("Created By Gourav R Dutta", True, (255, 255, 255)), (200, 250))
        # pygame.time.wait(2000)
    else:
        if secs > 2 and secs > 20 and secs <= 30:
            a = 2
        elif secs > 30:
            a = 2
            # if boy == enemyy[5]:
            bost = 'fire'

            if bost == 'fire':
                enemybomb(box, boy)
                boy += boch
            if boy > 500:
                boy = enemyy[5]
                box = enemyx[5]
                bost = 'ready'

        elif secs > 50:
            a = 5
        print(secs)
        events = pygame.event.get()
        if g==0:


            for event in events:
                if event.type == pygame.QUIT:
                    run=False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        plrxc-=5
                        if bul_state == 'ready':
                            bulx=plrx


                    if event.key == pygame.K_SPACE:
                        bul_state='fire'
                        bulletsound=mixer.Sound('laser.wav')
                        bulletsound.play()

                        bulych=4
                    if event.key == pygame.K_RIGHT:
                        plrxc+=5
                        if bul_state == 'ready':
                            bulx=plrx


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        plrxc=0
                        if bul_state == 'ready':
                            bulx=plrx





            if bul_state=='fire':
                fire(bulx,buly)
                buly -= bulych
            if buly < 0:
                buly = 500
                bulych = 0
                bulx = plrx
                bul_state = 'ready'

            for i in range(numofene):
                enemyx[i] += (enex_ch[i])
                if enemyx[i] < 0:
                    enex_ch[i]=a
                    enemyy[i] = enemyy[i]+ eney_ch[i]
                elif enemyx[i] >= 736:
                    enex_ch[i]=-a
                    enemyy[i] = enemyy[i]+ eney_ch[i]
                if i!=5:
                    enemy(enemyimg[i],enemyx[i], enemyy[i])
                else:
                    if bost == 'ready':
                        boy=enemyy[i]
                        box=enemyx[i]

                    enemy(enemyimg1, enemyx[i], enemyy[i])



                    #Game Over
                if enemyy[i]>440 and (plrx> enemyx[i] and plrx <enemyx[i]+10) or (boy > 440 and (plrx> box-20 and plrx <box+20)):
                    collsound = mixer.Sound('explosion.wav')
                    collsound.play()
                    for j in range(numofene):
                        enemyy[j]=1000
                    g=1




                    # COLLISION

                if (buly > enemyy[i] and buly < enemyy[i] + 10) and (bulx > enemyx[i] - 40 and bulx < enemyx[i] + 40):
                    collsound=mixer.Sound('explosion.wav')
                    collsound.play()
                    screen.blit(blast, (enemyx[i], enemyy[i]))
                    enemyy[i] = random.randint(50, 150)
                    enemyx[i] = random.randint(0, 735)
                    bul_state = 'ready'
                    buly = 500
                    bulx = plrx
                    bulych = 0

                    score_value += 1

                show_scores(textX,textY)

            if plrx > 736:
                plrx = 736
            elif plrx < 0:
                plrx = 0
            else:
                plrx += plrxc

            player(plrx,plry)
        else:
            gameovrtxt()
            for event in events:
                if event.type == pygame.QUIT:
                    run=False




    pygame.display.update()

