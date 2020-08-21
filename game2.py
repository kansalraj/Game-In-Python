
import pygame
from pygame.locals import *
import math
import random

# Initializing game
pygame.init()
width, height = 1280, 960
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[200,100]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194


# Loading pics
player = pygame.image.load("/home/ankit/Downloads/Dude.png")
bgd = pygame.image.load("/home/ankit/Downloads/bgd.jpg")
home = pygame.image.load("/home/ankit/Downloads/home.png")
arrow = pygame.image.load("/home/ankit/Downloads/bullet3.png")
badguyimg1 = pygame.image.load("/home/ankit/Downloads/badguy.png")
badguyimg=badguyimg1
healthbar = pygame.image.load("/home/ankit/Downloads/red.png")
health = pygame.image.load("/home/ankit/Downloads/healthbar.png")
gameover = pygame.image.load("/home/ankit/Downloads/gameover.png")
youwin = pygame.image.load("/home/ankit/Downloads/youwin.png")



#  keep looping

running = 1
exitcode = 0
while running:
    badtimer-=1

    
    # clearing screen before drawing it again
    screen.fill(0)

    #  draw bgd and house
    for x in range(width/bgd.get_width()+1):
        for y in range(height/bgd.get_height()+1):
            screen.blit(bgd,(x*250,y*250))
    screen.blit(home,(-50,-60))
    screen.blit(home,(-50,75))
    screen.blit(home,(-50,210))
    screen.blit(home,(-50,345 ))
    screen.blit(home,(-50,475 ))
    screen.blit(home,(-50,605 ))
    screen.blit(home,(-50,735 ))


    # angry bird position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 

    #  Drawing arrows

    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>1280 or bullet[2]<-64 or bullet[2]>960:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # Drawing enemy

    if badtimer==0:
        badguys.append([1280, random.randint(50,860)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        # Attacking residense
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        #Checking collisions
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1
            
        # Next enemy

        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)



    # clock
    font = pygame.font.Font(None, 100)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[1270,5]
    screen.blit(survivedtext, textRect)
    
    # health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

        
    #  update screen
    pygame.display.flip()
    #looping events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+102,playerpos1[1]+52])



    # Moving angry bird
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    #Win/Lose 
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
# Win/lose display        
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (400, 200))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (400,200))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()        

