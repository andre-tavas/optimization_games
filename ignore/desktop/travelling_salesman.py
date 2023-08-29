from typing import List, Tuple, Type
import turtle
import math
import random
from utils import *

def get_cities_loc(min_width = -250, max_width = 250, 
                   min_height = -250, max_height = 250):
    cities_loc = []
    for c in range(10):
        x = random.randint(min_width, max_width)
        y = random.randint(min_height,max_height)
        cities_loc.append((x,y))
    return cities_loc

def screen_setup(split_screen = False):
    # Creating the screen with name and size
    screen = turtle.Screen()
    screen.title("Caixeiro Viajante")
    # screen.setup(width=1.0, height=1.0, startx=None, starty=None)
    screen.setup(width=0.85, height=0.95, starty=0)
    
    if split_screen:
        divider_turtle = turtle.Turtle()
        divider_turtle.width(5)
        divider_turtle.color('black')
        divider_turtle.speed(0)
        divider_turtle.penup()
        divider_turtle.goto(0, -screen.window_height() // 2)
        divider_turtle.pendown()
        divider_turtle.goto(0, screen.window_height()//2)
        divider_turtle.hideturtle()
    
    return screen

class City(turtle.Turtle):
    origin_defined = False
    cities = []

    def __init__(self, pos : Tuple, name = None, color = None):
        turtle.Turtle.__init__(self, shape = 'circle', visible = True)
        self.name = name
        self.visited = False
        self.penup()
        self.speed(0)
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(pos)
        self.write(name)
        # self.hideturtle()

        City.cities.append(self)
        if not City.origin_defined:
            self.color('red')
            City.origin_defined = True
    
    def __repr__(self) -> str:
        if self.name != None:
            return f"{self.name}"
        else:
            return super().__repr__

    def distance_to(self, other : Type['City']) -> float:
        '''Return the linear distance to another city'''
        x_distance = abs(self.xcor() - other.xcor())
        y_distance = abs(self.ycor() - other.ycor())
        return math.sqrt(x_distance**2 + y_distance**2)
    
    def angle(self, other : Type['City']):
        return self.towards(other)
    
class Salesman(turtle.Turtle):
    def __init__(self, origin : City):
        turtle.Turtle.__init__(self, visible = False)
        self.house = origin
        self.current_city = origin
        self.color('blue')
        self.penup()
        self.goto(origin.pos())
        self.pendown()
        self.pencolor('blue')
        self.hideturtle()
        self.dx = 4
        self.dy = 4

    def travel(self, destination):
        self.goto(destination.pos())

class Arrow(turtle.Turtle):
    def __init__(self):
        self.arrow = self._arrow_setup()
        # TODO: refatorar e colocar ângulo aqui
        # colocar tambem current city (origin) e current destination
        # self.current_angle

    def _arrow_setup(self) -> turtle.Turtle:
        arrow = turtle.Turtle()
        arrow.shape('arrow')
        arrow.color('red')
        arrow.shapesize(stretch_wid=0.6)
        arrow.speed(0)
        arrow.width(2)
        return arrow
    
    def draw_arrow(self, origin : City, destination : City):
        self.arrow.clear()
        self.arrow.penup()
        self.arrow.goto(origin.pos())
        self.arrow.setheading(origin.towards(destination))
        self.arrow.pendown()
        arrow_size = origin.distance_to(destination)
        self.arrow.forward(arrow_size)
        

class Score(turtle.Turtle):
    def __init__(self, position):
        turtle.Turtle.__init__(self, visible = False)
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.current_score = 0
        self.write("Custo atual: 0", align="center", font=("Courier", 13, "bold"))

    def update(self, cost):
        self.clear()
        self.write(f"Custo atual: {cost}", 
                   align="center", 
                   font=("Courier", 13, "bold"))
        
    def end_game(self, final_cost):
        self.clear()
        self.color('red')
        self.write(f"Custo final: {final_cost}", 
                   align="center", 
                   font=("Courier", 13, "bold"))

class Game:
    def __init__(self, cities : List[City], 
                 salesman : Salesman,
                 arrow : Arrow,
                 score : Score,
                 commands_dict = None):
        self.cities = cities
        self.salesman = salesman
        self.arrow = arrow
        self.current_city = self.salesman.house
        self.current_destination = None
        self.current_destination = self.neighbours[0]
        self.cost = 0
        self.score = score
        self._end_game = False
        arrow.draw_arrow(self.current_city, self.current_destination)
        self._commands_dict = commands_dict
        # self.keys_controlling(commands_dict)
    
    @property
    def neighbours(self) -> List[City]: # mudar para candidates
        '''
        Returns the unvisited and diferent from 
        the current origin and destination
        '''
        return [c for c in self.cities
                if c not in [self.current_city, self.current_destination]
                and not c.visited]

    def get_closest_neighbour(self, clockwise = True):
        factor = 1
        if not clockwise:
            factor = -1
        smallest_angle = 360
        closest = None
        for n in self.neighbours:
            n_angle = self.current_city.angle(n)
            angle_to_compare = (self._current_angle - n_angle) * factor
            if angle_to_compare <= 0:
                n_angle *= factor
                angle_to_compare = self._current_angle * factor + (360 - n_angle)

            if angle_to_compare <= smallest_angle:
                smallest_angle = angle_to_compare
                closest = n
        return closest
    
    def next_neighbour(self, direction : str):
        direction = direction.lower()
        if is_between(self._current_angle, 0, 90):
            if direction in ['left', 'up']:
                next = self.get_closest_neighbour(clockwise = False)
            else:
                next = self.get_closest_neighbour(clockwise = True)
        elif is_between(self._current_angle, 91, 180):
            if direction in ['left', 'down']:
                next = self.get_closest_neighbour(clockwise = False)
            else:
                next = self.get_closest_neighbour(clockwise = True)
        elif is_between(self._current_angle, 181, 280):
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
            self.current_destination = next
            self.arrow.draw_arrow(self.current_city, next)

    def get_random_neighbour(self):
        if len(self.neighbours) == 0:
            return self.salesman.house
        else:
            return random.choice(self.neighbours)
    
    def make_travel(self):
        house = self.salesman.house
        if not self._end_game:
            dest = self.current_destination
            self.cost += int(self.current_city.distance_to(self.current_destination))
            self.score.update(self.cost)
            self.salesman.travel(dest)
            if dest != house or self.get_random_neighbour() == house:
                dest.color('green')
                dest.visited = True
            self.current_city = dest
            self.current_destination = self.get_random_neighbour()
            self.arrow.draw_arrow(self.current_city, self.current_destination)
        if all([c.visited for c in self.cities])\
            and self.current_city == house:
            self._end_game = True
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

def play_alone(screen = None, **kwargs):
    if not screen:
        screen = screen_setup(split_screen=False)
        width_reference = 0
        width_len = int(screen.window_width() * 0.9)
        height = screen.window_height() * 0.9

    cities_loc = get_cities_loc(min_width = int(width_reference - width_len/2),
                                max_width = int(width_reference + width_len/2),
                                min_height = int(-height/2),
                                max_height = int(height/2 * 0.85))
    
    cities = [City(pos, name = idx) for idx, pos in enumerate(cities_loc)]
    salesman = Salesman(cities[0])
    arrow = Arrow()
    score = Score(position = (0, height/2 * 0.9))
    game = Game(cities, salesman, arrow, score)
    game.start()

    screen.mainloop()

def play_versus():
    screen = screen_setup(split_screen=True)
    width = screen.window_width()/2
    width_len = int(width * 0.9)
    height = screen.window_height() * 0.9
    width_reference = 0
    width_margin = screen.window_width()/2 * 0.05

    # GET CITIES LOC
    cities_loc = get_cities_loc(min_width = -int(width_len/2),
                                  max_width = int(width_len/2),
                                  min_height = int(-height/2),
                                  max_height = int(height/2 * 0.85))
    
    # cities_loc_2 = get_cities_loc(min_width = width_reference + width_margin,
    #                               max_width = width_reference + (width_len + width_margin),
    #                               min_height = int(-height/2),
    #                               max_height = int(height/2 * 0.85))

    width_diff = screen.window_width()/4
    cities_loc_1 = [(x - width_diff, y) for (x,y) in cities_loc]
    cities_loc_2 = [(x + width_diff, y) for (x,y) in cities_loc]
    
    # CREATES CITIES OBJECTS
    cities_1 = [City(pos, name = idx) for idx, pos in enumerate(cities_loc_1)]
    City.origin_defined = False
    cities_2 = [City(pos, name = idx) for idx, pos in enumerate(cities_loc_2)]

    # CREATES SALESMAN OBJECTS 
    salesman_1 = Salesman(cities_1[0])
    salesman_2 = Salesman(cities_2[0])

    arrow_1 = Arrow()
    arrow_2 = Arrow()

    score_1 = Score(position = (-width/2, height/2 * 0.95))
    score_2 = Score(position = (width/2, height/2 * 0.95))

    commands_dict_2 = {'up' : 'w', 'down' : 's',
                       'right' : 'd', 'left' : 'a',
                       'travel' : 'space'}
    
    game_1 = Game(cities_1, salesman_1, arrow_1, score_1, commands_dict_2)
    game_2 = Game(cities_2, salesman_2, arrow_2, score_2)

    game_1.start()
    game_2.start()

    

    # while True:
    #     a = None
    
    screen.mainloop()
    
    # Ver como rodar os dois jogos em paralelo
    # play_alone(screen = None, width_reference = 0 - width/2,
    #            width_len = width_len, height = height)
    
    # cities_loc_1 = get_cities_loc(min_width = int(0-width_margin-width),
    #                               max_width = int(0-width_margin),
    #                               min_height = int(-height/2),
    #                               max_height = int(height/2 * 0.85))


if __name__ == '__main__':
    play_versus()