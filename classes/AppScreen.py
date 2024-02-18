import turtle
# from classes.solve_problem import OptimalSalesman
from classes.AbstractTurtle import AbstractTurtle

class AppScreen:

    def __init__(self, title : str,
                 instructions : bool = True,
                 optimal : bool = False,
                 width=0.85, height=0.90, starty=0
                 ):
        self.screen = turtle.Screen()
        self.screen.title(title)
        self.screen.setup(height=height, width=width, starty=starty)

        self.width_player = int(self.screen.window_width()/2 * 0.85)
        self.height = self.screen.window_height() * 0.9
        self.keep_game_over = True
        self.freeze_window = False

        self._instructions = instructions
        self._optimal = optimal

    def game_loop(self, game_fun, n_cities = 10):
        self.screen.update()
        self.wait_for_start() # shows instructions

        self.keep_game_over = True
        self.screen.clear()
        self._split_screen()

        num_cities = n_cities

        if self._optimal:
            score_1, score_2, optimal_obj = game_fun(self, get_optimal=self._optimal, num_cities=num_cities)
            self.show_result(score_1, score_2, optimal_obj)
        else:
            score_1, score_2 = game_fun(self, num_cities=num_cities)
            self.show_result(score_1, score_2)

        turtle.listen()
        self.screen.onkey(lambda: self.game_loop(game_fun, num_cities), 'Return')
        self.screen.update()

        self.screen.mainloop()

    def stop_game_over(self):
        self.keep_game_over = False

    def _show_instructions(self):
        self.screen.clear()
        instructions_turtle = turtle.Turtle(visible=False)
        self.screen.bgcolor("black")
        instructions_turtle.penup()
        instructions_turtle.color("white")
        instructions_turtle.goto(0, 200)
        instructions_turtle.write("Jogo do caixeiro viajante", align="center", font=("Arial", 24, "bold"))
        instructions_turtle.goto(0, 0)
        instructions = self._get_instructions()
        instructions_turtle.write(instructions, align="center", font=("Arial", 13, "normal"))
        instructions_turtle.goto(0, -100)
        instructions_turtle.write("Press 't' to start the game", align="center", font=("Arial", 18, "normal"))
        del(instructions_turtle)

    def _get_instructions(self):
        file = open('instructions.txt', 'r')
        text = file.read()
        file.close()
        return text
    
    def wait_for_start(self):
        self._show_instructions()
        self.screen.listen()
        self.screen.onkey(self.start_game, 't')

        self.freeze_window = True
        while self.freeze_window:
            self.screen.update()

    def start_game(self):
        self.freeze_window = False

    def game_over(self, score_1 : float, score_2 : float, optimal_value : float = None):
        
        self.show_result(score_1, score_2)

        while True:
            turtle.listen()
            turtle.onkey(self.play_again , 'Return')            
            if not self.keep_game_over:
                break
            self.screen.update()

        turtle.onkey(None, 'Return')
    
    def show_result(self, score_1, score_2, optimal_obj = None):
        self._divider_turtle.clear()
        writer_1 = turtle.Turtle(visible=False)
        writer_1.penup()
        writer_1.color("black")
        writer_2 = writer_1.clone()

        score_width = self.width_player / 2
        score_height = self.height/2 * 0.9
        score_player_1 = (-score_width, score_height)
        score_player_2 = (score_width, score_height)
        writer_1.goto(score_player_1)
        writer_2.goto(score_player_2)
        
        if score_1 < score_2:
            writer_1.write("Parabens! Você ganhou!!! :)", align="center", font=("Arial", 12, "bold"))
            writer_2.write("Ahhh, você perdeu... :(", align="center", font=("Arial", 12, "bold"))
        elif score_1 > score_2:
            writer_2.write("Parabens! Você ganhou!!! :)", align="center", font=("Arial", 12, "bold"))
            writer_1.write("Ahhh, você perdeu... :(", align="center", font=("Arial", 12, "bold"))
        else:
            writer_1.goto(0, score_height)
            writer_1.write('EMPATE!', align="center", font=("Arial", 12, "bold"))

        writer_1.goto(0, score_height * 0.875)
        writer_1.write('Pressione Enter para reiniciar', align="center", font=("Arial", 12, "bold"))
        del(writer_1, writer_2)

    def _split_screen(self):
        divider_turtle = AbstractTurtle(visible=False, color =  'black')
        divider_turtle.width(5)
        divider_turtle.goto(0, -self.screen.window_height() // 2)
        divider_turtle.pendown()
        divider_turtle.goto(0, self.screen.window_height()//2)
        self._divider_turtle = divider_turtle