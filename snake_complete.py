import pygame
import time
import random
from datetime import datetime
import funks

# todo criar menu de opcoes de jogo

pygame.init()


amarelo = (255, 255, 102)
branco = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
preto = (0, 0, 0, 0)

dis_width, dis_height = 500, 1000 #largura, altura


tela = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('VERME')

clock = pygame.time.Clock()

snake_block = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 20)


# todo padronizar para todas as telas
def pontos(score):
    value = score_font.render(f"Pontos {score}", True, amarelo)
    tela.blit(value, [0, 0])



def our_snake(snake_block, snake_list, cor):
    for x in snake_list:
        pygame.draw.rect(tela, cor, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    tela.blit(mesg, [dis_width / 6, dis_height / 3])



game_close = False

def gameLoop():
    game_over = False
    global game_close
    game_close = True

    cor_verme = [225, 255, 255]

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    parede_on = False
    corpo_on = True
    snake_List = []
    Length_of_snake = 1
    snake_speed = 15
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    print(foody, foodx)
    while not game_over:
        while game_close == True:
            mouse_pos = pygame.mouse.get_pos()
            tela.fill(preto)
            funks.texto('Obrigado por Jogar! press ENTER', (5, 150), tela, cor=amarelo)
            funks.texto('ENTER para continuar!', (15, 175), tela, cor=amarelo)
            funks.texto('Q para voltar ao menu!', (25, 200), tela, cor=amarelo)

            parede = funks.texto(f'Parede = {"On" if parede_on else "Off"}', (250, 500 - 70), tela, cor=amarelo)
            if parede.top < mouse_pos[1] < parede.bottom and parede.left < mouse_pos[0] < parede.right:
                parede = funks.texto(f'Parede = {"On" if parede_on else "Off"}', (250, 500 - 70), tela, cor=amarelo)

            corpo = funks.texto(f'Corpo Transparente = {"On" if corpo_on else "Off"}', (250, 500 - 100), tela, cor=amarelo)
            if corpo.top < mouse_pos[1] < corpo.bottom and corpo.left < mouse_pos[0] < corpo.right:
                corpo = funks.texto(f'Corpo Transparente = {"On" if corpo_on else "Off"}', (250, 500 - 100), tela, cor=amarelo)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if parede.top < mouse_pos[1] < parede.bottom and parede.left < mouse_pos[0] < parede.right:
                        if not parede_on:
                            parede_on = True
                        else:
                            parede_on = False
                    if corpo.top < mouse_pos[1] < corpo.bottom and corpo.left < mouse_pos[0] < corpo.right:
                        if corpo_on:
                            corpo_on = False
                        else:
                            corpo_on = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    if event.key == pygame.K_RETURN:
                        game_close = False







        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                if event.key == pygame.K_LEFT and not x1_change == snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and not x1_change == -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and not y1_change == snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and not y1_change == -snake_block:
                    y1_change = snake_block
                    x1_change = 0
            # print(event)  #
        x1 += x1_change
        y1 += y1_change

        if parede_on == True:
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

        # jogo infinito
        if x1 >= dis_width:
            x1 = 0
        if y1 >= dis_height:
            y1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 < 0:
            y1 = dis_height


        tela.fill(preto)

        pygame.draw.rect(tela, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if not corpo_on:
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

        our_snake(snake_block, snake_List, cor_verme)
        pontos(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # print(foody, foodx)
            Length_of_snake += 1
            snake_speed += 1
            if cor_verme[1] > 5:
                cor_verme[1] -= 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
