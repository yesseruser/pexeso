import pygame
pygame.init()

pygame.display.set_mode((700, 700))

def nacteni_obrazku():
    pass

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False