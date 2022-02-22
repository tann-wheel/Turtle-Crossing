from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        # super().__init
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        self.move_increment=MOVE_INCREMENT


    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_position=random.randint(-250,250)
            new_car.goto(310,y_position)
            self.all_cars.append(new_car)




    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed+=self.move_increment




