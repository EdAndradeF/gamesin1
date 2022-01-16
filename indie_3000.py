import random as rd

import pygame as py
import funks



py.init()

branco = (255, 255, 255)
preto = (0, 0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 102)
cinza = (50, 50, 50)
rosa = (255, 0, 255)


class Carro:
    def __init__(self, cor, pos_h, pos_v=0):
        self.h, self.v = pos_h, pos_v
        self.corpo = (50, 100)
        self.roda = (10, 20)
        self.roda_p = ((0, 5),
                       (40, 5),
                       (0, 75),
                       (40, 75))
        self.cor = cor
        self.hit = py.Rect


    def desenho(self, r_cor=preto):
        self.hit = py.draw.rect(dis, self.cor, ((self.h, self.v), self.corpo))
        for roda_pos in self.roda_p:
            if self.roda_p.index(roda_pos) <= 2:
                py.draw.rect(dis, r_cor, ((self.h+roda_pos[0], self.v + roda_pos[1]), self.roda))
            else:
                py.draw.rect(dis, r_cor, ((self.h+roda_pos[0], self.v + roda_pos[1]), self.roda))


class Player(Carro):
    def __init__(self, cor, pos_h=200, pos_v=800):
        super().__init__(cor, pos_h, pos_v)
        self.veloc = (self.v // -100) * 5


    def mover(self, event):

        if event.key == py.K_LEFT and self.h > 0:
            self.h -= 50
        elif event.key == py.K_RIGHT and self.h < 450:
            self.h += 50
        elif event.key == py.K_UP and self.v > 0:
            self.v -= 100

        elif event.key == py.K_DOWN and self.v < 900:
            self.v += 100



class Bot(Carro):

    def __init__(self, cor, pos_v=-100):
        super().__init__(cor, pos_v)
        self.acele = 1
        self.h = rd.randrange(0, 500, 50)

    def movimento(self):
        self.v += 1




dis = funks.tela('Indie 3000')

clock = py.time.Clock()






def game_loop():
    p1 = Player(rosa, 200, 800)
    tx_count = 0
    lista_taxi = []
    velocidade = 100
    fps = ((p1.v // -100) * 5) + velocidade
    game_close = False
    game_over = False
    pontos = 0
    while not game_over:
        while game_close == True:

            dis.fill(preto)
            funks.texto('Obrigado por Jogar! press ENTER', (5, 150), dis, cor=amarelo)
            funks.texto('ENTER para continuar!', (15, 175), dis, cor=amarelo)
            funks.texto('Q para voltar ao menu!', (25, 200), dis, cor=amarelo)

            py.display.update()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        return
                    if event.key == py.K_RETURN:
                        game_loop()



        dis.fill(preto)
        if tx_count > 100:
            lista_taxi.append(Bot(amarelo))
            tx_count = 0
        tx_count += 1


        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    game_close = True
                if event.type == 13:
                    return

                p1.mover(event)
        fps = ((p1.v // -100) * 5) + velocidade
        print((p1.v // -100) * 5)
        print(fps, '><><><', velocidade)




        p1.desenho()
        for taxi in lista_taxi:
            taxi.desenho()
            taxi.movimento()
            if taxi.hit.left >= p1.hit.left and taxi.hit.right <= p1.hit.right:
                if taxi.hit.bottom + 10 >= p1.hit.top and taxi.hit.top + 10 <= p1.hit.bottom:
                    game_close = True
            if taxi.hit.top > 1000:
                taxi.acele += 0.5
                pontos += 1
                velocidade +=2
                lista_taxi.remove(taxi)




        funks.texto(f'Pontos {pontos}', (0, 0), dis, cor=amarelo)



        py.display.update()
        clock.tick(fps)

    py.quit()
    quit()


game_loop()























