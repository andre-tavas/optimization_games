import turtle
from AbstractTurtle import AbstractTurtle

class Screen(turtle.Screen):

    def __init__(self, split : bool = True):
        Screen.__init__(self)
        self.title("Caixeiro Viajante")
        self.setup(width=0.85, height=0.95, starty=0)
        self.width_player = int(self.window_width() * 0.9)
        self.height = self.window_height() * 0.9
        if split:
            self._split_screen()
            self.width_player = int(self.width_player/2)

        '''
        Colocar aqui os números de width e hight (como atributos talvez)
        '''

    def _split_screen(self):
        divider_turtle = AbstractTurtle(visible=False, color =  'black')
        divider_turtle.width(5)
        divider_turtle.goto(0, -self.window_height() // 2)
        divider_turtle.pendown()
        divider_turtle.goto(0, self.window_height()//2)