import pygame

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

def draw(win):
    #Background
    win.fill((255,255,255))

    #Grid
    thickness = 8
    pygame.draw.line(win, (0,0,0), (WIDTH/3,0), (WIDTH/3, HEIGHT), thickness)
    pygame.draw.line(win, (0,0,0), (2*WIDTH/3,0), (2*WIDTH/3, HEIGHT), thickness)

    pygame.draw.line(win, (0,0,0), (0,WIDTH/3), (HEIGHT, WIDTH/3), thickness)
    pygame.draw.line(win, (0,0,0), (0,2*WIDTH/3), (HEIGHT, 2*WIDTH/3), thickness)

    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw(win)

main()