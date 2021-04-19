import pygame

pygame.init()

pygame.display.set_mode((700, 700))

obrazky = []


def nacteni_obrazku():
    index = 0
    while index < 9:
        obrazky.append(pygame.image.load("obrazky/" + str(index) + ".png"))
        index += 1


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
