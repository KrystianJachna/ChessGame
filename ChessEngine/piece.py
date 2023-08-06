# Piece service

from abc import ABC, abstractmethod
from pygame import Surface, display



class Piece(ABC):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        self.x : int = x
        self.y : int = y
        self.surface_to_draw : Surface = surface_to_draw
        self.board_fields : list[list[str]] = [[letter + str(num) for num in range(0,9)] for letter in ['','a','b','c','d','e','f','g','h']]

    def draw(self, screen: display):
        screen.blit(self.surface_to_draw, (self.x, self.y))

    def change_pos(self, x : int, y : int):
        self.x = x
        self.y = y

    def find_pos(self, current_field) -> tuple[int,int]:
        first_index = ['','a','b','c','d','e','f','g','h'].index(current_field[0])
        second_index = int(current_field[1])
        return first_index, second_index
    
    def get_next_letter(self, letter : str, move : int = 1) -> str:
        letter_asci = ord(letter)
        return chr(letter + move)
    
    def get_field(self, i:int, j:int) -> str:
        return self.board_fields[i][j]

    @abstractmethod
    def get_possible_moves(self, current_field:str, board) -> tuple[list[str], list[str]]:
        pass

    def check_if_free(board) -> bool:
        pass


class King(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    #todo unikanie ruchow narazajacych na szacha, roszada
    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i, j = self.find_pos(current_field)
        
        possible_moves = []
        possible_beatings = []

        if j + 1 in range(1, 9):
            if i - 1 in range(1, 9):
                if board.get_piece_by_field(self.get_field(i -1 , j + 1)) is None:
                    possible_moves.append(self.get_field(i-1, j + 1))
                else:
                    if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1,j+1)):
                        possible_beatings.append(self.get_field(i-1, j + 1))
            if i + 1 in range(1, 9):
                if board.get_piece_by_field(self.get_field(i +1 , j + 1)) is None:
                    possible_moves.append(self.get_field(i+1, j + 1))
                else:
                    if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1,j+1)):
                        possible_beatings.append(self.get_field(i+1, j + 1))
            if board.get_piece_by_field(self.get_field(i  , j + 1)) is None:
                possible_moves.append(self.get_field(i, j + 1))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i,j+1)):
                    possible_beatings.append(self.get_field(i, j + 1))
        if j - 1 in range(1, 9):
            if i - 1 in range(1, 9):
                if board.get_piece_by_field(self.get_field(i -1 , j - 1)) is None:
                    possible_moves.append(self.get_field(i-1, j -1))
                else:
                    if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1,j-1)):
                        possible_beatings.append(self.get_field(i-1, j - 1))
            if i + 1 in range(1, 9):
                if board.get_piece_by_field(self.get_field(i +1 , j - 1)) is None:
                    possible_moves.append(self.get_field(i+1, j - 1))
                else:
                    if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1,j-1)):
                        possible_beatings.append(self.get_field(i+1, j - 1))
            if board.get_piece_by_field(self.get_field(i  , j -1)) is None:
                possible_moves.append(self.get_field(i, j - 1))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i,j-1)):
                    possible_beatings.append(self.get_field(i, j - 1))
        if i - 1 in range(1, 9):
                if board.get_piece_by_field(self.get_field(i -1 , j)) is None:
                    possible_moves.append(self.get_field(i-1, j))
                else:
                    if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1,j)):
                        possible_beatings.append(self.get_field(i-1, j))
        if i + 1 in range(1, 9):
            if board.get_piece_by_field(self.get_field(i +1 , j)) is None:
                possible_moves.append(self.get_field(i+1, j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1,j)):
                    possible_beatings.append(self.get_field(i+1, j))
        return possible_moves, possible_beatings

