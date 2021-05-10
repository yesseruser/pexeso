import pygame
from pygame.surface import Surface

pygame.init()

okno = pygame.display.set_mode((700, 700))
obrazky = []

prvni_karticka = (-1, -1)
druha_karticka = (-1, -1)

def nacteni_obrazku():
    """
    Loads all Pictures
    """
    for index in range(0, 9, 1):
        obrazek = pygame.transform.smoothscale(pygame.image.load("obrazky/" + str(index) + ".png"),(150, 150))
        obrazky.append(obrazek)

karticky = [
    [1, 2, 5, 7],
    [5, 6, 3, 4],
    [6, 7, 8, 3],
    [8, 4, 2, 1]
]
def kresleni_karticek():
    """
    Draws all the cards in a line
    """
    okno.fill((0, 0, 0))
    for radek in range(0, 4, 1):
        for sloupec in range(0, 4, 1):
            karticka = karticky[radek][sloupec]
            if karticka != -1:
                souradnice: tuple[int, int] = (sloupec * 150 + (sloupec + 1) * 20, radek * 150 + (radek + 1) * 20)
                if prvni_karticka == (sloupec, radek):
                    okno.blit(obrazky[karticka], souradnice)
                else:
                    okno.blit(obrazky[0], souradnice)
    pygame.display.flip()

def kontrola_karticek():
    global prvni_karticka, druha_karticka
    x1, y1 = prvni_karticka
    prvni_cislo = karticky[y1][x1]
    x2, y2 = druha_karticka
    druhe_cislo = karticky[y2][x2]
    if prvni_cislo == druhe_cislo:
        karticky[y1][x1] = -1
        karticky[y2][x2] = -1
    else:
        prvni_karticka = (-1, -1)
        druha_karticka = (-1, -1)
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
            karticka = mx // 170, my // 170
            if prvni_karticka == (-1, -1):
                prvni_karticka = karticka
            elif prvni_karticka != karticka:
                druha_karticka = karticka
                kontrola_karticek()
        kresleni_karticek()
