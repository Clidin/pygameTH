import pygame
import random
import os

#Matriz cópia
matriz = [[-1 for x in range (5)] for y in range (5)]

#Matriz predefinida | 0 = número | 8 = tesouro | 9 = mimico
matrizPredef = [[0, 8, 9, 0, 0], [0, 8, 0, 9, 0], [9, 0, 0, 8, 0], [0, 8, 0, 9, 0], [8, 0, 8, 9, 0]]

pygame.init()

sair = True

#Imagens
tesouro = pygame.image.load(os.path.join('tesouro.png'))
mimico = pygame.image.load(os.path.join('mimic.png'))
num0 = pygame.image.load(os.path.join('numero0.png'))
num1 = pygame.image.load(os.path.join('numero1.png'))
num2 = pygame.image.load(os.path.join('numero2.png'))
num3 = pygame.image.load(os.path.join('numero3.png'))
num4 = pygame.image.load(os.path.join('numero4.png'))

imgnum = [num0,num1,num2,num3,num4]

#Cores RGB
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (128,128,128)
cores = [white,black,green,blue,gray]


#Valores
pontos = 0
vida = 400
contadorTesouro = 0
contadorMimico = 0
coisasMatriz = [0,8,9]

#Deixa a matriz aleatória
random.shuffle(matrizPredef)

#Detecta e define quantos tesouros estão próximos de números
for i in range(len(matrizPredef)):
    for j in range(len(matrizPredef[i])):
        if matrizPredef[i][j] not in [8,9]:
            contador = 0
            if i != 0:
                if matrizPredef[i-1][j] == 8:
                    contador += 1
            if i != len(matrizPredef)-1:
                if matrizPredef[i+1][j] == 8:
                    contador += 1
            if j != 0:
                if matrizPredef[i][j-1] == 8:
                    contador += 1
            if j != len(matrizPredef[i])-1:
                if matrizPredef[i][j+1] == 8:
                    contador += 1
            matrizPredef[i][j] = contador

#Tela
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Treasure Hunt")
screen.fill(white)

#Textos
fonte = pygame.font.SysFont("Arial",40)
gameOver = fonte.render("Fim de Jogo",False,(0,0,0))
vitoria = fonte.render("Você ganhou",False,(0,0,0))
textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",False,(0,0,0))
textoVida = fonte.render("Vida",False,(0,0,0))
legendaTesouro = fonte.render("Tesouro",False,(0,0,0))
legendaTesouropontos = fonte.render("100 pontos",False,(0,0,0))
legendaMimico = fonte.render("Bomba",False,(0,0,0))
legendaMimicovida = fonte.render("-100 vida",False,(0,0,0))
tituloJogo1 = fonte.render("Caça",False,(0,0,0))
tituloJogo2 = fonte.render("ao",False,(0,0,0))
tituloJogo3 = fonte.render("Tesouro",False,(0,0,0))
divisaoTitulos = fonte.render("_________",False,(0,0,0))

#Imprime o "gabarito" no Shell      
print(matrizPredef)

#Jogo
while sair == True:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            sair = False
        
        screen.fill(white)
                         
        #Clique do mouse
        if(evento.type == pygame.MOUSEBUTTONUP):
            x, y = pygame.mouse.get_pos()
            
            #Como ignorar o clique fora da área da matriz?
            #Como ignorar clique em uma área que já foi escolhida?
            
            #Função pra quando clicar dentro da matriz
            if (x or y) or (x and y) <= 500:
                x = x//100
                y = y//100
                matriz[x][y] = matrizPredef[y][x]
            if matriz[x][y] == 8:
                contadorTesouro += 1
                pontos = pontos + 100

            elif matriz[x][y] == 9:
                contadorMimico += 1
                if vida > 0:
                    vida = vida - 100
                    
        #Criar os blocos corretos
        for i in range(0,5):
            for j in range (0,5):
                         
                #Bloco verde com contorno preto
                if matriz[i][j] == -1:
                    pygame.draw.rect(screen,green,(i*100,j*100,100,100),0)
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                         
                #Tesouro quando encontrado
                elif (matriz[i][j] == 8):
                    pygame.draw.rect(screen,blue,(i*100,j*100,100,100),0)
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(tesouro,(i*108,j*110))
                         
                #Mimico quando encontrado
                elif (matriz[i][j] == 9):
                    pygame.draw.rect(screen,blue,(i*100,j*100,100,100),0)
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(mimico,(i*100,j*100))
                         
                #Numero quando encontrado
                else:
                    pygame.draw.rect(screen,blue,(i*100,j*100,100,100),0)
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(imgnum[matriz[i][j]],(i*100,j*100))
                    
    #Barra de vida
    if vida == 400:
        pygame.draw.rect(screen,green,(50,548,399,24),0)
    elif vida == 300:
        pygame.draw.rect(screen,gray,(50,548,399,24),0)
        pygame.draw.rect(screen,green,(50,548,299,24),0)
    elif vida == 200:
        pygame.draw.rect(screen,gray,(50,548,399,24),0)
        pygame.draw.rect(screen,green,(50,548,199,24),0)
    elif vida == 100:
        pygame.draw.rect(screen,gray,(50,548,399,24),0)
        pygame.draw.rect(screen,green,(50,548,99,24),0)

    screen.blit(textoVida,(212,502))
    
    #Contorno barra de vida
    pygame.draw.rect(screen,black,(50,548,400,25),1)
    pygame.draw.rect(screen,black,(50,548,300,25),1)
    pygame.draw.rect(screen,black,(50,548,200,25),1)
    pygame.draw.rect(screen,black,(50,548,100,25),1)

    #Titulo
    screen.blit(tituloJogo1,(555,3))
    screen.blit(tituloJogo2,(580,46))
    screen.blit(tituloJogo3,(530,89))
    screen.blit(divisaoTitulos,(503,114))#Separa os titulos
    
    #Legendas
    screen.blit(legendaTesouro,(530,175))
    screen.blit(legendaTesouropontos,(504,218))
    screen.blit(divisaoTitulos,(503,245))#Separa as legendas
    screen.blit(legendaMimico,(530,304))
    screen.blit(legendaMimicovida,(506,347))
    screen.blit(divisaoTitulos,(503,245))
    screen.blit(divisaoTitulos,(503,370))
               
    pygame.display.update()

    #Vitória | Acaba o jogo
    if contadorTesouro == 6:
        textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",True,(0,0,0))
        screen.blit(vitoria,(100,568))
        screen.blit(textoPontos,(100,623))
        pygame.display.update()
        pygame.time.wait(3000)
        break

    #Derrota | Acaba o jogo
    if vida == 0:
        textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",True,(0,0,0))
        pygame.draw.rect(screen,gray,(50,548,399,24),0)
        screen.blit(gameOver,(100,568))
        screen.blit(textoPontos,(100,623))
        pygame.display.update()
        pygame.time.wait(3000)
        break
    
pygame.quit()
