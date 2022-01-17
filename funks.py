import pygame as py



py.init()

#cores
branco = (255, 255, 255)
preto = (0, 0, 0, 0)
red = (213, 50, 80)
verde = (0, 255, 0)
azul = (0,0,255)
vermelho = (255,0,0)
amarelo = (255, 255, 102)


#fontes

arial = py.font.SysFont("arial", 20)
font_style = py.font.SysFont("bahnschrift", 25)


#funcao de impressao de texto
def texto(txt, pos, tela, font=arial,cor=branco):
    '''
                            recebe os parametros para criar uma caixa de txt na tela
                              e returna o objeto para tratamento
    :param font: font para ser redenrizada
    :param txt: texto a ser imprimido
    :param pos: posicionamento da caixa de txt na tela
    :param tela: tela que ira mostar o txt
    :param cor: cor do txt
    :return: o objeto para manipulacao e interacao com o usuario
    '''
    texto = font.render(txt, True, cor)
    ret = tela.blit(texto, pos)
    return ret


# width, height = 500, 1000
def tela(caption, tamanho=(500, 1000)):

    tela = py.display.set_mode(tamanho)
    py.display.set_caption(caption)
    return tela

