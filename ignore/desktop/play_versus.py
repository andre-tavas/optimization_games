from classes import Arrow, Screen, City, Game, Salesman, Score, utils

def main():
    screen = Screen.Screen(split = True)
    cities_loc = utils.generate_cities_loc(width= screen.width_player,
                                           height= screen.height)
    width_diff = screen.width_player/2
    cities_loc_1 = [(x - width_diff, y) for (x,y) in cities_loc]
    cities_loc_2 = [(x + width_diff, y) for (x,y) in cities_loc]
    score_pos_1 = (-screen.width_player/2, screen.height/2 * 0.95)
    score_pos_2 = (screen.width_player/2, screen.height/2 * 0.95)
    commands_dict_2 = {'up' : 'w', 'down' : 's',
                       'right' : 'd', 'left' : 'a',
                       'travel' : 'space'}
    game_1 = create_game(cities_loc_1, score_pos_1)
    game_2 = create_game(cities_loc_2, score_pos_2, commands_dict_2)

    game_1.start()
    game_2.start()

    screen.mainloop()


def create_game(cities_loc, score_pos, commands_dict = None):
    cities = City.create_objects(cities_loc)
    salesman = Salesman(cities[0])
    arrow = Arrow()
    score = Score(position = score_pos)
    game = Game(cities, salesman, arrow, score, commands_dict)
    return game

if __name__ == '__main__':
    main()
    
