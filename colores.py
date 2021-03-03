import pygame
from pygame.locals import *
import random
import time
import os
import math
import json

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20) 

length = 800
height = 600
screen = pygame.display.set_mode((length, height))
pygame.display.set_caption('Memorama')
background_colour = (0,0,0)
screen.fill(background_colour)

colores_dict = {
(0,0,0) : 'Black',
(255,255,255) : 'White',
(255,0,0) : 'Red',
(0,255,0) : 'Lime',
(0,0,255) : 'Blue',
(255,255,0) : 'Yellow',
(0,255,255) : 'Cyan',
(255,0,255) : 'Magenta',
(192,192,192) : 'Silver',
(128,128,128) : 'Gray',
(128,0,0) : 'Maroon',
(128,128,0) : 'Olive',
(0,128,0) : 'Green',
(128,0,128) : 'Purple',
(0,128,128) : 'Teal',
(0,0,128) : 'Dark Blue'
}

colores_lista = [
(0,0,0),
(255,255,255),
(255,0,0),
(0,255,0),
(0,0,255),
(255,255,0),
(0,255,255),
(255,0,255),
(192,192,192),
(128,128,128),
(128,0,0),
(128,128,0),
(0,128,0),
(128,0,128),
(0,128,128),
(0,0,128)
]

num_colores = 9
colores_mostrados = {}
colores_mostrados_lista = []
pos_color = 0

for y in range(1, int(math.sqrt(num_colores)) + 1):
    space_p_partY = height // int(math.sqrt(num_colores))

    for x in range(1, int(math.sqrt(num_colores)) + 1):

        space_p_partX = length // int(math.sqrt(num_colores))
        p1 = ((space_p_partX * x) - space_p_partX, (space_p_partY * y) - space_p_partY)
        p4 = ((space_p_partX * x), (space_p_partY * y))
        rand_color = random.choice(colores_lista)

        # while rand_color in colores_mostrados_lista:
        #     rand_color = random.choice(colores_lista)

        colores_mostrados[pos_color] = colores_dict[rand_color]
        colores_mostrados_lista.append(rand_color)
        pygame.draw.rect(screen, rand_color, (p1, p4))
        text = font.render(colores_dict[rand_color], False, (0,0,0)) if colores_dict[rand_color] != 'Black' else font.render(colores_dict[rand_color], False, (255,255,255))
        screen.blit(text, (p1, p4))

        pos_color += 1

pygame.display.update()

tiempo = 0
while tiempo < 6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.time.wait(1000)
    tiempo += 1

pygame.quit()

puntuacion = 0

for i in colores_mostrados:
    if input(f'Color {i} ').lower() == colores_mostrados[i].lower():
        puntuacion += 10
        print('Correcto!', puntuacion)
    else:
        print('Incorrecto!', puntuacion)

print(f'puntuacion final = {puntuacion}')
name = input('Name? ')

if os.path.isfile('puntuaciones.json'):
    with open('puntuaciones.json', 'r') as json_read:
        json_object = json.loads(json_read.read().replace("'", '"'))

    with open('puntuaciones.json', 'w') as json_write:
        if name in [i for i in json_object]:
            if json_object[name] < puntuacion:
                json_object[name] = puntuacion
        else:
            json_object[name] = puntuacion
        json_write.write(f'{json_object}')

else:
    with open('puntuaciones.json', 'w') as json_write:
        this = {name: puntuacion}
        json_write.write(f'{this}')