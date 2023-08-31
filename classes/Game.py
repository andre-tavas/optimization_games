from typing import List, Tuple
import random
import turtle

from classes.utils import is_between
from classes.Arrow import Arrow
from classes.Salesman import Salesman
from classes.City import City
from classes.Score import Score

class Game:
    def __init__(self, cities : List[City],
                 score_pos : Tuple,
                 commands_dict = None):
        self.cities = cities
        self.salesman = Salesman(cities[0])
        self.arrow = Arrow(self.salesman.house, destination = None)
        self.score = Score(score_pos)
        self.is_finished = False
        self._commands_dict = commands_dict
        self.arrow.set_destination(self.candidates[0])
        self.arrow.draw_arrow()
    
    @property
    def candidates(self) -> List[City]:
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
    
    def get_score(self):
        return self.score.current_score

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
        if len(self.candidates) == 0:
            return self.salesman.house
        else:
            return random.choice(self.candidates)
    
    def make_travel(self):
        house = self.salesman.house
        current_city = self.salesman.current_city
        destination = self.arrow.destination
        if not self.is_finished:
            add_cost = int(current_city.distance_to(destination))
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
            self.score.end_game()
            self.is_finished = True

    def start(self):
        if not self._commands_dict:
            self._commands_dict = {'up' : 'Up', 'down' : 'Down', 
                            'right' : 'Right', 'left' : 'Left',
                            'travel' : 'Return'}
            commands_dict = self._commands_dict
        else:
            commands_dict = self._commands_dict
        
        turtle.listen()
        turtle.onkey(lambda: self.next_neighbour('up'), commands_dict['up'])
        turtle.onkey(lambda: self.next_neighbour('down'), commands_dict['down'])
        turtle.onkey(lambda: self.next_neighbour('left'), commands_dict['left'])
        turtle.onkey(lambda: self.next_neighbour('right'), commands_dict['right'])
        turtle.onkey(self.make_travel, commands_dict['travel'])

    def clear_commands(self):
        turtle.onkey(None, self._commands_dict['up'])
        turtle.onkey(None, self._commands_dict['down'])
        turtle.onkey(None, self._commands_dict['left'])
        turtle.onkey(None, self._commands_dict['right'])
        turtle.onkey(None, self._commands_dict['travel'])

    def clear_game(self):
        # TODO: Clear all the objects (save the objects somewhere and then delete them)
        pass