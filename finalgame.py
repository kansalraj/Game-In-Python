
import pygame
from pygame.locals import *
import math
import random
# Initializing game
restart = 1
wait = 0

pygame.init()
pygame.mixer.init()
high = 0

while restart:
 
 pygame.mixer.init()
 width, height = 1920, 1017
 screen=pygame.display.set_mode((width, height)) 


 keys = [False, False, False, False]
 playerpos=[200,100]
 acc=[0,0]
 arrows=[]
 cheat=[0,0,0,0,0]
 badtimer=100
 badtimer1=0
 badguys=[[640,100]]
 goodtimer=200
 goodtimer1=0
 goodguys=[[640,300]]
 bombtimer=300
 bombtimer1=0
 bombguys=[] 
 dtimer=250
 dtimer1=0
 dguys=[] 
 healthvalue=194
 s1=100
 s2 = 14
 s3 = 20
 s4 = -64
 a = 0
 


 # Loading pics
 player1 = pygame.image.load("/home/ankit/Downloads/Dude1.png")
 player = player1
 player2 = pygame.image.load("/home/ankit/Downloads/Dude2.png")
 player3 = pygame.image.load("/home/ankit/Downloads/Dude3.png")
 player4 = pygame.image.load("/home/ankit/Downloads/Dude4.png")
 player5 = pygame.image.load("/home/ankit/Downloads/Dude5.png")
 
 
 star = pygame.image.load("/home/ankit/Downloads/star.png")
 bgd = pygame.image.load("/home/ankit/Downloads/image_1_(2).jpg")
 home = pygame.image.load("/home/ankit/Downloads/home4.png")
 arrow = pygame.image.load("/home/ankit/Downloads/bullet5.png")
 badguyimg1 = pygame.image.load("/home/ankit/Downloads/badguy.png")
 goodguyimg1 = pygame.image.load("/home/ankit/Downloads/life.png")
 bombguyimg1 = pygame.image.load("/home/ankit/Downloads/bomb.png")
 badguyimg=badguyimg1

 dguyimg1 = pygame.image.load("/home/ankit/Downloads/danger.png")
 dguyimg=dguyimg1
 bombguyimg=bombguyimg1
 goodguyimg=goodguyimg1
 health = pygame.image.load("/home/ankit/Downloads/healthbar.png")
 gameover = pygame.image.load("/home/ankit/Downloads/gameover.png")
 youwin = pygame.image.load("/home/ankit/Downloads/you_win.png")
 enemy = pygame.mixer.Sound("/home/ankit/Downloads/Arrow+3.wav")
 pain = pygame.mixer.Sound("/home/ankit/Downloads/pain.wav")
 life = pygame.mixer.Sound("/home/ankit/Downloads/life.wav")
 blast = pygame.mixer.Sound("/home/ankit/Downloads/blast.wav")
 pygame.mixer.music.load('/home/ankit/Downloads/123.wav')
 pygame.mixer.music.play(-1, 0.0)
 pygame.mixer.music.set_volume(1)



 running = 1
 exitcode = 0
 out = 1
 screen.fill(0)
 
 
 while out:
     font = pygame.font.Font(None, 100)
     screen.blit(bgd,(100,0))
     text2 = font.render("""PRESS 1' FOR LEVEL 1 """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery-324
    
     screen.blit(text2, textRect2)
     
     text2 = font.render("""PRESS '2' FOR LEVEL 2 """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery-224
    
     screen.blit(text2, textRect2)
     text2 = font.render("""PRESS '3' FOR LEVEL 3 """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery-124
    
     screen.blit(text2, textRect2)
     text2 = font.render("""PRESS '4' FOR LEVEL 4 """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery-24
    
     screen.blit(text2, textRect2)
     text2 = font.render("""PRESS '5' FOR LEVEL 5 """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+76
    
     screen.blit(text2, textRect2)
     
     text2 = font.render("""PRESS 'X' TO EXIT """, True, (125,0,125))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+176
    
     screen.blit(text2, textRect2)
  

     wait = pygame.time.get_ticks()
     pygame.display.flip()
     for event in pygame.event.get():
         screen.blit(bgd,(0,0))
         if event.type==pygame.QUIT:
             # quit the game
             pygame.quit() 
             exit(0) 
         if event.type == pygame.KEYDOWN:
             
             if event.key==K_1:

                
                 
                 out = 0
                 player = player2
                 s1 = 200
                 s2 = 7
                 s3 = 15
                 
                 
             elif event.key==K_2:
                 out = 0
                 player = player5
                 s1 = 150
                 s2 = 10
                 s3 = 18
                 
             elif event.key==K_3:
                 out = 0
                 player = player1
                 s1 = 100
                 s2 = 14
                 s3 = 20
                 
             elif event.key==K_4:
                 out = 0
                 player = player3
                 s1 = 90
                 s2 = 17
                 s3 = 26


             elif event.key==K_5:
                 out = 0
                 player = player4
                 s1=80
                 s2 = 20
                 s3 = 32
             elif event.key==K_x:
                 pygame.quit() 
                 exit(0) 
                 



         if out == 0:
           break    

 while running:
     badtimer-=1
     goodtimer-=1
     bombtimer-=1
     dtimer-=1

    
     # clearing screen before drawing it again
     screen.fill(0)

    
     #for x in range(width/bgd.get_width()+2):
     #    for y in range(height/bgd.get_height()+1):
      #       screen.blit(bgd,(x*250,y*250))
     screen.blit(bgd,(0,0))
     screen.blit(home,(0,-60))
     screen.blit(home,(0,75))
     screen.blit(home,(0,210))
     screen.blit(home,(0,345 ))
     screen.blit(home,(0,475 ))
     screen.blit(home,(0,605 ))
     screen.blit(home,(0,735 ))
     screen.blit(home,(0,865 ))

 
     # angry bird position and rotation
     position = pygame.mouse.get_pos()
     angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
     playerrot = pygame.transform.rotate(player, 360-angle*57.29)
     playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
     screen.blit(playerrot, playerpos1) 

     #   arrows maaar
 
     for bullet in arrows:
         index=0
         velx=math.cos(bullet[0])*s3
         vely=math.sin(bullet[0])*s3
         bullet[1]+=velx
         bullet[2]+=vely
         if bullet[1]<-64 or bullet[1]>1920 or bullet[2]<-64 or bullet[2]>1017:
             arrows.pop(index)
         index+=1
         for projectile in arrows:
             arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
             screen.blit(arrow1, (projectile[1], projectile[2]))
     a = a - 1
     # enemy aaya re
 
     if badtimer==0:
         badguys.append([1920, random.randint(50,1017)])
         badtimer=s1-(badtimer1*2)
         if badtimer1>=35:
             badtimer1=35
         else:
             badtimer1+=5
     index=0
     for badguy in badguys:
         if badguy[0]<s4:
             badguys.pop(index)
             
         badguy[0]-=s2
         # attACK residense
         badrect=pygame.Rect(badguyimg.get_rect())
         badrect.top=badguy[1]
         badrect.left=badguy[0]
         
         if badrect.left<64:
             if (cheat[0]==0 or cheat[1]==0 or cheat[2]==0 or cheat[3]==0 ):

                healthvalue -= random.randint(5,20)
             badguys.pop(index)
         #collisions check karra
         index1=0
         for bullet in arrows:
             arrow2 = pygame.transform.rotate(arrow, 360-bullet[0]*57.29)
             bullrect=pygame.Rect(arrow2.get_rect())
             bullrect.left=bullet[1]
             bullrect.top=bullet[2]
             if badrect.colliderect(bullrect):
                 pain.play()
                 acc[0]+=1
                 badguys.pop(index)
                 arrows.pop(index1)
             index1+=1
             
         # Naya enemy

         index+=1
         
     for badguy in badguys:
         screen.blit(badguyimg, badguy)
     





     # life aaya re
 
     if goodtimer==0:
         goodguys.append([1920, random.randint(50,1017)])
         goodtimer=500-(goodtimer1)
         if goodtimer1>=35:
             goodtimer1=35
         else:
             goodtimer1+=5
     index=0
     for goodguy in goodguys:
         if goodguy[0]<-64:
             goodguys.pop(index)
             
         goodguy[0]-=s2
         

         goodrect=pygame.Rect(goodguyimg.get_rect())
         goodrect.top=goodguy[1]
         goodrect.left=goodguy[0]
         

         if goodrect.left<64:
             
             goodguys.pop(index)
         #collisions check karra
        
         
         plrect=pygame.Rect(playerrot.get_rect())
         plrect.left=playerpos1[0]
         plrect.top=playerpos1[1]
         if goodrect.colliderect(plrect):
                 life.play()
                 healthvalue += 20
                 
                 goodguys.pop(index)
                 
                 
             
             
         # Naya life

         index+=1
     for goodguy in goodguys:
         screen.blit(goodguyimg, goodguy)

     


     # BOMBS
 
     if bombtimer==0:
         bombguys.append([1920, random.randint(50,1017)])
         bombtimer=550-(bombtimer1)
         if bombtimer1>=35:
             bombtimer1=35
         else:
             bombtimer1+=5
     index=0
     for bombguy in bombguys:
         if bombguy[0]<-64:
             bombguys.pop(index)
             
         bombguy[0]-=s2
         

         bombrect=pygame.Rect(bombguyimg.get_rect())
         bombrect.top=bombguy[1]
         bombrect.left=bombguy[0]
         

         if bombrect.left<64:
             
             bombguys.pop(index)
         #collisions check karra
         index1=0
         for bullet in arrows:
             arrow2 = pygame.transform.rotate(arrow, 360-bullet[0]*57.29)
             bullrect=pygame.Rect(arrow2.get_rect())
             bullrect.left=bullet[1]
             bullrect.top=bullet[2]
             if bombrect.colliderect(bullrect):
                 
                 blast.play()
                 s4 =1920
                 a = 14
                 bombguys.pop(index)
                 arrows.pop(index1)
                 
             index1+=1
             
         # Naya bomb

         index+=1
     for bombguy in bombguys:
         screen.blit(bombguyimg, bombguy)

     if a == 0:
        s4 = -64
     



















     # danger
 
     if dtimer==0:
         dguys.append([1920, random.randint(50,1017)])
         dtimer=550-(dtimer1)
         if dtimer1>=35:
             dtimer1=35
         else:
             dtimer1+=5
     index=0
     for dguy in dguys:
         if dguy[0]<-64:
             dguys.pop(index)
             
         dguy[0]-=s2
         

         drect=pygame.Rect(dguyimg.get_rect())
         drect.top=dguy[1]
         drect.left=dguy[0]
         

         if drect.left<64:
             
             dguys.pop(index)
         #collisions check karra
         index1=0
         for bullet in arrows:
             arrow2 = pygame.transform.rotate(arrow, 360-bullet[0]*57.29)
             bullrect=pygame.Rect(arrow2.get_rect())
             bullrect.left=bullet[1]
             bullrect.top=bullet[2]
             if drect.colliderect(bullrect):
                 
                 blast.play()
                 healthvalue -= 60
                
                 dguys.pop(index)
                 arrows.pop(index1)
                 
             index1+=1
             
         # Naya bomb

         index+=1
     for dguy in dguys:
         screen.blit(dguyimg, dguy)





















     




 
 
 
     # clock
     
     font = pygame.font.Font(None, 100)
     survivedtext = font.render(str((90000 + wait -pygame.time.get_ticks())/60000)+":"+str((90000 +wait -pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
     textRect = survivedtext.get_rect()
     textRect.topright=[1910,5]
     screen.blit(survivedtext, textRect)
     
     
     #score
   
     survivedtext1 = font.render("SCORE"+":"+str(acc[0]).zfill(2), True, (200,0,0))
     textRect1 = survivedtext1.get_rect()
     textRect1.topright=[1630,5]
     screen.blit(survivedtext1, textRect1)
      
     #high
   
     survivedtext1 = font.render(" HIGH SCORE"+":"+str(high).zfill(2) + " ", True, (128,0,128))
     textRect1 = survivedtext1.get_rect()
     textRect1.topright=[1230,5]
     screen.blit(survivedtext1, textRect1)


     # health bar.......
    
     for health1 in range(healthvalue):
         screen.blit(health, (health1+8,5))
     font1 = pygame.font.Font(None, 50) 
     survivedtext2 = font1.render("health", True, (0,0,0))
     textRect2 = survivedtext2.get_rect()
     
     screen.blit(survivedtext2, textRect2)
      
 
         
     #  update screen
     pygame.display.flip()
 
 
 
     
     for event in pygame.event.get():
         
         if event.type==pygame.QUIT:
             # quit the game
             pygame.quit() 
             exit(0) 
         if event.type == pygame.KEYDOWN:


              
             if event.key==K_p:


                 
               wait2 = pygame.time.get_ticks()

               
               font = pygame.font.Font(None, 100)
               
               text2 = font.render("""PAUSED""", True, (125,0,125))
               textRect2 = text2.get_rect()
               textRect2.centerx = screen.get_rect().centerx
               textRect2.centery = screen.get_rect().centery-324
    
               screen.blit(text2, textRect2)
     
               text2 = font.render("""PRESS 'P' TO RESUME """, True, (125,0,125))
               textRect2 = text2.get_rect()
               textRect2.centerx = screen.get_rect().centerx
               textRect2.centery = screen.get_rect().centery-224
    
               screen.blit(text2, textRect2)
               text2 = font.render("""PRESS 'X' TO QUIT """, True, (125,0,125))
               textRect2 = text2.get_rect()
               textRect2.centerx = screen.get_rect().centerx
               textRect2.centery = screen.get_rect().centery-124

               
               pp = 1
               while pp :
                 pygame.display.flip()  
                 font = pygame.font.Font(None, 100)
               
                 text2 = font.render("***PAUSED***", True, ( 100,0,255))
                 textRect2 = text2.get_rect()
                 textRect2.centerx = screen.get_rect().centerx
                 textRect2.centery = screen.get_rect().centery-324
      
                 screen.blit(text2, textRect2)
       
                 text2 = font.render("""PRESS 'P' TO RESUME """, True, ( 100,0,255))
                 textRect2 = text2.get_rect()
                 textRect2.centerx = screen.get_rect().centerx
                 textRect2.centery = screen.get_rect().centery-224
      
                 screen.blit(text2, textRect2)
                 text2 = font.render("""PRESS 'X' TO QUIT """, True, ( 100,0,255))
                 textRect2 = text2.get_rect()
                 textRect2.centerx = screen.get_rect().centerx
                 textRect2.centery = screen.get_rect().centery-124
                 screen.blit(text2, textRect2)
   
                 for event in pygame.event.get():
                    if event.type==pygame.QUIT:
            #.        quit the game
                        pygame.quit() 
                        exit(0) 
                    if event.type == pygame.KEYDOWN:
                        if event.key==K_x:
                           pygame.quit() 
                           exit(0) 
                            

                        
                        elif event.key==K_p:
                           pp = 0
               wait1 = pygame.time.get_ticks()
               wait += wait1 - wait2
      
             elif event.key==K_w:
                 keys[0]=True
             elif event.key==K_a:
                 keys[1]=True
             elif event.key==K_s:
                 keys[2]=True
             elif event.key==K_d:
                 
                 keys[3]=True

             elif event.key==K_l:
                 cheat[0]=1
             elif event.key==K_i:
                 cheat[1]=1
             elif event.key==K_f:
                 cheat[2]=1
             elif event.key==K_e:
                 
                 cheat[3]=1
                  
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
             
             enemy.play()
             position=pygame.mouse.get_pos()
             acc[1]+=1
             arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
 
 
 
     # Moving angry bird
     if keys[0]:
         playerpos[1]-=10
     elif keys[2]:
         playerpos[1]+=10
     if keys[1]:
         playerpos[0]-=10
     elif  keys[3]:
         playerpos[0]+=10
     #Win/Lose 
     if pygame.time.get_ticks()>=(wait+90000):
         running=0
         exitcode=1
     if healthvalue<=0:
         running=0
         exitcode=0
     if acc[1]!=0:
         accuracy=int(acc[0]*1.0/acc[1]*100)
     else:
         accuracy=0
 # Win/lose display        
 if exitcode==0:
     
     pygame.font.init()
     font = pygame.font.Font(None, 100)
     text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,0,0))
     textRect = text.get_rect()
     textRect.centerx = screen.get_rect().centerx
     textRect.centery = screen.get_rect().centery+24
     screen.blit(gameover, (600, 200))
     screen.blit(text, textRect)
     text1 = font.render("Score: "+str(acc[0]), True, (255,0,0))
     if acc[0]>high:
         high = acc[0]
     textRect1 = text1.get_rect()
     textRect1.centerx = screen.get_rect().centerx
     textRect1.centery = screen.get_rect().centery+124
    
     screen.blit(text1, textRect1)


     text2 = font.render("CLICK ANY WHERE TO RESTART", True, (128,0,128))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+224
    
     screen.blit(text2, textRect2)
     text2 = font.render("PRESS  'X'  TO EXIT", True, (128,0,128))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+324
    
     screen.blit(text2, textRect2)
     
  


 else:
     
     pygame.font.init()
     font = pygame.font.Font(None, 100)
     text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
     textRect = text.get_rect()
     textRect.centerx = screen.get_rect().centerx
     textRect.centery = screen.get_rect().centery+24
     screen.blit(youwin, (600,200))
     screen.blit(text, textRect)
     text1 = font.render("Score: "+str(acc[0]), True, (255,0,0))
     if acc[0] > high:
         high = acc[0]
     
     textRect1 = text1.get_rect()
     textRect1.centerx = screen.get_rect().centerx
     textRect1.centery = screen.get_rect().centery+124
     
     screen.blit(text1, textRect1)

     text2 = font.render("CLICK ANY WHERE TO RESTART", True, (128,0,128))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+224
    
     screen.blit(text2, textRect2)


     text2 = font.render("PRESS  'X'  TO EXIT", True, (128,0,128))
     textRect2 = text2.get_rect()
     textRect2.centerx = screen.get_rect().centerx
     textRect2.centery = screen.get_rect().centery+324
    
     screen.blit(text2, textRect2)



     if accuracy == 100:
         screen.blit(star, (700, 350))
         screen.blit(star, (850, 350))
         screen.blit(star, (1000, 350))
     elif accuracy>50:
         screen.blit(star, (750, 350))
         screen.blit(star, (900, 350))
         
     elif accuracy>0:
         
         screen.blit(star, (850, 350))
         
         
         

     
         

 while 1:
     restart = 0
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             exit(0)
         restart = 0
         if event.type==pygame.MOUSEBUTTONDOWN:
             restart = 1  
             wait = pygame.time.get_ticks()  
             break
         if event.type == pygame.KEYDOWN:
             
            if event.key==K_x:

                pygame.quit() 
                exit(0) 
              




                    
     if restart ==1:
             break    
     pygame.display.flip() 
 
   
