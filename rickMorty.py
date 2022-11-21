import pygame
import random
import time
import sys  
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("RICK AND MORTY")
altura = 1080
largura = 1920
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load("assets/fundoRick2.jpg")
iron = pygame.image.load("assets/rickFoda.png")
missile = pygame.image.load("assets/missile.png")

  
  

res = (1920,1080)  
screen = pygame.display.set_mode(res)  
color = (255,255,255)  
color_light = (170,170,170)  
color_dark = (100,100,100)  
width = screen.get_width()  
height = screen.get_height()  
smallfont = pygame.font.SysFont('Corbel',35)  
text = smallfont.render('quit' , True , color)  

loginNome = input("Digite seu Nome: ")
loginEmail = input("Digite seu Email: ")
  
while True:  
      
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:  
            pygame.quit()  
            
        if ev.type == pygame.MOUSEBUTTONDOWN:  
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                    pygame.quit()
                      
                  
    
    screen.fill((60,25,60))  
      
    
    
    mouse = pygame.mouse.get_pos()  
      
    
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])  
          
    else:  
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])  
      
    
    screen.blit(text , (width/2+50,height/2))
    break  


def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("GAME OVER!",True,preto)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (650,250))
    gameDisplay.blit(textoDisplay2, (670,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    ironX = 780
    ironY = 700
    movimentoIronX = 0
    larguraIron = 250
    alturaIron = 352
    alturaMissile = 250
    larguraMissile = 50
    posicaoMissileX = 400
    posicaoMissileY = -240
    velocidadeMissile = 1
    pontos = 0
    pygame.mixer.music.load("assets/temaRick.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

    morteSound = pygame.mixer.Sound("assets/morteRick.wav")
    morteSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoIronX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoIronX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoIronX = 0
            
        if jogando:
            if posicaoMissileY > altura:
                posicaoMissileY = -240
                posicaoMissileX = random.randint(0,largura)
                velocidadeMissile = velocidadeMissile + 1
                pontos = pontos + 1
                pygame.mixer.Sound.play(missileSound)
            else:
                posicaoMissileY =posicaoMissileY + velocidadeMissile

            if ironX + movimentoIronX >0 and ironX + movimentoIronX< largura-larguraIron:
                ironX = ironX + movimentoIronX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(iron, (ironX,ironY))
            
            gameDisplay.blit(missile, (posicaoMissileX,posicaoMissileY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXIron = list(range(ironX, ironX+larguraIron))
            pixelsYIron = list(range(ironY, ironY+alturaIron))

            pixelXMissile = list(range(posicaoMissileX, posicaoMissileX+larguraMissile))
            pixelYMissile = list(range(posicaoMissileY, posicaoMissileY+alturaMissile))

            colisaoY = len(list(set(pixelYMissile) & set(pixelsYIron) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMissile) & set(pixelsXIron) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(morteSound)


        pygameDisplay.update()
        clock.tick(60)

jogar()

