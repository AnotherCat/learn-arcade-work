import arcade
import random

WIDTH = 700
HEIGHT = WIDTH


x = 100
y = 100


def on_draw(dt):
    arcade.start_render()

    arcade.draw_circle_filled(on_draw.x, on_draw.y, 25, arcade.color.BLUE)

    on_draw.x += dt * on_draw.vx
    on_draw.y += dt * on_draw.vy

    """
    if on_draw.x >= 675 or on_draw.x <= 25:
        on_draw.vx *= -1
        if on_draw.vx > 500:
            on_draw.vx = 100
    
    if on_draw.y >= 675 or on_draw.y <= 25:
        on_draw.vy *= -1
        if on_draw.vy > 300:
            on_draw.vy = 50
    """
    n = random.randint(1, 100)
    if on_draw.x >= 675:
        on_draw.vx = -1 * abs(on_draw.vx)
        on_draw.vx -= n
    elif on_draw.x <= 25:
        on_draw.vx = abs(on_draw.vx)
        on_draw.vx += n
    elif on_draw.y >= 675:
        on_draw.vy = -1 * abs(on_draw.vy)
        on_draw.vy -= n
    elif on_draw.y <= 25:
        on_draw.vy = abs(on_draw.vy)
        on_draw.vy += n


on_draw.x = 100
on_draw.y = 100
on_draw.vx = 100
on_draw.vy = 50

arcade.open_window(WIDTH, HEIGHT, "bouncey")


arcade.schedule(on_draw, 1 / 60)

arcade.run()
