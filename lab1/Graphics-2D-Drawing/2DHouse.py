import cairo

# Setup surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 500)
context = cairo.Context(surface)

# Background color (white)
context.set_source_rgb(1, 1, 1)
context.paint()

# Draw the house
def draw_house():
    # Draw main house rectangle
    context.set_source_rgb(0, 0, 0)  # black color
    context.set_line_width(3)

    # Base of house
    context.move_to(100, 200)
    context.line_to(100, 380)

    # top window
    context.rectangle(175, 210, 40, 40)
    context.stroke()

    # middle rectangle
    context.rectangle(150, 275, 100, 60)
    context.stroke()

    #bottom rectangle
    context.rectangle(140, 335, 120, 15)
    context.stroke()

    #Right Rectangle
    context.rectangle(300, 200, 280, 185)
    context.stroke()

    # other rectangle
    context.rectangle(450, 275, 100, 60)
    context.stroke()

    # other lower Rectangle
    context.rectangle(440, 335, 120, 15)
    context.stroke()

    # Lower Rectangle
    context.rectangle(90, 385, 500, 15)
    context.stroke()

    # Draw the roof (a parallelogram)
    context.move_to(300, 200)  # Left bottom of the roof
    context.line_to(40, 90)
    context.line_to(300, 90)  # Top of the roof (roof peak)
    context.line_to(600, 200)  # Right bottom of the roof
    context.close_path()  # Close the triangle shape
    context.stroke()

    #triangle roof
    context.move_to(90, 250)
    context.line_to(200, 100)
    context.line_to(310, 250)
    context.stroke()
    context.move_to(80, 240)
    context.line_to(200, 70)
    context.line_to(320, 240)
    context.stroke()

# Draw the moon (crescent)
def draw_moon():
    # Moon circle
    context.arc(450, 80, 40, 0, 2 * 3.14)
    context.stroke()

    # Crescent (overlaying smaller circle)
    context.arc(460, 80, 30, 0, 2 * 3.14)
    context.set_source_rgb(1, 1, 1)  # white to overlay
    context.fill()

# Call the draw functions
draw_house()
draw_moon()

# Save to file
surface.write_to_png("house_drawing_updated.png")
