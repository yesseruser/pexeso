import pygame

pygame.init()

okno = pygame.display.set_mode((700, 700))

obrazky = []


def nacteni_obrazku():
    for index in range(0, 9, 1):
        obrazky.append(pygame.image.load("obrazky/" + str(index) + ".png"))


def kresleni_karticek():
    for sloupec in range(0, 4, 1):
        okno.blit(obrazky[0], (sloupec * 150 + (sloupec + 1) * 20, 20))
    pygame.display.flip()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
