# Board service

from ChessEngine.images_loader import ImagesLoader
import ChessEngine.piece as Piece

import pygame

class Board():
    def __init__(self, screen : pygame.display) -> None:
        self.images : ImagesLoader = ImagesLoader()
        self.screen: pygame.display = screen

        #* Koordynaty
        self.letters : dict[str:int] = {'a':0, 'b':100, 'c':200, 'd':300, 'e':400, 'f':500, 'g':600, 'h':700}
        self.numbers : dict[str:int] = {str(num) : pos for num, pos in zip(range(1, 9),range(700,-100, -100))}
        
        #* plansza {a1 : [(x_pos, y_pos), (piece, color)|None]}
        self.board : dict[str: list[tuple|None]] = {letter + number: [(self.letters[letter], self.numbers[number]), None] for \
                      letter in self.letters.keys() for number in self.numbers.keys()}

        #* Ustawienie gornego gracza
        self.board['a8'][1] = (Piece.Rook(0, 0, self.images.BLACK_PIECES['rook']), "black")
        self.board['b8'][1] = (Piece.Knight(100, 0, self.images.BLACK_PIECES['knight']), "black")
        self.board['c8'][1] = (Piece.Bishop(200, 0, self.images.BLACK_PIECES['bishop']), "black")
        self.board['d8'][1] = (Piece.Queen(300, 0, self.images.BLACK_PIECES['queen']), "black")
        self.board['e8'][1] = (Piece.King(400, 0, self.images.BLACK_PIECES['king']), "black")
        self.board['f8'][1] = (Piece.Bishop(500, 0, self.images.BLACK_PIECES['bishop']), "black")
        self.board['g8'][1] = (Piece.Knight(600, 0, self.images.BLACK_PIECES['knight']), "black")
        self.board['h8'][1] = (Piece.Rook(700, 0, self.images.BLACK_PIECES['rook']), "black")

        for letter, x in zip(self.letters, range(0, 800, 100)):
            self.board[letter + '7'][1] = (Piece.BlackPawn(x, 100, self.images.BLACK_PIECES['pawn']), "black")

        #* Ustawienie dolnego gracza
        self.board['a1'][1] = (Piece.Rook(0, 700, self.images.WHITE_PIECES['rook']), "white")
        self.board['b1'][1] = (Piece.Knight(100, 700, self.images.WHITE_PIECES['knight']), "white")
        self.board['c1'][1] = (Piece.Bishop(200, 700, self.images.WHITE_PIECES['bishop']), "white")
        self.board['d1'][1] = (Piece.Queen(300, 700, self.images.WHITE_PIECES['queen']), "white")
        self.board['e1'][1] = (Piece.King(400, 700, self.images.WHITE_PIECES['king']), "white")
        self.board['f1'][1] = (Piece.Bishop(500, 700, self.images.WHITE_PIECES['bishop']), "white")
        self.board['g1'][1] = (Piece.Knight(600, 700, self.images.WHITE_PIECES['knight']), "white")
        self.board['h1'][1] = (Piece.Rook(700, 700, self.images.WHITE_PIECES['rook']), "white")

        for letter, x in zip(self.letters, range(0, 800, 100)):
            self.board[letter + '2'][1] = (Piece.WhitePawn(x, 600, self.images.WHITE_PIECES['pawn']), "white")

    #* Rysowanie planszy
    def draw_board(self) -> None:
        self.screen.blit(self.images.BOARD, (0,0))

    #* Rysowanie bierek
    def draw_pieces(self) -> None:
        for _, piece in self.board.values():
            if piece:
                piece[0].draw(self.screen)

    #* Zwraca bierke na polu x, y
    def get_piece(self, x:int, y:int) -> Piece:
        return self.board[self.get_field(x, y)][1][0]

    #* Zwraca oznaczenie pola np a1, a2, ... w zaleznosci od wspolrzednych
    def get_field(self, x:int, y:int) -> str:
        if 0 <= x < 100:
            letter = 'a'
        elif 100 <= x < 200:
            letter = 'b'
        elif 200 <= x < 300:
            letter = 'c'
        elif 300 <= x < 400:
            letter = 'd'
        elif 400 <= x < 500:
            letter = 'e'
        elif 500 <= x < 600:
            letter = 'f'
        elif 600 <= x < 700:
            letter = 'g'
        elif 700 <= x <= 800:
            letter = 'h'
        else:
            raise IndexError("Out of bounds mouse click!")

        if 0 <= y < 100:
            number = '8'
        elif 100 <= y < 200:
            number = '7'
        elif 200 <= y < 300:
            number = '6'
        elif 300 <= y < 400:
            number = '5'
        elif 400 <= y < 500:
            number = '4'
        elif 500 <= y < 600:
            number = '3'
        elif 600 <= y < 700:
            number = '2'
        elif 700 <= y <= 800:
            number = '1'
        else:
            raise IndexError("Out of bounds mouse click!")
        return letter + number

    #* Zwraca kolor bierki na polu
    def get_piece_color(self, x:int, y:int) -> str | None:
        if self.board[self.get_field(x, y)][1]:
            return self.board[self.get_field(x, y)][1][1]
        return None
        
    def highlight_field(self, x:int, y:int) -> None:
        highlight_color = (255, 255, 0) # zolty
        field_size = 102
        x, y = self.board[self.get_field(x, y)][0]

        highlight_surface = pygame.Surface((field_size, field_size))
        highlight_surface.fill(highlight_color)
        highlight_surface.set_alpha(128) # przezroczystosc
        self.screen.blit(highlight_surface, (x, y))
    
    def highlight_possible_move(self, field:str) -> None:
        highlight_color = (192,192,192, 100) # szary
        field_size = 102
        x, y = self.board[field][0]
        center_x, center_y = x + field_size // 2 - field_size // 5, y + field_size // 2 - field_size // 5
        
        highlight_surface = pygame.Surface((field_size, field_size), pygame.SRCALPHA)
        pygame.draw.circle(highlight_surface, highlight_color, (field_size // 5, field_size // 5), field_size // 5)
        self.screen.blit(highlight_surface, (center_x,  center_y))

    def is_free(self, field: str) -> bool:
        return self.board is None
    
    def move_piece(self, prev_field:str, to_field:str) -> None: #todo zwraca zbita bierke
        #* specjalna obsluga piona
        if isinstance(self.board[prev_field][1][0], Piece.WhitePawn) or isinstance(self.board[prev_field][1][0], Piece.BlackPawn):
            self.board[prev_field][1][0].first_move = False
        self.board[to_field][1] = self.board[prev_field][1]
        x,y = self.board[to_field][0]
        self.board[to_field][1][0].change_pos(x,y)
        self.board[prev_field][1] = None

def draw_window(board: pygame.display, highlight_field:bool, x:int, y:int, piece:Piece) -> None:
    board.draw_board()
    if highlight_field:
        board.highlight_field(x,y) 
    board.draw_pieces()
    if piece:
        for field in piece.get_possible_moves(board.get_field(x,y)):
            board.highlight_possible_move(field)

