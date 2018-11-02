import pygame
import random
import os


def criaimg(x,y,tesouro):
    screen.blit(tesouro,(x,y))

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


#Matriz
pontos = 0
vida = 400
contadorTesouro = 0
contadorMimico = 0
coisasMatriz = [0,8,9]

#Deixa a matriz aleatória
random.shuffle(matrizPredef)

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
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Treasure Hunt")
screen.fill(white)

#Textos
fonte = pygame.font.SysFont("Arial",50)
gameOver = fonte.render("Fim de Jogo",False,(0,0,0))
vitoria = fonte.render("Você ganhou",False,(0,0,0))
textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",False,(0,0,0))

print(matrizPredef)

#Jogo
while sair == True:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            sair = False
        
        screen.fill(white)
        pygame.draw.rect(screen,blue,(0,0,503,503),0)

        if(evento.type == pygame.MOUSEBUTTONUP):#Mouse clique
            x, y = pygame.mouse.get_pos()
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
                    
        #Grade verde
        for i in range(0,5):
            for j in range (0,5):
                if matriz[i][j] == -1:
                    pygame.draw.rect(screen,green,(i*100,j*100,100,100),0)
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                elif (matriz[i][j] == 8):
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(tesouro,(i*108,j*110))
                elif (matriz[i][j] == 9):
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(mimico,(i*100,j*100))
                else:
                    pygame.draw.rect(screen,black,(i*100,j*100,100,100),1)
                    screen.blit(imgnum[matriz[i][j]],(i*100,j*100))
        
    if vida == 400:
        pygame.draw.rect(screen,green,(50,505,399,24),0)
    elif vida == 300:
        pygame.draw.rect(screen,gray,(50,505,399,24),0)
        pygame.draw.rect(screen,green,(50,505,299,24),0)
    elif vida == 200:
        pygame.draw.rect(screen,gray,(50,505,399,24),0)
        pygame.draw.rect(screen,green,(50,505,199,24),0)
    elif vida == 100:
        pygame.draw.rect(screen,gray,(50,505,399,24),0)
        pygame.draw.rect(screen,green,(50,505,99,24),0)
            
    pygame.draw.rect(screen,black,(50,505,400,25),1)
    screen.blit(tesouro, (520,20))
    screen.blit(mimico, (520,100))
    pygame.display.update()

    print(pontos)
    if contadorTesouro == 6:
        textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",True,(0,0,0))
        screen.blit(vitoria,(100,525))
        screen.blit(textoPontos,(100,580))
        pygame.display.update()
        pygame.time.wait(3000)
        break
    if vida == 0:
        textoPontos = fonte.render("Você fez " + str(pontos) + " pontos",True,(0,0,0))
        pygame.draw.rect(screen,gray,(50,505,399,24),0)
        screen.blit(gameOver,(100,525))
        screen.blit(textoPontos,(100,580))
        pygame.display.update()
        pygame.time.wait(3000)
        break
    
pygame.quit()
