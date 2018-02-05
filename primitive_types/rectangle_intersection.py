from collections import namedtuple

Rectangle = namedtuple("Rectangle", ("x","y","width","height"))

def are_rectangles_intersecting(rectangle1, rectangle2):
    new_x = max(rectangle1.x, rectangle2.x)
    new_y = max(rectangle1.y, rectangle2.y)
    new_width = min(rectangle1.x+rectangle1.width-new_x, rectangle2.x+rectangle2.width-new_x)
    new_height = min(rectangle1.y+rectangle1.height-new_y, rectangle2.y+rectangle2.height-new_y)
    if new_width >= 0 and new_height >= 0 :
        return Rectangle(new_x, new_y, new_width, new_height)
    return Rectangle(0, 0, -1, -1)
