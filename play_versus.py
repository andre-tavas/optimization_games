import turtle
from classes import utils
from classes.Arrow import Arrow
from classes.Screen import GameScreen, StartScreen
from classes.City import City
from classes.Game import Game
from classes.Salesman import Salesman
from classes.Score import Score
# from classes.utils import *

def main():
    # Cria a tela
    screen = turtle.Screen()
    screen.title("Caixeiro Viajante")
    screen.setup(width=0.85, height=0.90, starty=0)

    start_screen = StartScreen(screen)
    start_screen.wait_for_start(start, screen)
    
    # screen.mainloop()

def create_game(cities_loc, score_pos, commands_dict = None):
    cities = City.create_objects(cities_loc)
    game = Game(cities, score_pos, commands_dict)
    return game

def start(screen):
    game_screen = GameScreen(screen = screen, split = True)
    cities_loc = utils.generate_cities_loc(width= game_screen.width_player,
                                        height= game_screen.height * 0.85)
    width_diff = game_screen.width_player/2
    cities_loc_1 = [(x - width_diff, y) for (x,y) in cities_loc]
    cities_loc_2 = [(x + width_diff, y) for (x,y) in cities_loc]
    score_pos_1 = (-game_screen.width_player/2, game_screen.height/2)
    score_pos_2 = (game_screen.width_player/2, game_screen.height/2)
    commands_dict_1 = {'up' : 'w', 'down' : 's',
                    'right' : 'd', 'left' : 'a',
                    'travel' : 'space'}
    game_1 = create_game(cities_loc_1, score_pos_1, commands_dict_1)
    game_2 = create_game(cities_loc_2, score_pos_2)

    while True:
        game_1.start()
        game_2.start()

        if game_1.is_finished and game_2.is_finished:
            break

        screen.update()
    
    game_screen.game_over(score_1=game_1.get_score(), score_2=game_2.get_score())
    
    screen.clear()
    return None

if __name__ == '__main__':
    main()
    
