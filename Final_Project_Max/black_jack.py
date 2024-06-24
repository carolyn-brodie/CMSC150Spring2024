import arcade
import random
from arcade.gui import UIManager
# from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane
from deck import Deck
from card import Card


# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Black Jack"

CARD_VALUES = ["A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "J", "Q", "K"]
CARD_SUITS = ["clubs", "hearts", "spades", "diamonds"]

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.card = None # Card Sprites
        self.hit = None # Hit button
        self.stand = None # Stand Button
        self.deck = None # Deck Image

        self.lst_card = None # Card Sprites lst
        self.lst_hit = None # Hit button Sprites lst
        self.lst_stand = None # Stand Button Sprites lst
        self.lst_deck = None # Deck Image Sprites lst

        self.score_player = None # Player Score
        self.score_dealer = None # Dealer Score
        arcade.set_background_color(arcade.color.AMAZON)
        # self.text = ""

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.lst_card = arcade.SpriteList()
        self.lst_hit = arcade.SpriteList()
        self.lst_stand = arcade.SpriteList()
        self.lst_deck = arcade.SpriteList()

        self.create_deck()
        self.create_player_card()
        self.create_dealer_card()
        # Added for buttons
        self.manager = UIManager()
        self.manager.enable()

        ##Text on screen
        # self.manager.add(
        #     UIInputText(x=600, y=110, width=200, height=50, text=self.text),
        # )

        ##Buttons
        # Create a BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        reload_button = arcade.gui.UIFlatButton(text="Print Text", width=200)
        self.v_box.add(reload_button.with_space_around(bottom=20))

        reload_button.on_click = self.on_click_print

        end_button = arcade.gui.UIFlatButton(text="Ending Button", width=200)
        self.v_box.add(end_button.with_space_around(bottom=20))

        end_button.on_click = self.on_click_end

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box)
        )


    def on_click_print(self, event):
        print("My Start:", event)




    def on_click_end(self, event):
        print("My Start:", event)
        # end_view = EndingView()
        # self.window.show_view(end_view)




    def draw(self):
        arcade.start_render()

        self.manager.draw()
        self.lst_deck.draw()
        self.lst_card.draw()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        self.draw()


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass

    def create_deck(self):
        self.deck = Deck()
        self.lst_deck.append(self.deck)

    def create_dealer_card(self):
        suit = random.choice(CARD_SUITS)
        value = random.choice(CARD_VALUES)
        self.card1 = Card(440, 668, f"./images/cards/card_{suit}_{value}.png")
        self.lst_card.append(self.card1)
        suit = random.choice(CARD_SUITS)
        value = random.choice(CARD_VALUES)
        self.card2 = Card(572, 668, f"./images/cards/card_{suit}_{value}.png")
        self.lst_card.append(self.card2)

    def create_player_card(self):
        suit = random.choice(CARD_SUITS)
        value = random.choice(CARD_VALUES)
        self.card1 = Card(572, 100, f"./images/cards/card_{suit}_{value}.png")
        suit = random.choice(CARD_SUITS)
        value = random.choice(CARD_VALUES)
        self.card2 = Card(440, 100, f"./images/cards/card_{suit}_{value}.png")
        self.lst_card.append(self.card1)
        self.lst_card.append(self.card2)

def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

