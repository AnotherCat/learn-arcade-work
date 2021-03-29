import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(300, 50, 600, 100, arcade.csscolor.BLUE)
arcade.draw_ellipse_filled(250, 138, 76, 76, arcade.csscolor.GREEN)

arcade.finish_render()


arcade.run()