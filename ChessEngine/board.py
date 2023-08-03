# Board service

from ChessEngine.images_loader import ImagesLoader
import ChessEngine.piece as Piece

class Board():
    def __init__(self) -> None:
        self.images = ImagesLoader()

        #* Koordynaty
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        numbers = [str(num) for num in range(1, 9)]

        self.board = {letter + number: None for letter in letters for number in numbers}

        #* Ustawienie gornego gracza
        self.board['a8'] = Piece.Roock(0, 0, self.images.BLACK_PIECES['roock'])
        self.board['b8'] = Piece.Roock(100, 0, self.images.BLACK_PIECES['knight'])
        self.board['c8'] = Piece.Roock(200, 0, self.images.BLACK_PIECES['bishop'])
        self.board['d8'] = Piece.Roock(300, 0, self.images.BLACK_PIECES['queen'])
        self.board['e8'] = Piece.Roock(400, 0, self.images.BLACK_PIECES['king'])
        self.board['f8'] = Piece.Roock(500, 0, self.images.BLACK_PIECES['bishop'])
        self.board['g8'] = Piece.Roock(600, 0, self.images.BLACK_PIECES['knight'])
        self.board['h8'] = Piece.Roock(700, 0, self.images.BLACK_PIECES['roock'])

        for letter, x in zip(letters, range(0, 800, 100)):
            self.board[letter + '7'] = Piece.BlackPawn(x, 100, self.images.BLACK_PIECES['pawn'])

        #* Ustawienie dolnego gracza
        self.board['a1'] = Piece.Roock(0, 700, self.images.WHITE_PIECES['roock'])
        self.board['b1'] = Piece.Roock(100, 700, self.images.WHITE_PIECES['knight'])
        self.board['c1'] = Piece.Roock(200, 700, self.images.WHITE_PIECES['bishop'])
        self.board['d1'] = Piece.Roock(300, 700, self.images.WHITE_PIECES['queen'])
        self.board['e1'] = Piece.Roock(400, 700, self.images.WHITE_PIECES['king'])
        self.board['f1'] = Piece.Roock(500, 700, self.images.WHITE_PIECES['bishop'])
        self.board['g1'] = Piece.Roock(600, 700, self.images.WHITE_PIECES['knight'])
        self.board['h1'] = Piece.Roock(700, 700, self.images.WHITE_PIECES['roock'])

        for letter, x in zip(letters, range(0, 800, 100)):
            self.board[letter + '2'] = Piece.BlackPawn(x, 600, self.images.WHITE_PIECES['pawn'])

        


    def draw_board(self, screen):
        screen.blit(self.images.BOARD, (0,0))

        for piece in self.board.values():
            if piece:
                piece.draw(screen)

