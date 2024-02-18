from classes.AbstractTurtle import AbstractTurtle
from classes.City import City

class Arrow(AbstractTurtle):

    def __init__(self, origin : City, destination : City):
        AbstractTurtle.__init__(self, visible = True, color='red',shape='arrow')
        self._setup()
        self.origin = origin
        self.destination = destination
        # TODO: refatorar e colocar ângulo aqui
        # colocar tambem current city (origin) e current destination
        # self.current_angle

    @property
    def current_angle(self):
        return self.origin.angle(self.destination)
    
    def set_origin(self, origin : City):
        self.origin = origin

    def set_destination(self, destination : City):
        self.destination = destination

    def _setup(self):
        self.width(2)
    
    def draw_arrow(self):
        self.clear()
        self.penup()
        self.goto(self.origin.pos())
        self.setheading(self.origin.towards(self.destination))
        self.pendown()
        arrow_size = self.origin.distance_to(self.destination)
        self.forward(arrow_size)