from typing import Any, Tuple, Union, List

import pygame
from pygame.surface import Surface

pygame.init()

okno: Surface = pygame.display.set_mode((700, 700))
souradnice: tuple[Union[int, Any], int] = (sloupec * 150 + (sloupec + 1) * 20, 20)
obrazky = []


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
    for sloupec in range(0, 4, 1):
        okno.blit(obrazky[0], souradnice)
    pygame.display.flip()


nacteni_obrazku()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
