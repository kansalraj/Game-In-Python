
import pygame
from pygame.locals import *
import math
import random

pygame.init()
width, height = 1280, 960
screen=pygame.display.set_mode((width, height))
bgd = pygame.image.load("/home/ankit/Downloads/bgd.jpg")
home = pygame.image.load("/home/ankit/Downloads/home.png")
keys = [False, False, False, False]
playerpos=[100,100]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194




player = pygame.image.load("/home/ankit/Downloads/Dude.png")
arrow = pygame.image.load("/home/ankit/Downloads/bullet3.png")
badguyimg1 = pygame.image.load("/home/ankit/Downloads/badguy.png")
badguyimg=badguyimg1




while 1:


    screen.fill(0)



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



    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
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
    # 6.3 - Draw badgers
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
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


        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.3 - Next bad guy
        
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
        



    pygame.display.flip()






    for event in pygame.event.get():


        if event.type==pygame.QUIT:


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
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])



    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
badtimer-=1        
