import pygame
pygame.font.init()

#-----------------------------------------[TEMP]-------------------------------------------

from game import Game

lmao = Game()

#------------------------------------------------------------------------------------------

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

def click(pos):
    x = int(pos[0]/(WIDTH/3)) 
    y = int(pos[1]/(WIDTH/3))

    if lmao.turn % 2 == 1:
        lmao.play('x', (x,y))
    else:
        lmao.play('o', (x,y))

def draw(win):
    #Background
    win.fill((255,255,255))

    #Grid
    thickness = 8
    pygame.draw.line(win, (0,0,0), (WIDTH/3,0), (WIDTH/3, HEIGHT), thickness)
    pygame.draw.line(win, (0,0,0), (2*WIDTH/3,0), (2*WIDTH/3, HEIGHT), thickness)

    pygame.draw.line(win, (0,0,0), (0,WIDTH/3), (HEIGHT, WIDTH/3), thickness)
    pygame.draw.line(win, (0,0,0), (0,2*WIDTH/3), (HEIGHT, 2*WIDTH/3), thickness)

    #Shapes
    font = pygame.font.SysFont("comicsansms", 50)
    texta = font.render("x", 1, (0,0,0))
    textb = font.render("o", 1, (0,0,0))
    for i in range(3):
        for j in range(3):
            if lmao.grid[i][j] == 'x':
                win.blit(texta, (i * (WIDTH/3) + WIDTH/6 - texta.get_width()/2, j * (HEIGHT/3) + HEIGHT/6 - texta.get_height()/2))
            elif lmao.grid[i][j] == 'o':
                win.blit(textb, (i * (WIDTH/3) + WIDTH/6 - textb.get_width()/2, j * (HEIGHT/3) + HEIGHT/6 - textb.get_height()/2))
            else:
                pass

    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click(pos)

        draw(win)

main()