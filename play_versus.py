from classes import utils
#from classes.solve_problem import OptimalSalesman
from classes.Screen import GameScreen, StartScreen
from classes.City import City
from classes.Game import Game
from classes.AppScreen import AppScreen

def main():
    app = AppScreen('Travelling salesman game', instructions=False, optimal=True)

    app.game_loop(play, n_cities= 10)

def create_game(cities_loc, score_pos, commands_dict = None):
    cities = City.create_objects(cities_loc)
    game = Game(cities, score_pos, commands_dict)
    return game

def play(app_screen : AppScreen, get_optimal = False, num_cities = 10):
    cities_loc = utils.generate_cities_loc(width= app_screen.width_player,
                                        height= app_screen.height * 0.85, 
                                        num_cities=num_cities)
    
    width_diff = app_screen.width_player/2
    cities_loc_1 = [(x - width_diff, y) for (x,y) in cities_loc]
    cities_loc_2 = [(x + width_diff, y) for (x,y) in cities_loc]
    score_pos_1 = (-app_screen.width_player/2, app_screen.height/2)
    score_pos_2 = (app_screen.width_player/2, app_screen.height/2)

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

        app_screen.screen.update()

    game_1.clear_commands()
    game_2.clear_commands()
    
    if not get_optimal:
        return game_1.get_score(), game_2.get_score()
    else:
        pass
        # optimal = OptimalSalesman(game_1.cities)
        # solution = optimal.solve()
        # print(solution)
        # print(optimal.get_solution_cost())
        # return game_1.get_score(), game_2.get_score(), optimal

if __name__ == '__main__':
    main()
    
