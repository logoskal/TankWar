import pygame
import sys
from gamedata import *

def checkExit(events):
        """Checks If An Exit Event Is Triggered To Close The Program"""
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

def tankArrowMov(tank, tank_vel, figure):
    """Controls Movement Of Objects With Arrow Keys"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank.x - tank_vel >= 0:
        tank.x -= tank_vel
        figure = pygame.transform.rotate(figure, 90)
    if keys[pygame.K_RIGHT] and tank.right + tank_vel <= WIDTH:
        tank.x += tank_vel
        pygame.transform.rotate(figure, 270)
    if keys[pygame.K_UP] and tank.y - tank_vel >= 0:
        tank.y -= tank_vel
        pygame.transform.rotate(figure, 0)
    if keys[pygame.K_DOWN] and tank.bottom + tank_vel <= HEIGHT:
        tank.y += tank_vel
        pygame.transform.rotate(figure, 180)

def tankWasdMov(tank, tank_vel):
    """Controls Movement Of Objects With WASD Keys"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and tank.x - tank_vel >= 0:
        tank.x -= tank_vel
    if keys[pygame.K_d] and tank.right + tank_vel <= WIDTH:
        tank.x += tank_vel
    if keys[pygame.K_w] and tank.y - tank_vel >= 0:
        tank.y -= tank_vel
    if keys[pygame.K_s] and tank.bottom + tank_vel <= HEIGHT:
        tank.y += tank_vel

def checkBorder(tank):
    """Checks If argument Is Inside The Screen. If Not, Places It Inside The Screen"""
    if tank.bottom > HEIGHT:
        tank.bottom = HEIGHT
    if tank.right > WIDTH:
        tank.right = WIDTH
    if tank.left < 0:
        tank.left = 0
    if tank.top < 0:
        tank.top = 0
def shotMechanic(tank, events, shot_list, shot_button, orientation):
    """Manages Button Configuration While Shooting"""
    for event in events:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == shot_button and len(shot_list) < TOT_SHOTS:
                        if orientation == 0:
                            shot = pygame.Rect(tank.x + tank.width/2 - 5, tank.y + tank.height + 10, 10,10)
                            shot_list.append(shot)
                        elif orientation == 3:
                            shot = pygame.Rect(tank.x + tank.width/2 - 5, tank.y - 10, 10,10)
                            shot_list.append(shot)
def writeText(text, size=30, color='#D0F4F7'):
    FONT = pygame.font.SysFont('Bell MT', size)
    return FONT.render(text, True, color)

def update():
     """Update The Display"""
     pygame.display.update()