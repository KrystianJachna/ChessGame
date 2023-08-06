# Game Logic

import pygame
from ChessEngine.board import Board, draw_window
from ChessEngine.piece import  Piece
from ChessEngine.images_loader import ImagesLoader

def main():
    #* Inicjalizacja PYGAME
    pygame.init()
    pygame.display.set_caption('Chess')

    #* Stale
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
    FPS = 60

    #* Utworzenie okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #* Utworzenie planszy
    board = Board(screen)

    #* Glowna petla gry
    clock = pygame.time.Clock()
    running = True
    current_player = "white"
    highlight_field = False
    x,y, piece  = None, None, None
    prev_x, prev_y = 163, 172

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(highlight_field)
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    field = board.get_field(x,y)

                    if board.get_piece_color(x, y) == current_player:
                        prev_x, prev_y = x, y
                        highlight_field = True
                        piece = board.get_piece(x, y)
                    elif highlight_field and field in\
                          board.get_piece(prev_x,prev_y).get_possible_moves(board.get_field(prev_x, prev_y), board)[0] \
                          or field in board.get_piece(prev_x,prev_y).get_possible_moves(board.get_field(prev_x, prev_y), board)[1]:
                        board.move_piece(board.get_field(prev_x, prev_y), board.get_field(x,y))
                        highlight_field = False
                        current_player = "white" if current_player == "black" else "black"
                        piece = None
                        prev_x, prev_y = x,y

                    else:   
                        highlight_field = False
                        piece = None
        #todo logika gry
        #todo sprawdzanie stanu gry (szach, mat, pat, ...)
        #* Wyswietlanie
        draw_window(board, highlight_field, x, y, piece)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    
if __name__ == "__main__":
    main()
