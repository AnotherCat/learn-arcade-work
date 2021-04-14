import arcade

MOVEMENT_SPEED = 5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
class Car:
    def __init__(self, pos_x, pos_y, change_x, change_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = 200
        self.height = 95

    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x > SCREEN_WIDTH - self.width:
            self.pos_x = SCREEN_WIDTH - self.width

        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y > SCREEN_HEIGHT - self.height:
            self.pos_y = SCREEN_HEIGHT - self.height


    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x + 100, self.pos_y + 40, 200, 50, arcade.csscolor.GREEN)
        arcade.draw_rectangle_filled(self.pos_x + 110, self.pos_y + 80, 100, 30, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(self.pos_x+30, self.pos_y + 15, 15, arcade.csscolor.RED)
        arcade.draw_circle_filled(self.pos_x+170, self.pos_y + 15, 15, arcade.csscolor.RED)



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our car
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
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.run()

if __name__ == '__main__':
    main()