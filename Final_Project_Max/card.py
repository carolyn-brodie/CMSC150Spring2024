import arcade

class Card(arcade.Sprite):
    def __init__(self, x_position, y_position, image):
        super().__init__()
        self.board = [[300, 100], [300, 300]]
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 768
        self.SPRITE_SCALE = 2

        self.CARD_POSITION = (self.SCREEN_WIDTH * 0.2, self.SCREEN_HEIGHT * 0.2)
        self.PATH = image

        self.texture = arcade.load_texture(self.PATH)

        self.center_x = x_position
        self.center_y = y_position
        self.scale = 2.5