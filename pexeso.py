import random

import pygame
pygame.init()

okno = pygame.display.set_mode((700, 700))

obrazky = []

mapa = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

prvni_karticka = (-1, -1)
druha_karticka = (-1, -1)

def michani_karticek():
    pass

def volna_pozice():
    y = random.randint(0, 3)
    x = random.randint(0, 3)
    while mapa[y][x] > 0:
        y = random.randint(0, 3)
        x = random.randint(0, 3)
        return y, x

def nacteni_obrazku():
    for index in range(0, 9, 1):
        obrazek = pygame.image.load("obrazky/" + str(index) + ".png")
        obrazky.append(pygame.transform.smoothscale(obrazek, (150, 150)))

def kresleni_karticek():
    okno.fill((0, 0, 0))
    for radek in range(0, 4, 1):
        for sloupec in range(0, 4, 1):
            karticka = mapa[radek][sloupec]
            if karticka != -1:
                souradnice = (sloupec * 150 + (sloupec + 1) * 20, (radek * 150 + (radek + 1) * 20))
                if prvni_karticka == (sloupec, radek) or druha_karticka == (sloupec, radek):
                    okno.blit(obrazky[karticka], souradnice)
                else:
                    okno.blit(obrazky[0], souradnice)
    pygame.display.flip()

def kontrola_karticek():
    global prvni_karticka, druha_karticka
    x1, y1 = prvni_karticka
    prvni_cislo = mapa[y1][x1]
    x2, y2 = druha_karticka
    druhe_cislo = mapa[y2][x2]
    # odstraneni karticek
    if prvni_cislo == druhe_cislo:
        mapa[y1][x1] = -1
        mapa[y2][x2] = -1
    # zakryti karticek
    prvni_karticka = (-1, -1)
    druha_karticka = (-1, -1)

hodiny = pygame.time.Clock()

def cekani():
    for tick in range(60):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        hodiny.tick(60)

def smycka(prvni_karticka):
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
                    kresleni_karticek()
                    cekani()
                    kontrola_karticek()

nacteni_obrazku()
smycka(prvni_karticka)