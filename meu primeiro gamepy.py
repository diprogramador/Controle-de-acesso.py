import pygame

def main():         #cria janela
    #As definições dos objetos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 450]) #VARIAVEL QUE MUDA TAMANHO DA JANELA
    pygame.display.set_caption("Jogo Iniciante") #titulo da janela
    relogio = pygame.time.Clock()#VARIAVEL QUE A PAGINA ATUALIZA EM FLAMES
    cor_branca = (255,255,255)#VARIAVEL QUE DEFINE COR DE FUNDO DA JANELA
    cor_azul = (108, 194, 236)#VARIAVEL DE COR DO OBJETO
    cor_verde = (54, 182, 112)#VARIAVEL DE COR DO OBJETO
    cor_vermelha = (227, 57, 9)#VARIAVEL DE COR DO OBJETO
    cor_rosa = (253, 147, 226)#VARIAVEL DE COR DO OBJETO
    sup = pygame.Surface((600, 450))#define o tamanho do objeto
    sup.fill(cor_azul)#define a cor do objeto (---+--- OBJETO 1 ---+---)

   

    ret = pygame.Rect(10, 10, 30, 30)#VARIAVEL RETÂNGULO
    ret2 = pygame.Rect(10, 40, 560, 20)#VARIAVEL RETÂNGULO

    pygame.font.init() #CHAVE PARA INICIAR AS FONTES

    font_padrao = pygame.font.get_default_font() #variaveis de textos que aparecerão quando colidir objetos
    fonte_perdeu = pygame.font.SysFont(font_padrao,45)
    fonte_ganhou = pygame.font.SysFont(font_padrao,30)

    audio_explosao = pygame.mixer.Sound("boom1.ogg")#VARIAVEL DO SOM DA EXPLOSAO
    
    
    #---------+-----------------+-------------+--------------------+------#
    
    sair = False    #VARIAVEL QUE FAZ COM QUE O BOTÃO X DA JANELA FECHE A JANELA

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #MODULO QUE FAZ O X DA JANELA FECHA-LA
                sair = True
                
                
            #if event.type == pygame.MOUSEBUTTONDOWN:        #O MOUSE CONTROLA  OBJETO
                #ret = ret.move(10, 10)                      #DEFINE DIREÇÃO QUE O OBJETO IRA SE MOVER
                

            #if event.type == pygame.MOUSEMOTION:         #SO EM MECHER COM O MOUSE, MECHE O OBJETO
                #ret = ret.move(-10, -10)                 #DEFINE EM X & Y A DIREÇÃO
                    


                
        relogio.tick(30)#JANELA ATUALIZA FLAMES POR SEGUNDOS(Maior o valor, o objeto segue mouse mais rapido)
        tela.fill(cor_branca)#COR DE FUNDO DA JANELA
        tela.blit(sup, [0, 0])#Define a distancia X & Y do objeto
                
        (xant, yant) = (ret.left, ret.top)#COLIZÃO COM OUTRO OBJETO
        (ret.left, ret.top) = pygame.mouse.get_pos()#OBJETO MECHE JUNTO COM O MOUSE
        ret.left -= ret.width/2#CENTRALIZA O MOUSE NO OBJETO
        ret.top -= ret.height/2#CENTRALIZA O MOUSE NO OBJETO
        if ret.colliderect(ret2):#COLISÃO COM OUTRO OBJETO
            text = fonte_perdeu.render('BATEU A NAVE!!!', 1, (255,255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.10)#VOLUME DO SOOM DA EXPLOSÃO
            tela.blit(text, (150, 150))#TEXTO APARECE NA ALTURA DECLARADA QUANDO COLIDIR NOS OBJETOS
            (ret.left, ret.top) = (xant, yant)#COLIZÃO COM OUTRO OBJETO
            
        
        pygame.draw.rect(tela, cor_vermelha, ret)#DEFINE COR E LOCAL DO OBJETO NA TELA
        pygame.draw.rect(tela, cor_rosa, ret2)#DEFINE COR E LOCAL DO OBJETO NA TELA
        pygame.display.update()#atualiza a janela
        
    pygame.quit() 


main()
    
    
