import turtle
import random

def is_between(number, lower_bound, upper_bound):
    '''Returns wheter number is between the bounds'''
    return number >= lower_bound and number <= upper_bound

def generate_cities_loc(min_width = -250, max_width = 250, 
                   min_height = -250, max_height = 250, 
                   width = None, height = None, 
                   num_cities = 10):
    if width and height:
        min_height = int(-height/2)
        max_height = int(height/2 * 0.85)
        min_width = -int(width/2)
        max_width = int(width/2)
    
    cities_loc = []
    for c in range(num_cities):
        x = random.randint(min_width, max_width)
        y = random.randint(min_height,max_height)
        cities_loc.append((x,y))
    return cities_loc

def get_quadrant(angle):
    if is_between(angle, 0, 90):
        return 1
    elif is_between(angle, 91, 180):
        return 2
    elif is_between(angle, 181, 270):
        return 3
    else:
        return 4