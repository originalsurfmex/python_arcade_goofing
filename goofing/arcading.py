import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "bounce"

RECT_WIDTH = 50
RECT_HEIGHT = 50


def on_draw(dt):

    arcade.start_render()

    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
                                 RECT_WIDTH, RECT_HEIGHT,
                                 arcade.color.AMETHYST)

    on_draw.center_x += on_draw.delta_x * dt
    on_draw.center_y += on_draw.delta_y * dt

    if on_draw.center_x < RECT_WIDTH // 2 \
       or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
       or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.delta_y *= -1


on_draw.center_x = 100
on_draw.center_y = 50
on_draw.delta_x = 115
on_draw.delta_y = 130


def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    arcade.schedule(on_draw, 1 / 60)

    arcade.run()


main()
