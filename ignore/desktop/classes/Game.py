from typing import List
import random
import turtle

from utils import is_between
from Arrow import Arrow
from Salesman import Salesman
from City import City
from Score import Score

class Game:
    def __init__(self, cities : List[City], 
                 salesman : Salesman,
                 arrow : Arrow,
                 score : Score,
                 commands_dict = None):
        self.cities = cities
        self.salesman = salesman
        self.arrow = arrow
        self.score = score
        self.end_game = False
        self._commands_dict = commands_dict

        arrow.destination = self.candidates[0]
        score.cost = 0
        arrow.draw_arrow()
        # self.keys_controlling(commands_dict)
    
    @property
    def candidates(self) -> List[City]: # mudar para candidates
        '''
        Returns the unvisited and diferent from 
        the current origin and destination
        '''
        current = self.salesman.current_city
        destination = self.arrow.destination
        return [c for c in self.cities
                if c not in [current, destination]
                and not c.visited]

    def get_closest_neighbour(self, clockwise = True):
        factor = 1
        if not clockwise:
            factor = -1
        smallest_angle = 360
        closest = None
        for n in self.candidates:
            n_angle = self.salesman.current_city.angle(n)
            angle_to_compare = (self.arrow.current_angle - n_angle) * factor
            if angle_to_compare <= 0:
                n_angle *= factor
                angle_to_compare = self.arrow.current_angle * factor + (360 - n_angle)

            if angle_to_compare <= smallest_angle:
                smallest_angle = angle_to_compare
                closest = n
        return closest
    
    def next_neighbour(self, direction : str):
        direction = direction.lower()
        current_angle = self.arrow.current_angle
        if is_between(current_angle, 0, 90):
            if direction in ['left', 'up']:
                next = self.get_closest_neighbour(clockwise = False)
            else:
                next = self.get_closest_neighbour(clockwise = True)
        elif is_between(current_angle, 91, 180):
            if direction in ['left', 'down']:
                next = self.get_closest_neighbour(clockwise = False)
            else:
                next = self.get_closest_neighbour(clockwise = True)
        elif is_between(current_angle, 181, 280):
            if direction in ['left', 'up']:
                next = self.get_closest_neighbour(clockwise = True)
            else:
                next = self.get_closest_neighbour(clockwise = False)
        else:
            if direction in ['right', 'up']:
                next = self.get_closest_neighbour(clockwise = False)
            else:
                next = self.get_closest_neighbour(clockwise = True)
        if next:
            self.arrow.set_destination(next)
            self.arrow.draw_arrow()

    def get_random_neighbour(self):
        if len(self.neighbours) == 0:
            return self.salesman.house
        else:
            return random.choice(self.candidates)
    
    def make_travel(self):
        house = self.salesman.house
        current_city = self.salesman.current_city
        destination = self.arrow.destination
        if not self.end_game:
            add_cost += int(current_city.distance_to(destination))
            self.score.update(add_cost)
            self.salesman.travel(destination)
            if destination != house or self.get_random_neighbour() == house:
                destination.color('green')
                destination.visited = True
            self.arrow.set_origin(destination)
            self.arrow.set_destination(self.get_random_neighbour())
            self.arrow.draw_arrow()
        if all([c.visited for c in self.cities])\
            and self.salesman.current_city == house:
            self.end_game = True
            self.score.end_game(self.cost)

    def start(self):
        if not self._commands_dict:
            commands_dict = {'up' : 'Up', 'down' : 'Down', 
                            'right' : 'Right', 'left' : 'Left',
                            'travel' : 'Return'}
        else:
            commands_dict = self._commands_dict
        
        turtle.listen()
        turtle.onkeypress(lambda: self.next_neighbour('up'), commands_dict['up'])
        turtle.onkeypress(lambda: self.next_neighbour('down'), commands_dict['down'])
        turtle.onkeypress(lambda: self.next_neighbour('left'), commands_dict['left'])
        turtle.onkeypress(lambda: self.next_neighbour('right'), commands_dict['right'])
        turtle.onkeypress(self.make_travel, commands_dict['travel'])