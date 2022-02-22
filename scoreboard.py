from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_font=FONT
        self.level = 1
        self.ht()

        self.penup()
        self.color("white")
        self.goto(-280,270)

        self.write(f"Level:{self.level} ", align="left", font=(self.new_font))

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"level:{self.level} ", align="left", font=(self.new_font))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="center", font=('Arial', 10, 'normal'))


