from AbstractTurtle import AbstractTurtle

class Score(AbstractTurtle):
    def __init__(self, position):
        AbstractTurtle.__init__(self, visible = False)
        self.goto(position)
        self.current_score = 0
        self.write("Custo atual: 0", align="center", font=("Courier", 13, "bold"))

    def update(self, cost):
        self.current_score += cost
        self.clear()
        self.write(f"Custo atual: {self.current_score}", 
                   align="center", 
                   font=("Courier", 13, "bold"))
        
    def end_game(self, final_cost):
        self.clear()
        self.color('red')
        self.write(f"Custo final: {final_cost}",
                   align="center", 
                   font=("Courier", 15, "bold"))