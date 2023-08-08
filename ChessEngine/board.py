# Board service

from ChessEngine.images_loader import ImagesLoader
import ChessEngine.piece as Piece
from copy import copy

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
        if self.board[self.get_field(x, y)][1]:
            return self.board[self.get_field(x, y)][1][0]
        return None
    
     #* Zwraca bierke na polu 'field'
    def get_piece_by_field(self, field : str) -> Piece:
        if self.board[field][1]:
            return self.board[field][1][0]
        return None
    

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

    #* Zwraca kolor bierki na polu x, y
    def get_piece_color(self, x:int, y:int) -> str | None:
        if self.board[self.get_field(x, y)][1]:
            return self.board[self.get_field(x, y)][1][1]
        return None
    
    #* Zwraca kolor bierki na polu x, y
    def get_piece_color_by_field(self, field:str) -> str | None:
        if self.board[field][1]:
            return self.board[field][1][1]
        return None
    
    def get_field_pos(self, field:str) -> tuple[int, int]:
        return self.board[field][0]
        
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
    
    def highlight_possible_beat(self, field:str) -> None:
        highlight_color = (169, 169, 169, 100)  # szary
        field_size = 102
        x, y = self.board[field][0]
        center_x, center_y = x + field_size // 2 - field_size // 2, y + field_size // 2 - field_size // 2

        highlight_surface = pygame.Surface((field_size, field_size), pygame.SRCALPHA)
        pygame.draw.circle(highlight_surface, highlight_color, (field_size // 2, field_size // 2), field_size // 2)

        # rysowanie mniejszego kola w celu wycieccia srodka
        inner_radius = field_size // 2 - field_size // 6
        inner_color = (0, 0, 0, 0)  
        pygame.draw.circle(highlight_surface, inner_color, (field_size // 2, field_size // 2), inner_radius)

        self.screen.blit(highlight_surface, (center_x, center_y))

    def is_free(self, field: str) -> bool:
        return self.board[field][1] is None
    
    #todo zwraca zbita bierke do wyswietlenia
    def move_piece(self, prev_field:str, to_field:str) -> str | None: 
        #* specjalna obsluga piona
        promotion_field = None
        alphabet = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        fields_to_flag_enpassant = []

        if isinstance(self.board[prev_field][1][0], Piece.WhitePawn) or isinstance(self.board[prev_field][1][0], Piece.BlackPawn):
            self.board[prev_field][1][0].first_move = False
            if to_field[1] == '8' or to_field[1] == '1':
                promotion_field = to_field
            if to_field[1] == '5' and prev_field[1] == '7' or to_field[1] == '4' and prev_field[1] == '2':
                # en passant
                current_pos = alphabet.index(to_field[0])
                fields_to_flag_enpassant = []
                type_moved_piece = type(self.board[prev_field][1][0])
                #left
                if current_pos - 1 in range(1,9) and not self.is_free(alphabet[current_pos-1] + to_field[1]):
                    moving_piece_color = self.get_piece_color_by_field(prev_field)
                    left_piece_color = self.get_piece_color_by_field(alphabet[current_pos-1] + to_field[1])
                    if moving_piece_color != left_piece_color:
                        if to_field[1] == '5':
                            fields_to_flag_enpassant.append((alphabet[current_pos-1] + to_field[1], to_field[0] + str(int(to_field[1]) + 1)))
                        else:
                            fields_to_flag_enpassant.append((alphabet[current_pos-1] + to_field[1], to_field[0] + str(int(to_field[1]) - 1)))
                #right
                if current_pos + 1 in range(1,9) and not self.is_free(alphabet[current_pos+1] + to_field[1]):
                    moving_piece_color = self.get_piece_color_by_field(prev_field)
                    left_piece_color = self.get_piece_color_by_field(alphabet[current_pos+1] + to_field[1])
                    if moving_piece_color != left_piece_color:
                        if to_field[1] == '5':
                            fields_to_flag_enpassant.append((alphabet[current_pos+1] + to_field[1], to_field[0] + str(int(to_field[1]) + 1)))
                        else:
                            fields_to_flag_enpassant.append((alphabet[current_pos+1] + to_field[1], to_field[0] + str(int(to_field[1]) - 1)))
           
            if to_field[1] == '6' or to_field[1] == '3':
                if isinstance(self.get_piece_by_field(to_field[0] + str(int(to_field[1]) - 1)), Piece.BlackPawn) and self.get_piece_color_by_field(prev_field) == 'white':
                        self.set_piece_on_field(None, to_field[0] + str(int(to_field[1]) - 1), None)
                elif isinstance(self.get_piece_by_field(to_field[0] + str(int(to_field[1]) + 1)), Piece.WhitePawn)and self.get_piece_color_by_field(prev_field) == 'black':
                    self.set_piece_on_field(None, to_field[0] + str(int(to_field[1]) + 1), None)

            
        self.board[to_field][1] = copy(self.board[prev_field][1])
        x,y = self.board[to_field][0]
        self.board[to_field][1][0].change_pos(x,y)
        self.board[prev_field][1] = None
        
        return promotion_field, fields_to_flag_enpassant
    
    def turn_off_enpassant_beatings(self, color):
        if color == 'black':
            for  _, piece in self.board.values():
                if piece:
                    if isinstance(piece[0], Piece.BlackPawn):
                        piece[0].en_passant_beatings = []
        else:
            for  _, piece in self.board.values():
                if piece:
                    if isinstance(piece[0], Piece.WhitePawn):
                        piece[0].en_passant_beatings = []
    

    def set_piece_on_field(self, piece, field: str, color: str| None):
        if piece is None and color is None:
            self.board[field][1] = None
        else:
            self.board[field][1] = (piece, color)
    
    def flag_enpassant_beatings(self, field_beatings):
        for field, beating in field_beatings:
            self.board[field][1][0].en_passant_beatings.append(beating)
    
def draw_promotion_possibilites(x: int, y: int, pawn_promotion_field, screen) -> tuple[int, int, int, int, str, str]:
    green_color = (0, 70,  0) # dark green
    black_color = (0, 0,  0 ) # dark green
    images = ImagesLoader()

    rect_width, rect_height = 90, 390
    rect_x = x + 5
    #* Promocja bialego piona
    if pawn_promotion_field[1] == '8': 
        rect_y = y + 105
        pieces = [Piece.Queen(x, y + 100, images.WHITE_PIECES['queen']),\
                    Piece.Knight(x, y+200, images.WHITE_PIECES['knight']),\
                        Piece.Bishop(x, y + 300, images.WHITE_PIECES['bishop']),\
                        Piece.Rook(x, y + 400, images.WHITE_PIECES['rook'])]
        color = 'white'
    #* Promocja czarnego piona
    else:
        rect_y = y - 395
        pieces = [Piece.Queen(x, y - 400, images.BLACK_PIECES['queen']),\
                    Piece.Knight(x, y-300, images.BLACK_PIECES['knight']),\
                        Piece.Bishop(x, y - 200, images.BLACK_PIECES['bishop']),\
                        Piece.Rook(x, y - 100, images.BLACK_PIECES['rook'])]   
        color = 'black'             

    pygame.draw.rect(screen, black_color, (rect_x - 3, rect_y - 3, rect_width + 6, rect_height + 6), border_radius=20)
    pygame.draw.rect(screen, green_color, (rect_x, rect_y, rect_width, rect_height), border_radius=20)
    if pawn_promotion_field[1] == '8': 
        for i in range(2,5):
            pygame.draw.rect(screen, black_color, (x + 2, y + i * 100 , 100 - 4, 3))
    else:
        for i in range(1,4):
            pygame.draw.rect(screen, black_color, (x + 2, y - i * 100 , 100 - 4, 3))
    for piece in pieces:
        piece.draw(screen)

    return rect_x, rect_y, rect_width, rect_height, color, pawn_promotion_field



def draw_window(board: Board, highlight_field:bool, x:int, y:int, piece:Piece, pawn_promotion_field:str|None, screen) -> None:
    box = None
    board.draw_board()
    if highlight_field:
        board.highlight_field(x,y) 
    board.draw_pieces()
    if pawn_promotion_field:
            x,y = board.get_field_pos(pawn_promotion_field)
            board.highlight_field(x,y) 
            box = draw_promotion_possibilites(x, y, pawn_promotion_field, screen)
            #todo draw promotion possibilites and return its 

    if piece:
        possible_moves, possible_beatings = piece.get_possible_moves(board.get_field(x,y), board)
        for field in possible_moves:
            board.highlight_possible_move(field)
        for field in possible_beatings:
            board.highlight_possible_beat(field)
    
    return box

def promote_pawn(x:int, y:int, box:tuple[int,int,int,int,int, str, str], board:Board) -> bool:
    rect_x, rect_y, rect_width, rect_height, color, pawn_promotion_field = box
    rect_width += rect_x
    rect_height += rect_y
    field = board.get_field(x, y)
    field_pos_x, field_pos_y = board.get_field_pos(pawn_promotion_field)
    images = ImagesLoader()

    if color == 'white':
        pieces_images = {'queen' : images.WHITE_PIECES['queen'], 'knight' : images.WHITE_PIECES['knight'],\
                         'bishop' : images.WHITE_PIECES['bishop'], 'rook' : images.WHITE_PIECES['rook']}
    else:
        pieces_images = {'queen' : images.BLACK_PIECES['queen'], 'knight' : images.BLACK_PIECES['knight'],\
                         'bishop' : images.BLACK_PIECES['bishop'], 'rook' : images.BLACK_PIECES['rook']}

    if rect_x <= x <= rect_width and rect_y <= y <= rect_height:
        if rect_y <= y <= rect_y + 100:
            board.set_piece_on_field(Piece.Queen(field_pos_x, field_pos_y, pieces_images['queen']), pawn_promotion_field, color)
        elif rect_y <= y <= rect_y + 200:
            board.set_piece_on_field(Piece.Knight(field_pos_x, field_pos_y, pieces_images['knight']), pawn_promotion_field, color)
        elif rect_y <= y <= rect_y + 300:
            board.set_piece_on_field(Piece.Bishop(field_pos_x, field_pos_y, pieces_images['bishop']), pawn_promotion_field, color)
        else:
            board.set_piece_on_field(Piece.Rook(field_pos_x, field_pos_y, pieces_images['rook']), pawn_promotion_field, color)
        return True
    return False


def add_enpassant_beatings(board: Board, fields = list[str]):
    for field in fields:
        board.board[field][1]