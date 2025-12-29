import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
pygame.draw.circle(screen,GREEN,(300,300),50)
pygame.draw.circle(screen,BLUE,(100,100),50,3)
pygame.draw.circle(screen,RED,(150,300),50)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
pygame.display.flip()