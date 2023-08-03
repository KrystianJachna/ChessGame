# Piece service

from abc import ABC, abstractclassmethod
from ChessEngine.images_loader import ImagesLoader

class Piece(ABC):
    def __init__(self, x, y, surface) -> None:
        self.x, self.y = x, y
        self.surface = surface

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_possible_moves():
        pass


class King(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass
        
class Queen(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass

class Roock(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass

class Bishop(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass

class Knight(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass

class BlackPawn(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass

class WhitePawn(Piece):
    def __init__(self, x, y, surface) -> None:
        super().__init__(x, y, surface)

    def get_possible_moves():
        pass