
import pygame
from gamedata import *
from modules import *

pygame.init()


SCREEN = pygame.display.set_mode(RESOLUTION)
DISPLAY = pygame.display
pygame.display.set_caption(GAME_TITLE)

TANK_IMAGE = pygame.image.load('assets/graphics/tank.png').convert_alpha()

TANK1_IMAGE = pygame.transform.scale_by(TANK_IMAGE, 0.15)
TANK2_IMAGE = pygame.transform.rotate(pygame.transform.scale_by(TANK_IMAGE, 0.15), 180)

TANK1_RECT = TANK1_IMAGE.get_rect(center=(600,100))
TANK2_RECT = TANK2_IMAGE.get_rect(center=(600,540))

CLOCK = pygame.time.Clock()

TANK1_SHOTS_FIRED = []
TANK2_SHOTS_FIRED = []

TANK1_HEALTH = 10
TANK2_HEALTH = 100
game_active = True

while True:
    events = pygame.event.get()
    checkExit(events)
    CLOCK.tick(FPS)
    if TANK1_HEALTH < 0 or TANK2_HEALTH < 0:
        game_active = False
    if game_active:
        SCREEN.fill('white')
        SCREEN.blit(TANK1_IMAGE, TANK1_RECT)
        SCREEN.blit(TANK2_IMAGE, TANK2_RECT)
        tankWasdMov(TANK1_RECT, TANK_VEL)
        tankArrowMov(TANK2_RECT, TANK_VEL, TANK2_IMAGE)
        if TANK1_RECT.colliderect(TANK2_RECT):
            TANK1_RECT.x += 5
            TANK1_RECT.y += 5
            TANK2_RECT.x -= 5
            TANK2_RECT.y -= 5
            print('Collision')
        keys = pygame.key.get_pressed()
        shotMechanic(TANK1_RECT, events, TANK1_SHOTS_FIRED, pygame.K_SPACE, 0)
        shotMechanic(TANK2_RECT, events, TANK2_SHOTS_FIRED, pygame.K_RETURN, 3)
        
        if TANK1_SHOTS_FIRED:
            for shot in TANK1_SHOTS_FIRED:
                pygame.draw.rect(SCREEN, 'red', shot)
                shot.y += SHOT_VEL
                if shot.colliderect(TANK2_RECT) or shot.y > HEIGHT:
                    TANK1_SHOTS_FIRED.remove(shot)
                    MAX_SHOTS -= 1
                    if shot.colliderect(TANK2_RECT): TANK2_HEALTH -= 13
        if TANK2_SHOTS_FIRED:
            for shot in TANK2_SHOTS_FIRED:
                pygame.draw.rect(SCREEN, 'red', shot)
                shot.y -= SHOT_VEL
                if shot.colliderect(TANK1_RECT) or shot.y < 0:
                    TANK2_SHOTS_FIRED.remove(shot)
                    MAX_SHOTS -= 1
                    if shot.colliderect(TANK1_RECT): TANK1_HEALTH -= 13
            

        SCREEN.blit(writeText(f'TANK A HEALTH: {TANK1_HEALTH}',  color='red'), (10, 10))
        SCREEN.blit(writeText(f'TANK B HEALTH: {TANK2_HEALTH}',  color='red'), (WIDTH - 210, HEIGHT-30))
        checkBorder(TANK1_RECT)
        checkBorder(TANK2_RECT)            
        update()
    else:
        SCREEN.fill('black')
        if TANK1_HEALTH < 0 and TANK2_HEALTH < 0:
            SCREEN.blit(writeText('DRAW BOTH TANK WERE DESTROYED', 40), (400, 100))
        elif TANK1_HEALTH < 0:
            SCREEN.blit(writeText('GAME OVER TANK B WON', 50), (400, 100))
        elif TANK2_HEALTH < 0:
            SCREEN.blit(writeText('GAME OVER TANK A WON', 50), (400, 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            TANK1_SHOTS_FIRED.clear()
            TANK2_SHOTS_FIRED.clear()
            TANK1_HEALTH = 100
            TANK2_HEALTH = 100
            game_active = True
        update()