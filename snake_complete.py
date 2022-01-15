import pygame
import time
import random
from datetime import datetime

# todo criar menu de opcoes de jogo

pygame.init()


amarelo = (255, 255, 102)
branco = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
preto = (0, 0, 0, 0)

dis_width, dis_height = 500, 1000 #largura, altura


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('VERME')

clock = pygame.time.Clock()

snake_block = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 20)


# todo padronizar para todas as telas
def pontos(score):
    value = score_font.render(f"Pontos {score}", True, amarelo)
    dis.blit(value, [0, 0])



def our_snake(snake_block, snake_list, cor):
    for x in snake_list:
        pygame.draw.rect(dis, cor, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    cor_verme = [225, 255, 255]

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 15
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    print(foody, foodx)
    while not game_over:
        while game_close == True:

            dis.fill(preto)
            message('Obrigado por Jogar! press ENTER', red)

            pontos(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                print(event.type)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.type == 768:
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = False
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

        #  MORTE NA PAREDE
        # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #     game_close = True

        # jogo infinito
        if x1 >= dis_width:
            x1 = 0
        if y1 >= dis_height:
            y1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 < 0:
            y1 = dis_height


        dis.fill(preto)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # morte no corpo
        # for x in snake_List[:-1]:
        #     if x == snake_Head:
        #         game_close = True

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
