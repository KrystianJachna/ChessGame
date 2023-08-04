# Piece service

from abc import ABC, abstractclassmethod
from pygame import Surface, display
from ChessEngine.images_loader import ImagesLoader



class Piece(ABC):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        self.x : int = x
        self.y : int = y
        self.surface_to_draw : Surface = surface_to_draw
        self.board_field : list[list[str]] = [[letter + str(num) for num in range(0,9)] for letter in ['','a','b','c','d','e','f','g','h']]

    def draw(self, screen: display):
        screen.blit(self.surface_to_draw, (self.x, self.y))

    def change_pos(self, x : int, y : int):
        self.x = x
        self.y = y

    def get_possible_moves() -> list[str]:
        pass

    def check_if_free(board) -> bool:
        pass


class King(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves():
        pass
        
class Queen(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves():
        pass

class Rook(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves():
        pass

class Bishop(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves():
        pass

class Knight(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)

    def get_possible_moves():
        pass

#todo bicia
class BlackPawn(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)
        self.first_move : bool = True

    def get_possible_moves(self, current_field):
        if self.first_move:
            all_fields = [current_field[0] + str(int(current_field[1]) - 1), current_field[0] + str(int(current_field[1]) - 2)]
        else:
            all_fields = [current_field[0] + str(int(current_field[1]) - 1)]

        return all_fields

class WhitePawn(Piece):
    def __init__(self, x : int, y : int, surface_to_draw : Surface) -> None:
        super().__init__(x, y, surface_to_draw)
        self.first_move : bool = True

    def get_possible_moves(self, current_field):
        if self.first_move:
            all_fields = [current_field[0] + str(int(current_field[1]) + 1), current_field[0] + str(int(current_field[1]) + 2)]
        else:
            all_fields = [current_field[0] + str(int(current_field[1]) + 1)]

        return all_fields