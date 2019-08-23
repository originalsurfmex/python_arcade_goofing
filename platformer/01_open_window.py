import arcade

arcade.open_window(600, 600, "Drawing Example")

# arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
# arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
arcade.set_background_color(arcade.color.BABY_POWDER)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH)
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH, 45)

arcade.draw_point(50, 580, arcade.color.RED, 5)

arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)

arcade.draw_circle_outline(140, 580, 18, arcade.color.WISTERIA, 3)
arcade.draw_circle_filled(190, 580, 18, arcade.color.WISTERIA)

arcade.draw_ellipse_filled(240, 580, 30, 15, arcade.color.AMBER)

arcade.draw_text("BASE", 10, 450, arcade.color.BRICK_RED, 20)

arcade.finish_render()

arcade.run()
