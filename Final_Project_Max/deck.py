import arcade

class Deck(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 768
        self.SPRITE_SCALE = 2

        self.DECK_POSITION = (self.SCREEN_WIDTH * 0.9, self.SCREEN_HEIGHT * 0.85)
        self.PATH = "images/extra_cards/card_back.png"

        self.texture = arcade.load_texture(self.PATH)

        self.center_x = self.DECK_POSITION[0]
        self.center_y = self.DECK_POSITION[1]
        self.scale = 2.5