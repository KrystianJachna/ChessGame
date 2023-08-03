# loads images

from os import getcwd
from pygame import image, transform

class ImagesLoader():
    def __init__(self) -> None:
        #* Sciezka do biezacego katalogu
        current_dir = getcwd()

        #* Obraz planszy
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
        BOARD_IMG = image.load(current_dir + "/ChessEngine/Assets/board.png")
        self.BOARD = transform.scale(BOARD_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        pieces = ["bishop", "king", "knight", "pawn", "queen", "rook"]
        #* Czarne bierki
        self.BLACK_PIECES = {piece : self.load_and_transform(current_dir + f"/ChessEngine/Assets/black_{piece}.png") for piece in pieces}
        #* Biale bierki
        self.WHITE_PIECES  = {piece : self.load_and_transform(current_dir + f"/ChessEngine/Assets/white_{piece}.png") for piece in pieces}

    def load_and_transform(self, image_path, width = 100, height = 100):
        img = image.load(image_path)
        return transform.scale(img, (width, height))
    
t = ImagesLoader()
