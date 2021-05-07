""" Sprite Sample Program """

import random
from typing import Optional
import pathlib
import os
import arcade
import sys

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_FLOWER = 0.08
COIN_COUNT = 50
FLOWER_COUNT = 150


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FILE_PATH: Optional[pathlib.Path] = None


def get_path(path: str) -> str:
    global FILE_PATH
    if not FILE_PATH:
        FILE_PATH = pathlib.Path(__file__).parent.absolute()
    return os.path.join(FILE_PATH, pathlib.Path(path))


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self) -> None:
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list: arcade.SpriteList
        self.coin_list: arcade.SpriteList
        self.evil_flower_list: arcade.SpriteList

        # Set up the player info
        self.player_sprite: arcade.Sprite
        self.score = 0
        self.health = 3

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self) -> None:
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.evil_flower_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Health
        self.health = 3

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(
            get_path("./character.png"), SPRITE_SCALING_PLAYER
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(get_path("coin_01.png"), SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(FLOWER_COUNT):
            flower = arcade.Sprite(get_path("evil.png"), SPRITE_SCALING_FLOWER)
            flower.center_x = random.randrange(SCREEN_WIDTH)
            flower.center_y = random.randrange(SCREEN_HEIGHT)
            if flower.center_y <= 100:
                flower.center_y += 100
            if flower.center_x <= 100:
                flower.center_x += 100
            self.evil_flower_list.append(flower)

    def on_draw(self) -> None:
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.evil_flower_list.draw()

        # Put the text on the screen.
        score = f"Score: {self.score}"
        arcade.draw_text(score, 10, 20, arcade.color.WHITE, 14)
        health = f"Health: {self.health}"
        arcade.draw_text(
            health, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20, arcade.color.RED, 14
        )

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time: float) -> None:
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.evil_flower_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        flower_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.evil_flower_list
        )
        for flower in flower_hit_list:
            flower.remove_from_sprite_lists()
            self.health -= 1
        if self.health <= 0:
            sys.exit()


def main() -> None:
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
