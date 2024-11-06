import cairo
import math
import random

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_sunrise_background(context):
    # Create a radial gradient for a sunrise background
    gradient = cairo.RadialGradient(WIDTH // 2, HEIGHT // 2, 300, WIDTH // 2, HEIGHT // 2, 600)
    gradient.add_color_stop_rgb(0, 1, 0.9, 0.6)  # Light yellow-orange at the center
    gradient.add_color_stop_rgb(0.5, 1, 0.5, 0.3)  # Soft orange midway
    gradient.add_color_stop_rgb(1, 0.7, 0.2, 0.1)  # Darker orange at the edges

    context.set_source(gradient)
    context.rectangle(0, 0, WIDTH, HEIGHT)
    context.fill()


def draw_daytime_sky(context, center_x, center_y, radius):
    # Create a radial gradient to represent a bright blue daytime sky
    gradient = cairo.RadialGradient(center_x, center_y, radius * 0.8, center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 0.53, 0.81, 0.98)  # Sky blue at the center
    gradient.add_color_stop_rgb(1, 1, 1, 1)           # Light white-blue at the edges

    context.arc(center_x, center_y, radius, 0, 2 * math.pi)  # Cover the globe area
    context.set_source(gradient)
    context.fill()


def draw_tree(context, x, y, scale=1.0):
    # Draw trunk
    context.set_source_rgb(0.55, 0.27, 0.07)  # Brown color
    context.rectangle(x - 5 * scale, y, 10 * scale, 40 * scale)
    context.fill()

    # Draw leaves
    context.set_source_rgb(0, 0.5, 0)  # Green color
    context.arc(x, y - 20 * scale, 25 * scale, 0, 2 * math.pi)
    context.fill()
    context.arc(x, y - 40 * scale, 20 * scale, 0, 2 * math.pi)
    context.fill()
    context.arc(x, y - 60 * scale, 15 * scale, 0, 2 * math.pi)
    context.fill()
    context.arc(x, y - 75 * scale, 10 * scale, 0, 2 * math.pi)
    context.fill()


def draw_stand(context, center_x, center_y, radius):
    # Dark brown base layer for the stand
    context.set_source_rgb(0.7, 1, 0.2)  # Dark brown color
    context.save()
    context.translate(center_x, center_y + radius * 1.3)  # Move to below the globe
    context.scale(1, 0.4)  # Make it more oval-shaped
    context.arc(0, 0, radius * 0.9, 0, 2 * math.pi)
    context.restore()
    context.fill()

    # Middle layer with lighter brown for 3D effect
    context.set_source_rgb(0, 0.5, 0)  # Medium brown color
    context.save()
    context.translate(center_x, center_y + radius * 1.15)
    context.scale(1, 0.3)
    context.arc(0, 0, radius * 0.8, 0, 2 * math.pi)
    context.restore()
    context.fill()

    # Top layer for the stand, to make it look like the globe sits on it
    context.set_source_rgb(0.1, 0.3, 0.3)  # Light brown
    context.save()
    context.translate(center_x, center_y + radius * 1.05)
    context.scale(1, 0.25)
    context.arc(0, 0, radius * 0.7, 0, 2 * math.pi)
    context.restore()
    context.fill()


def draw_birds(context, num_birds, center_x, center_y, radius):
    context.set_source_rgb(0, 0, 0)  # Black color for the birds
    for _ in range(num_birds):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(0, radius * 0.8)
        x = center_x + dist * math.cos(angle)
        y = center_y + dist * math.sin(angle)
        # Draw simple bird shapes as V
        context.move_to(x, y)
        context.line_to(x - 10, y + 10)
        context.line_to(x + 10, y + 10)
        context.close_path()
        context.fill()


def draw_butterflies(context, num_butterflies, center_x, center_y, radius):
    context.set_source_rgba(0.9, 0.6, 0.2, 0.8)  # Orange with some transparency for butterflies
    for _ in range(num_butterflies):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(0, radius * 0.8)
        x = center_x + dist * math.cos(angle)
        y = center_y + dist * math.sin(angle)
        # Draw small butterfly wings as arcs
        context.arc(x, y, 3, 0, math.pi)
        context.fill()
        context.arc(x + 6, y, 3, 0, math.pi)
        context.fill()


# Draw sunrise background
draw_sunrise_background(context)

# Draw the globe's sky inside
draw_daytime_sky(context, WIDTH // 2, HEIGHT // 2, 200)

# Draw trees inside the globe
draw_tree(context, WIDTH // 2 - 80, HEIGHT // 2 + 180, scale=1.5)  # Left tree
draw_tree(context, WIDTH // 2 + 80, HEIGHT // 2 + 180, scale=1.5)  # Right tree
draw_tree(context, WIDTH // 2, HEIGHT // 2 + 150, scale=1.8)       # Center tree, a bit lower

# Draw birds in the background
draw_birds(context, num_birds=10, center_x=WIDTH // 2, center_y=HEIGHT // 2, radius=200)

# Draw butterflies inside the globe
draw_butterflies(context, num_butterflies=10, center_x=WIDTH // 2, center_y=HEIGHT // 2, radius=200)

# Draw the stand at the bottom
draw_stand(context, WIDTH // 2, HEIGHT // 2.55, 200)

# Save the image
surface.write_to_png("sunrise_with_birds.png")
