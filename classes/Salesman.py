from classes.AbstractTurtle import AbstractTurtle
from classes.City import City

class Salesman(AbstractTurtle):
    def __init__(self, origin : City):
        AbstractTurtle.__init__(self, visible = False, color='blue')
        self.house = origin
        self.current_city = origin
        self.goto(origin.pos())
        self.pendown()

    def travel(self, destination : City):
        self.goto(destination.pos())
        self.current_city = destination
        
