import math
from typing import Tuple, Type
from AbstractTurtle import AbstractTurtle

class City(AbstractTurtle):

    def __init__(self, pos : Tuple, name = None, color : str = 'black'):
        AbstractTurtle.__init__(self, visible = True, color = color)
        self.name = name
        self.visited = False
        self.goto(pos)
        self.write(name)

    def __repr__(self) -> str:
        return f"{self.name}"
    
    def distance_to(self, other : Type['City']) -> float:
        '''Return the linear distance to another city'''
        x_distance = abs(self.xcor() - other.xcor())
        y_distance = abs(self.ycor() - other.ycor())
        return math.sqrt(x_distance**2 + y_distance**2)
    
    def angle(self, other : Type['City']) -> float:
        return self.towards(other)
    
    def create_objects(cities_loc):
        objects = []
        for idx, pos in enumerate(cities_loc):
            if idx != 0:
                obj = City(pos, name = idx, color = 'red')
            else:
                obj = City(pos, name = idx)
            objects.append(obj)
        return objects

