""" Lab 7 - User Control """

import arcade
import pathlib
import os

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3



class Car:
    def __init__(self, pos_x, pos_y, change_x, change_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = 200
        self.height = 95
        print(pathlib.Path(__file__).parent.absolute())
        self.sound = arcade.Sound(pathlib.Path(os.path.join(pathlib.Path(__file__).parent.absolute(), pathlib.Path("explosion.wav"))))

    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        if self.pos_x < 0:
            self.pos_x = 0
            self.sound.play()
        elif self.pos_x > SCREEN_WIDTH - self.width:
            self.pos_x = SCREEN_WIDTH - self.width
            self.sound.play()

        if self.pos_y < 0:
            self.pos_y = 0
            self.sound.play()
        elif self.pos_y > SCREEN_HEIGHT - self.height:
            self.pos_y = SCREEN_HEIGHT - self.height
            self.sound.play()


    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x + 100, self.pos_y + 40, 200, 50, arcade.csscolor.GREEN)
        arcade.draw_rectangle_filled(self.pos_x + 110, self.pos_y + 80, 100, 30, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(self.pos_x+30, self.pos_y + 15, 15, arcade.csscolor.RED)
        arcade.draw_circle_filled(self.pos_x+170, self.pos_y + 15, 15, arcade.csscolor.RED)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.background_color = arcade.color.SKY_BLUE
        self.car = Car(50, 50, 0 ,0)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.car.draw()

    def update(self, dt):
        self.car.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.car.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.car.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.car.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.car.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.car.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.car.change_y = 0
        


def main():
    window = MyGame()
    arcade.run()


main()