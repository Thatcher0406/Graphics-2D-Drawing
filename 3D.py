import cairo

# Image dimensions
width, height = 600, 400

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set background color to white
context.set_source_rgb(1, 1, 1)
context.rectangle(0, 0, width, height)
context.fill()

# Function to draw a rectangle with border
def draw_rect(x, y, w, h, fill_color, border_color, border_width=2):
    context.set_source_rgb(*fill_color)
    context.rectangle(x, y, w, h)
    context.fill_preserve()
    context.set_source_rgb(*border_color)
    context.set_line_width(border_width)
    context.stroke()

# Function to draw a polygon with border
def draw_polygon(points, fill_color, border_color, border_width=2):
    context.set_source_rgb(*fill_color)
    context.move_to(*points[0])
    for point in points[1:]:
        context.line_to(*point)
    context.close_path()
    context.fill_preserve()
    context.set_source_rgb(*border_color)
    context.set_line_width(border_width)
    context.stroke()

# Draw the main body of the house
draw_rect(200, 150, 200, 150, (0.9, 0.9, 0.9), (0, 0, 0))

# Draw the roof
roof_points = [(180, 150), (300, 70), (420, 150)]
draw_polygon(roof_points, (1, 0, 0), (0, 0, 0))

# Draw the chimney
draw_rect(320, 90, 20, 50, (0.9, 0.9, 0.9), (0, 0, 0))

# Draw the door
draw_rect(285, 230, 30, 70, (0.5, 0.25, 0), (0, 0, 0))

# Draw the door knob
context.set_source_rgb(0, 0, 0)
context.arc(305, 265, 3, 0, 2 * 3.14)
context.fill()

# Draw left window
draw_rect(220, 180, 30, 40, (0.5, 0.75, 1), (0.3, 0.2, 0.1))
draw_rect(255, 180, 30, 40, (0.5, 0.75, 1), (0.3, 0.2, 0.1))

# Draw right window
draw_rect(340, 180, 60, 40, (0.5, 0.75, 1), (0.3, 0.2, 0.1))

# Save the image
surface.write_to_png("house_drawing.png")
