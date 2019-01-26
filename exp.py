import pygame
from pygame.locals import *
from random import randint as r

RES=[1920,1080]

shift=-1
pygame.init()
screen=pygame.display.set_mode(RES, FULLSCREEN)
Clock=pygame.time.Clock()

run=True

screen.fill([255,255,255])


for i in range(RES[0]):
    shift=shift*(-1)
    
    for j in range(RES[1]):
        color=[r(0,255)]*3
        x=pygame.draw.line(screen, color, [i,j],[i,j])
        """
        if shift==-1:
            if not j%2==0:
                x=pygame.draw.line(screen, color, [i,j],[i,j])
        else:
            if j%2==0:
                x=pygame.draw.line(screen, color, [i,j],[i,j])"""

pygame.display.update()
            
        
            
            


while run:
    for e in pygame.event.get():
        if e.type==QUIT:run=False
        if e.type==KEYDOWN:
            if e.key==K_ESCAPE:
                run=False

    print(Clock.get_fps())
    Clock.tick(1000)

pygame.quit()

    
        

