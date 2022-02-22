import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player=Player()
car=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()

    #detecting collison of car with player

    for cars in car.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    #detecting end point of player
    if player.is_at_finishline():
        player.go_to_start()
        car.level_up()
        scoreboard.update_level()






screen.exitonclick()