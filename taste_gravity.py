import sys, pygame
from time import time, sleep
from heavyobject import HeavyObject
pygame.init()


size = width, height = 1000, 600
speed = [0.0,1.0]
black = 0,0,0
gravity = -0.01

screen = pygame.display.set_mode(size)
dir(screen)

balls = [
    HeavyObject(
        screen, 'ball.gif',
        position = (0, 0),
        speed = (2.0, 0.0),
        mass = 2.0
    ),
    HeavyObject(
        screen,
        'ball.gif',
        (width/2, 0),
        (0.0, 0.0),
        1.0
    )
]

flickTime = 0.0
sleepTime = 0.01
downPoint = (0,0)
flickTime = 0.0

while 1:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            downPoint = event.pos
            for ball in balls:
                if ball.rect().collidepoint(downPoint):
                    flickTime = time()
                    clickedThing = ball
                    break
            else:
                flickTime = 0.0

        if event.type == pygame.MOUSEBUTTONUP:
            if flickTime != 0.0:
                clickTime = (time() - flickTime) / sleepTime
                upPoint = event.pos
                speed = ( (upPoint[0] - downPoint[0]) / clickTime,
                          (upPoint[1] - downPoint[1]) / clickTime )
                clickedThing.speed( speed )
            flickTime = 0.0

        if event.type == pygame.MOUSEMOTION:
            pass

    screen.fill(black)
    for ball in balls:
        ball.move()
    pygame.display.flip()
    sleep(sleepTime)

