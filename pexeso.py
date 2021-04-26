from typing import Any, Tuple, Union, List

import pygame
from pygame.surface import Surface

pygame.init()

okno: Surface = pygame.display.set_mode((700, 700))
obrazky = []

prvni_karticka = (0, 0)
druha_karticka = (-1, -1)

def nacteni_obrazku():
    """
    Loads all Pictures
    """
    for index in range(0, 9, 1):
        pygame.transform.smoothscale(pygame.image.load("obrazky/" + str(index) + ".png"),(150, 150))
        obrazky.append(pygame.image.load("obrazky/" + str(index) + ".png"))

karticky: list[list[int]] = [
    [1, 2, 5, 7],
    [5, 6, 3, 4],
    [6, 7, 8, 3],
    [8, 4, 2, 1]
]
def kresleni_karticek():
    """
    Draws all the cards in a line
    """
    for radek in range(0, 4, 1):
        for sloupec in range(0, 4, 1):
            souradnice: tuple[Union[int, Any], int] = (sloupec * 150 + (sloupec + 1) * 20, radek * 150 + (radek + 1) * 20)
            if prvni_karticka == (radek, sloupec):
                okno.blit(obrazky[1], souradnice)
                okno.blit(obrazky[kart])
            else:
                okno.blit(obrazky[0], souradnice)
            okno.blit(obrazky[0], souradnice)
    pygame.display.flip()


nacteni_obrazku()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            print(mx, my)
            x, y = mx // 170, my // 170
            print(x, y)
            prvni_karticka = x, y
        kresleni_karticek()
