import pygame, tj
from pygame.locals import *

pygame.init()
RES = [500,500]
pygame.joystick.init()
BG_COLOR = tj.colors["WHITE"]
RECT_COLOR1 = tj.colors["RED"]
RECT_COLOR2 = tj.colors["BLUE"]
HEAD = tj.colors["ORANGE"]
TEXT_COLOR = tj.colors["CHOCOLATE"]
TEXT_SIZE = 25
TEXT_COLOR2 = tj.colors["DARK GREEN"]
TEXT_SIZE2 = 20
PADDING = 30

screen = pygame.display.set_mode(RES)
Clock = pygame.time.Clock()

run = True
m = 3

LIVES1 = 200
LIVES2 = 200

x1, y1 = [RES[0] // 2, RES[1] // 2]
x2, y2 = [RES[0] // 2 - PADDING, RES[1] // 2 - PADDING]
adderx1, addery1, adderx2, addery2 = [0, 0, 0, 0]
shot1 = False
shot_made1 = False
shot2 = False
shot_made2 = False
pygame.font.init()


def draw_text(screen, size, txt, color, pos):
    font = pygame.font.SysFont(None, size)
    text = font.render(txt, True, color)
    screen.blit(text, pos)


def draw_projectiles(Projectiles):
    global RECT_COLOR1, RECT_COLOR2
    L = Projectiles

    for i in range(len(Projectiles)):
        try:
            proj = Projectiles[i]
        except:
            continue
        a = proj[0]
        b = proj[1]
        adda = proj[2]
        addb = proj[3]
        a += adda
        b += addb

        if (a not in range(RES[0])) or (b not in range(RES[1])):
            L.pop(i)
            continue
        type = proj[4]

        if type == 0: RECT_COLOR = RECT_COLOR1
        if type == 1: RECT_COLOR = RECT_COLOR2

        pygame.draw.circle(screen, RECT_COLOR, [a, b], 3)
        proj = [a, b, adda, addb, type]
        L[i] = proj
    return L


def check_collide(R1, R2, Projectiles):
    global LIVES1, LIVES2
    # proj = [a, b, adda, addb, type]
    for proj in Projectiles:
        a = proj[0]
        b = proj[1]
        type = proj[4]
        pos = [a, b]

        if type == 0:  # Means its a red projectile, blue will be destoyed
            if R2.collidepoint(pos):
                LIVES2 -= 1

        if type == 1:  # Means its a blue projectile, red will be destoyed
            if R1.collidepoint(pos):
                LIVES1 -= 1


def check_win():
    global LIVES1, LIVES2
    if LIVES1 < 0: return 2
    if LIVES2 < 0:
        return 1
    else:
        return 0


Projectiles = []
while run:


    # ---------     JOYSTICK EVENT HANDLING      -----------#
    for i in range(pygame.joystick.get_count()):
        J = pygame.joystick.Joystick(0)
        J.init()

    for e in pygame.event.get():
        if e.type == QUIT:
            run = False

        #print(e)
        if e.type==KEYDOWN:
            if e.key==K_ESCAPE:run=False
            
            if e.key==K_UP:addery1=-m
            if e.key==K_DOWN:addery1=m
            if e.key==K_RIGHT:adderx1=m
            if e.key==K_LEFT:adderx1=-m

            if e.key==K_w:addery2=-m
            if e.key==K_s:addery2=m
            if e.key==K_d:adderx2=m
            if e.key==K_a:adderx2=-m

            if e.key==K_m:shot1=True
            if e.key==K_RSHIFT:shot1=True
            if e.key==257:shot1=True

            if e.key==K_LSHIFT:shot2=True
            if e.key==K_x:shot2=True
            if e.key==K_q:shot2=True
            

            if e.key == K_t: x1, y1 = [RES[0] // 2, RES[1] // 2]
            if e.key == K_r: x2, y2 = [RES[0] // 2 - PADDING, RES[1] // 2 - PADDING]




        if e.type==KEYUP:
            if e.key==K_UP:addery1=0
            if e.key==K_DOWN:addery1=0
            if e.key==K_RIGHT:adderx1=0
            if e.key==K_LEFT:adderx1=0

            if e.key==K_w:addery2=0
            if e.key==K_s:addery2=0
            if e.key==K_a:adderx2=0
            if e.key==K_d:adderx2=0

            if (e.key==K_m) or  (e.key==K_RSHIFT) or (e.key==257):
                shot1=False
                shot_made1 = False
            if (e.key==K_x) or (e.key==K_LSHIFT) or (e.key==K_q):
                shot2=False
                shot_made2 = False
            





        
        if e.type == JOYBUTTONDOWN:
            if e.button == 6: x1, y1 = [RES[0] // 2, RES[1] // 2]
            if e.button == 7: x2, y2 = [RES[0] // 2 - PADDING, RES[1] // 2 - PADDING]
            if e.button == 9: shot1 = True
            if e.button == 8: shot2 = True
        if e.type == JOYBUTTONUP:
            if e.button == 9:
                shot1 = False
                shot_made1 = False
            if e.button == 8:
                shot2 = False
                shot_made2 = False

        if e.type == JOYAXISMOTION:
            adderx1 = int(J.get_axis(0) * m)  # L Stick 1
            addery1 = int(J.get_axis(1) * m)  # L Stick 2
            adderx2 = int(J.get_axis(2) * m)  # R Stick 1
            addery2 = int(J.get_axis(3) * m)  # R Stick 2
            #a4 = J.get_axis(4)  # L Trigger
            #a5 = J.get_axis(5)  # R Trigger




    #-----------------     REAL CODE    ----------------------#

    screen.fill(BG_COLOR)
    x1 += adderx1
    y1 += addery1
    x2 += adderx2
    y2 += addery2

    R1 = pygame.draw.rect(screen, RECT_COLOR1, [x1, y1, PADDING, PADDING])
    pygame.draw.rect(screen, HEAD, [x1 + 10, y1 + 10, 10, 10])
    R2 = pygame.draw.rect(screen, RECT_COLOR2, [x2, y2, PADDING, PADDING])
    pygame.draw.rect(screen, HEAD, [x2 + 10, y2 + 10, 10, 10])

    if shot1 and (not shot_made1):
        a = x1 + PADDING // 2
        b = y1 + PADDING // 2
        adda = int(adderx1 * 2)
        addb = int(addery1 * 2)
        if (adda == 0) and (addb == 0):
            adda = 0
            addb = 2
        Data = [a, b, adda, addb, 0]  # 0 Means red, 1 means blue
        Projectiles += [Data]
        shot_made1 = True

    if shot2 and (not shot_made2):
        a = x2 + PADDING // 2
        b = y2 + PADDING // 2
        adda = int(adderx2 * 2)
        addb = int(addery2 * 2)
        if (adda == 0) and (addb == 0):
            adda = 0
            addb = 2
        Data = [a, b, adda, addb, 1]  # 0 Means red, 1 means blue
        Projectiles += [Data]
        shot_made2 = True

    if len(Projectiles) != 0:
        Projectiles = draw_projectiles(Projectiles)
    check_collide(R1, R2, Projectiles)
    draw_text(screen, TEXT_SIZE, "Live Projectiles: " + str(len(Projectiles)), TEXT_COLOR, [20, 10])
    draw_text(screen, TEXT_SIZE2, str(LIVES1) + " :RED LIVES", RECT_COLOR1, [RES[0] - 120, 30])
    draw_text(screen, TEXT_SIZE2, str(LIVES2) + " :BLUE LIVES", RECT_COLOR2, [RES[0] - 120, 70])
    draw_text(screen, TEXT_SIZE, "FPS: " + str(int(Clock.get_fps())), TEXT_COLOR, [20, RES[1] - 20])

    if check_win() == 1:
        screen.fill(BG_COLOR)
        draw_text(screen, 90, "RED WON", RECT_COLOR1, [90, RES[1] // 2 - 50])
    if check_win() == 2:
        screen.fill(BG_COLOR)
        draw_text(screen, 90, "BLUE WON", RECT_COLOR2, [90, RES[1] // 2 - 50])

    pygame.display.update()

    Clock.tick(60)

pygame.quit()
