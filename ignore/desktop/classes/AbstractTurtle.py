import turtle

class AbstractTurtle(turtle.Turtle):

    def __init__(self, shape : str = 'circle',
                 visible : str = True,
                 color : str = 'black'):
        turtle.Turtle.__init__(self, shape = shape, visible = visible)
        self.penup()
        self.speed(0)
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=1)