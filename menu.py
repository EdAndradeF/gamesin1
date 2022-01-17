import pygame as py
import funks

py.init()

preto = 0, 0, 0
branco = 255, 255, 255
verde = 0, 255, 0

width, height = 500, 1000
tela = py.display.set_mode((width, height))

fonte_padrao = py.font.SysFont('Arial', 30)


# todo feito **padronizar funcao para todas as telas**
def texto(txt, pos, cor=branco):
        #ler documentacao em funks.py
    texto = fonte_padrao.render(txt, True, cor)
    ret = tela.blit(texto, pos)
    return ret


def jogo(): #Funcao para iniciar a tela inicial do jogo

    importado_i3 = False
    importado_sc = False
    corfundo = preto
    play = True

    while True:

        while play:
            tela.fill(corfundo)
            #  pinta o fundo
            mouse_pos = py.mouse.get_pos()
            # mouse_pos[0] == altura ||| mouse_pos[1] == largura

            # botao para fechar o jogo
            saida = texto('Quit', (width / 2, height / 2))
            if saida.top < mouse_pos[1] < saida.bottom and saida.left < mouse_pos[0] < saida.right:
                saida = texto('Quit', (width / 2, height / 2), verde)

            # botao do jogo Snake
            cobra = texto('Snake', (width / 2, (height / 2) - 35))
            if cobra.top < mouse_pos[1] < cobra.bottom and cobra.left < mouse_pos[0] < cobra.right:
                cobra = texto('Snake', ((width / 2), (height / 2) - 35), verde)

            # botao do jogo Indie 3000
            indie = texto('Indie 3000', (width / 2, (height / 2) - 70))
            if indie.top < mouse_pos[1] < indie.bottom and indie.left < mouse_pos[0] < indie.right:
                indie = texto('Indie 3000', (width / 2, (height / 2) - 70), verde)

                    #todo funcionalizar EVENTOS DE COMANDOS
            for event in py.event.get():
                if event.type == py.QUIT:
                    play = False
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        play = False

                if event.type == py.MOUSEBUTTONDOWN:
                        # VOLTA PARA AREA DE TRABALHO
                    if saida.top < mouse_pos[1] < saida.bottom and saida.left < mouse_pos[0] < saida.right:
                        play = False

                        #  PLAY SNAKE GAME
                    if cobra.top < mouse_pos[1] < cobra.bottom and cobra.left < mouse_pos[0] < cobra.right:
                         #   importa e roda o jogo Snake,
                        if not importado_sc:
                            import snake_complete as sc
                            importado_sc = True
                        else:
                            sc.gameLoop()
                            jogo()

                        # PLAY INDIE 3000
                    if indie.top < mouse_pos[1] < indie.bottom and indie.left < mouse_pos[0] < indie.right:
                        # importa e roda o jogo Indie 3000
                        if not importado_i3:
                            import indie_3000 as i3
                            importado_i3 = True
                        else:
                            i3.game_loop()
                            jogo()

            py.display.flip()

        py.quit()
        quit()



jogo()
