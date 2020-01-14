import simplegui

# Constants are written in capital letters
WIDTH = 600
HEIGHT = 400

# Handler to draw on canvas :
# this function is called 60 times per second
def draw(canvas):
    canvas.draw_point ([WIDTH /2, HEIGHT /2] , 'Yellow')

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH , HEIGHT )
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
