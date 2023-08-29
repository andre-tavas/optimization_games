import turtle
from classes.AbstractTurtle import AbstractTurtle

class GameScreen:

    def __init__(self, screen, split : bool = True):
        self.screen = screen
        self.screen.bgcolor('white')
        self.width_player = int(self.screen.window_width()/2 * 0.9)*2
        self.height = self.screen.window_height() * 0.9
        if split:
            self._split_screen()
            self.width_player = int(self.width_player/2)

    def _split_screen(self):
        divider_turtle = AbstractTurtle(visible=False, color =  'black')
        divider_turtle.width(5)
        divider_turtle.goto(0, -self.screen.window_height() // 2)
        divider_turtle.pendown()
        divider_turtle.goto(0, self.screen.window_height()//2)

    def game_over(self, player_1 : str, player_2):
        writer_turtle = turtle.Turtle(visible=False)
        del(writer_turtle)


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
        self.screen.onkeypress(lambda: self.start_game(fun, screen), 't')
        self.screen.mainloop()

    def start_game(self, fun, screen):
        screen.clear()
        screen.onkeypress(None, 't')  # Desregistra a tecla Enter
        fun(screen)
        self.wait_for_start(fun, screen)

