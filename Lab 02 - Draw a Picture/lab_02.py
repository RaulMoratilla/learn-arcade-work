"""
Drawing a football field
"""

import arcade

arcade.open_window(800, 600, "Football Field")

# Dark blue as background colour
arcade.set_background_color((10,2,71))

arcade.start_render()

# Draw a dark green rectangle at the bottom part

arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, (28,41,1))

# Draw a dark green trapeze rounding the field

arcade.draw_polygon_filled([[0, 100],
                            [0, 200],
                            [180, 530],
                            [620, 530],
                            [800, 200],
                            [800,100]],
                            (28, 41, 1))

# Draw a light green trapeze to get depth

arcade.draw_polygon_filled([[0, 100],
                            [210, 500],
                            [590, 500],
                            [800, 100]],
                            (102, 138, 25))

# Remark borders with a white line
                      
arcade.draw_polygon_outline([[0, 100],
                            [210, 500],
                            [590, 500],
                            [800, 100]],
                            (255, 255, 255),
                            4)
            
# Big areas

arcade.draw_polygon_outline([[180, 100],
                            [220, 210],
                            [580, 210],
                            [620, 100]],
                            (255, 255, 255),
                            4)

arcade.draw_polygon_outline([[322, 500],
                            [305, 450],
                            [495, 450],
                            [478, 500]],
                            (255, 255, 255),
                            4)

# Small areas

arcade.draw_polygon_outline([[253, 100],
                            [270, 155],
                            [530, 155],
                            [547, 100]],
                            (255, 255, 255),
                            4)

arcade.draw_polygon_outline([[365, 500],
                            [358, 475],
                            [442, 475],
                            [435, 500]],
                            (255, 255, 255),
                            4)

# Center line

arcade.draw_line(130, 345, 670, 345, (255, 255, 255), 4)

# Center circle

arcade.draw_ellipse_outline(400, 345, 200, 120, (255, 255, 255), 4, 0, -1)

# Exterior grey lines pretending to be the passageway of the stands

for i in range(7):
    arcade.draw_line(0, 200+i*75, 180-i*27, 530+i*24, (115, 112, 108), 4)

for i in range(7):
    arcade.draw_line(800, 200+i*75, 620+i*27, 530+i*24, (115, 112, 108), 4)

for i in range(3):
    arcade.draw_line(180-i*27, 530+i*24, 620+i*27, 530+i*24, (115, 112, 108), 4)

# Orange lines pretending to be the stairs of the stands 

arcade.draw_line(180, 530, 100, 600, (227, 136, 18), 4)

arcade.draw_line(400, 530, 400, 600, (227, 136, 18), 4)

arcade.draw_line(94, 375, 0, 450, (227, 136, 18), 4)

arcade.draw_line(706, 375, 800, 450, (227, 136, 18), 4)

arcade.draw_line(620, 530, 700, 600, (227, 136, 18), 4)

arcade.finish_render()

arcade.run()