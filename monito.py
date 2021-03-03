import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
message = True

run_game = True

while run_game:

    closure = True

    text_to_underscore = lambda text, filled_text : ''.join(['_ ' if i != ' ' and i.lower() not in filled_text else i.lower() + ' ' for i in text])
    with open('palabras.txt', 'r') as palabrotas:
        text = random.choice(palabrotas.readlines())[:-1]

    attempts_left = myfont.render('intentos: 7', False, (200, 200, 200))
    right_words = ''
    wrong_words = ''

    textsurface = myfont.render(text_to_underscore(text, right_words), False, (200, 200, 200))
    pygame.display.set_caption('Ahorcado en el arbol de mi casa')
    screen = pygame.display.set_mode((800, 600))
    wrong_wordstext = myfont.render(f'letras equivocadas = {wrong_words}', False, (200, 200, 200))
    screen.blit(wrong_wordstext,(0,50))
    screen.blit(textsurface,(0, 400))
    screen.blit(attempts_left,(0,0))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    lines_dict = {2:((400, 86), (400, 186)), 3: ((397, 187), (358, 232)), 4: ((406, 187), (445, 235)), 5: ((406, 110), (449, 81)), 6:((397, 110), (341, 81))}
    num = 0

    pygame.display.update()
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run_game = False
                closure = False
            elif event.type == pygame.KEYDOWN:
                right_words += pygame.key.name(event.key) if pygame.key.name(event.key) != ' ' and pygame.key.name(event.key) in text.lower() and pygame.key.name(event.key) not in right_words else '' 
                wrong_words += pygame.key.name(event.key) if pygame.key.name(event.key) != ' ' and pygame.key.name(event.key) not in text.lower() and pygame.key.name(event.key) not in wrong_words else '' 
                textsurface = myfont.render(text_to_underscore(text, right_words), False, (200, 200, 200))
                attempts_left = myfont.render(f'intentos: {7 - len(wrong_words)}', False, (200, 200, 200))

                screen.blit(background, (0, 0))

                if all([True if i == ' ' or i in right_words else False for i in text.lower()]):
                    textsurface = myfont.render('si era la palabraaaaaaaaaaaaaaaaa, continuar? [y/n]', False, (200, 200, 200))
                    for i in range(1, len(wrong_words) + 1):
                        if i == 1:
                            pygame.draw.circle(screen, (100, 100, 100), (400, 55), 30, 3)
                        elif i <= 6:
                            pygame.draw.line(screen, (100, 100, 100), lines_dict[i][0], lines_dict[i][1], 10)
                        else:
                            textsurface = myfont.render(f'jaja, u lose, la palabra era {text}, continuar?? [y/n]', False, (200, 200, 200))
                            running = False
                    running = False

                else:
                    for i in range(1, len(wrong_words) + 1):
                        if i == 1:
                            pygame.draw.circle(screen, (100, 100, 100), (400, 55), 30, 3)
                        elif i <= 6:
                            pygame.draw.line(screen, (100, 100, 100), lines_dict[i][0], lines_dict[i][1], 10)
                        else:
                            textsurface = myfont.render(f'jaja, u lose, la palabra era {text}, continuar?? [y/n]', False, (200, 200, 200))
                            running = False
                wrong_wordstext = myfont.render(f'letras equivocadas = {wrong_words}', False, (200, 200, 200))
                screen.blit(wrong_wordstext,(0,50))
                screen.blit(textsurface,(0,400))
                screen.blit(attempts_left,(0,0))
                pygame.display.update()

    while closure:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closure = False
                run_game = False

            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'y':
                    closure = False
                    message = False
                else:
                    closure = False
                    run_game = False