class Queen(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        tmp = Rook(self.x, self.y, self.surface_to_draw)
        rook_moves, rook_beatings = tmp.get_possible_moves(current_field, board)
        
        tmp = Bishop(self.x, self.y, self.surface_to_draw)
        bishop_moves, bishop_beatings = tmp.get_possible_moves(current_field, board)

        return rook_moves + bishop_moves, rook_beatings + bishop_beatings

class Rook(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i, j = self.find_pos(current_field)
        possible_moves = []
        possible_beatings = []

        for index in range(j + 1, 9):
            if board.get_piece_by_field(self.get_field(i, index)) is None:
                possible_moves.append(self.get_field(i, index))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i,index)):
                    possible_beatings.append(self.get_field(i, index))
                break
        for index in range(j - 1, 0, -1):
            if board.get_piece_by_field(self.get_field(i, index)) is None:
                possible_moves.append(self.get_field(i, index))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i,index)):
                    possible_beatings.append(self.get_field(i, index))
                break
        for index in range(i + 1, 9):
            if board.get_piece_by_field(self.get_field(index, j)) is None:
                possible_moves.append(self.get_field(index, j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(index, j)):
                    possible_beatings.append(self.get_field(index, j))
                break
        for index in range(i - 1, 0, -1):
            if board.get_piece_by_field(self.get_field(index, j)) is None:
                possible_moves.append(self.get_field(index, j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(index, j)):
                    possible_beatings.append(self.get_field(index, j))
                break
        return possible_moves, possible_beatings

class Bishop(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i, j = self.find_pos(current_field)

        possible_moves = []
        possible_beatings = []

        next_i = i + 1
        next_j = j + 1

        while next_i in range(1,9) and next_j in range(1,9):
            if board.get_piece_by_field(self.get_field(next_i, next_j)) is None:
                possible_moves.append(self.get_field(next_i, next_j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(next_i, next_j)):
                    possible_beatings.append(self.get_field(next_i, next_j))
                break
            next_i += 1
            next_j += 1
        
        next_i = i - 1
        next_j = j - 1
        while next_i in range(1,9) and next_j in range(1,9):
            if board.get_piece_by_field(self.get_field(next_i, next_j)) is None:
                possible_moves.append(self.get_field(next_i, next_j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(next_i, next_j)):
                    possible_beatings.append(self.get_field(next_i, next_j))
                break
            next_i -= 1
            next_j -= 1

        next_i = i + 1
        next_j = j - 1
        while next_i in range(1,9) and next_j in range(1,9):
            if board.get_piece_by_field(self.get_field(next_i, next_j)) is None:
                possible_moves.append(self.get_field(next_i, next_j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(next_i, next_j)):
                    possible_beatings.append(self.get_field(next_i, next_j))
                break
            next_i += 1
            next_j -= 1

        next_i = i - 1
        next_j = j + 1
        while next_i in range(1,9) and next_j in range(1,9):
            if board.get_piece_by_field(self.get_field(next_i, next_j)) is None:
                possible_moves.append(self.get_field(next_i, next_j))
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(next_i, next_j)):
                    possible_beatings.append(self.get_field(next_i, next_j))
                break
            next_i -= 1
            next_j += 1
        return possible_moves, possible_beatings


class Knight(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i, j = self.find_pos(current_field)
        all_moves = []

        if i - 1 in range(1,9):
            if j + 2 in range(1,9):
                all_moves.append(self.get_field(i-1, j+2))
            if j - 2 in range(1,9):
                all_moves.append(self.get_field(i-1, j-2))
        if i + 1 in range(1,9):
            if j + 2 in range(1,9):
                all_moves.append(self.get_field(i+1, j+2))
            if j - 2 in range(1,9):
                all_moves.append(self.get_field(i+1, j-2))
        if i - 2 in range(1,9):
            if j + 1 in range(1,9):
                all_moves.append(self.get_field(i-2, j+1))
            if j - 1 in range(1,9):
                all_moves.append(self.get_field(i-2, j-1))
        if i + 2 in range(1,9):
            if j + 1 in range(1,9):
                all_moves.append(self.get_field(i+2, j+1))
            if j - 1 in range(1,9):
                all_moves.append(self.get_field(i+2, j-1))

        possible_moves = []
        possible_beatings = []

        for move in all_moves:
            if board.get_piece_by_field(move) is None:
                possible_moves.append(move)
            else:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(move):
                    possible_beatings.append(move)

        return possible_moves, possible_beatings

#todo bicie w przelocie na pierwszym, promocja
class BlackPawn(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)
        self.first_move : bool = True

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i,j = self.find_pos(current_field)
        possible_moves = []
        possible_beatings = []
        
        if self.first_move:     
            #* Mozliwe ruchy
            if j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i, j-1)) is None:
                possible_moves.append(self.get_field(i, j-1))
                if j-2 in range(1,9) and board.get_piece_by_field(self.get_field(i, j-2))  is None:
                    possible_moves.append(self.get_field(i, j-2))
            #* Mozliwe bicia
            if i+1 in range(1,9) and j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i+1,j-1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1, j-1)):
                    possible_beatings.append(self.get_field(i+1,j-1))
            if i-1 in range(1,9) and j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i-1,j-1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1, j-1)):
                    possible_beatings.append(self.get_field(i-1,j-1))
        else:
            #* Mozliwe ruchy
            if j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i, j-1)) is None:
                possible_moves.append(self.get_field(i, j-1))
            #* Mozliwe bicia
            if i+1 in range(1,9) and j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i+1,j-1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1, j-1)):
                    possible_beatings.append(self.get_field(i+1,j-1))
            if i-1 in range(1,9) and j-1 in range(1,9) and board.get_piece_by_field(self.get_field(i-1,j-1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1, j-1)):
                    possible_beatings.append(self.get_field(i-1,j-1))
        return possible_moves, possible_beatings


#todo bicie w przelocie na pierwszym, promocja
class WhitePawn(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)
        self.first_move : bool = True
        self.passant : bool = False         

    def get_possible_moves(self, current_field, board) -> tuple[list[str], list[str]]:
        i,j = self.find_pos(current_field)
        possible_moves = []
        possible_beatings = []
        
        if self.first_move:     
            #* Mozliwe ruchy
            if j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i, j+1)) is None:
                possible_moves.append(self.get_field(i, j+1))
                if j+2 in range(1,9) and board.get_piece_by_field(self.get_field(i, j+2))  is None:
                    possible_moves.append(self.get_field(i, j+2))
            #* Mozliwe bicia
            if i+1 in range(1,9) and j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i+1,j+1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1, j+1)):
                    possible_beatings.append(self.get_field(i+1,j+1))
            if i-1 in range(1,9) and j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i-1,j+1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1, j+1)):
                    possible_beatings.append(self.get_field(i-1,j+1))
        else:
            #* Mozliwe ruchy
            if j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i, j+1)) is None:
                possible_moves.append(self.get_field(i, j+1))
            #* Mozliwe bicia
            if i+1 in range(1,9) and j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i+1,j+1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i+1, j+1)):
                    possible_beatings.append(self.get_field(i+1,j+1))
            if i-1 in range(1,9) and j+1 in range(1,9) and board.get_piece_by_field(self.get_field(i-1,j+1)) is not None:
                if board.get_piece_color_by_field(current_field) != board.get_piece_color_by_field(self.get_field(i-1, j+1)):
                    possible_beatings.append(self.get_field(i-1,j+1))
        return possible_moves, possible_beatings

