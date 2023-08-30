import turtle
from classes.AbstractTurtle import AbstractTurtle

class GameScreen:

    def __init__(self, screen: turtle._Screen, split : bool = True):
        self.screen = screen
        self.screen.bgcolor('white')
        self.width_player = int(self.screen.window_width()/2 * 0.9)*2
        self.height = self.screen.window_height() * 0.9
        if split:
            self._split_screen()
            self.width_player = int(self.width_player/2)
        self.keep_game_over = True

    def _split_screen(self):
        divider_turtle = AbstractTurtle(visible=False, color =  'black')
        divider_turtle.width(5)
        divider_turtle.goto(0, -self.screen.window_height() // 2)
        divider_turtle.pendown()
        divider_turtle.goto(0, self.screen.window_height()//2)
        self._divider_turtle = divider_turtle

    def game_over(self, score_1 : float, score_2 : float, optimal_value : float = None):
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
        writer_1.write('Pressione Enter para voltar para tela inicial', align="center", font=("Arial", 12, "bold"))
        del(writer_1, writer_2)

        while True:
            turtle.listen()
            turtle.onkey(self.play_again , 'Return')            
            if not self.keep_game_over:
                break
            self.screen.update()

        return None

    def play_again(self):
        self.keep_game_over = False
        turtle.onkey(None, 'Return')
        self.screen.update()

class StartScreen:
    
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Caxeiro viajante")
        self.screen.setup(width=0.85, height=0.90, starty=0)
        
    def show_instructions(self):
        instructions_turtle = turtle.Turtle(visible=False)
        self.screen.bgcolor("black")
        instructions_turtle.penup()
        instructions_turtle.color("white")
        instructions_turtle.goto(0, 200)
        instructions_turtle.write("Jogo do caixeiro viajante", align="center", font=("Arial", 24, "bold"))
        instructions_turtle.goto(0, 0)
        instructions = self.get_instructions()
        instructions_turtle.write(instructions, align="center", font=("Arial", 13, "normal"))
        instructions_turtle.goto(0, -100)
        instructions_turtle.write("Pressione t para começar", align="center", font=("Arial", 18, "normal"))
        del(instructions_turtle)

    def get_instructions(self):
        file = open('instructions.txt', 'r')
        text = file.read()
        file.close()
        return text
    
    def wait_for_start(self, fun, screen):
        self.show_instructions()
        self.screen.listen()
        self.screen.onkey(lambda: self.start_game(fun, screen), 't')
        self.screen.mainloop()

    def start_game(self, fun, screen):
        screen.clear()
        screen.onkey(None, 't')
        fun(screen)
        self.wait_for_start(fun, screen)