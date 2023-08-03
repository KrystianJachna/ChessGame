# Game Logic

import pygame
from ChessEngine.board import Board
from ChessEngine.piece import  Piece
from ChessEngine.images_loader import ImagesLoader

def main():
    #* Inicjalizacja PYGAME
    pygame.init()

    #* Stale
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
    FPS = 60

    #* Utworzenie okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #* Wczytanie planszy i bierek
    images = ImagesLoader()

    #* Utworzenie planszy
    board = Board()

    #* Glowna petla gry
    clock = pygame.time.Clock()
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #todo ruchy graczy

        #todo logika gry
        #todo sprawdzanie stanu gry (szach, mat, pat, ...)
        
        #todo rysowanie planszy i figur
        board.draw_board(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    
if __name__ == "__main__":
    main()
