from turtle import Turtle, Screen, TK, mainloop
import time
from math import floor, ceil
import random

scr = Screen()
height = 20
width = 20
cells = 20
scr.setup(600, 600)

scr.mode('world')
scr.setworldcoordinates(0, 0, width, height)

BUTTON_SIZE = 60
CURSOR_SIZE = 20
FONT_SIZE = 18
FONT = ('Arial', FONT_SIZE, 'bold')
STATES = (('red', 'OFF'), ('green', 'ON'))


scr.bgcolor('black')

def toggle_power(x, y):
    global button_clicked, button, marker
    button.hideturtle()
    marker.hideturtle()
    #marker.goto((-500, -500))
    button_clicked = True




marker = Turtle(visible=False)
marker.hideturtle()
marker.penup()
marker.speed(0)
marker.goto(width // 2, height // 2 - 1 * (height / 10))
marker.color('white')
marker.write('Start', align='center', font=FONT)


button = Turtle('square')
button.shapesize(BUTTON_SIZE / CURSOR_SIZE, outline=2)
button.color('black', 'green')
button.penup()
button.hideturtle()
button.speed(0)
button.goto(width // 2, height // 2)  # move the button into position
# button.write("Click me!", align='center', font=FONT)
button.showturtle()




button_clicked = False

while not button_clicked:
    button.onclick(toggle_power)

scr.reset()

button.goto((-width // 2, -height // 2))


game_over = False



score = 0

scr.title(f"Score: {score}")
scr.bgcolor("black")


grid = []

snake_head_direction = (1, 0)
snake_tail_direction = snake_head_direction
intervel_ms = 200
offset_w = width / cells / 2
offset_h = height / cells / 2
new_piece_make = False



directions = []
can_take_input = True

tail_number = 0

fruit_exist = False
fruit_spawn_location = (0, 0)





def grid_maker():

    global grid
    for _ in range(cells + 1):
        line = []
        for _ in range(cells + 1):
            line.append(0)
        grid.append(line)


def gui_grid_maker():
    trt = Turtle(visible=False)
    trt.penup()
    trt.speed(0)
    trt.goto(0, height)
    trt.right(90)
    trt.color("white")


    for i in range(cells + 1):
        trt.pendown()
        trt.forward(height)
        trt.penup()
        
        if i % 2 == 0:
            trt.left(90)
            trt.forward(width / cells)
            trt.left(90)
        else:
            trt.right(90)
            trt.forward(width / cells)
            trt.right(90)
                
    trt.goto(0, 0)
    trt.right(90)


    for i in range(cells + 1):
        trt.pendown()
        trt.forward(width)
        trt.penup()
        
        if i % 2 == 0:
            trt.left(90)
            trt.forward(height / cells)
            trt.left(90)
        else:
            trt.right(90)
            trt.forward(height / cells)
            trt.right(90)


def speed_increase(spd):
    global snake_pieces
    for i in snake_pieces:
        piece = i[0]

        piece.speed(spd)

def update_directions():

    #That is to say when a certain direction has been applied to all pieces
    invalid_directions_number = 0

    global directions, grid

    for i in range(len(directions)):
        item = directions[i]
        #Get the direction of the snake piece with the item's number
        snake_piece_index = item[1]
        direction = item[0]
        snake_pieces[snake_piece_index][1] = direction
        current_snake_piece = snake_pieces[snake_piece_index][0]
        curr_p_pos = current_snake_piece.pos()

        directions[i][1] += 1

        # current_snake_piece.speed(0)

        
        # if direction[0] == 1:
        #     current_snake_piece.setheading(0)
        # elif direction[0] == -1:
        #     current_snake_piece.setheading(180)
        # elif direction[1] == 1:
        #     current_snake_piece.setheading(90)
        # else:
        #     current_snake_piece.setheading(270)
  

        # current_snake_piece.speed(2)

        if item[1] >= tail_number:
            invalid_directions_number += 1

    #Now we delete the expired directions 
    for i in range(invalid_directions_number):
        directions.pop(0)
    
    #scr.ontimer(update_directions, intervel_ms)





def move():
    global snake_pieces, tail_number, intervel_ms, snake_head
    
    tail = snake_pieces[-1][0]
    tail_position = tail.pos()
    grid[ceil(tail_position[0])][ceil(tail_position[1])] = 0 

    for piece in snake_pieces[-1::-1]:
        p = piece[0]
        direction = piece[1]
        
        current_position = p.pos()

        # print(current_position)
        
        # grid[ceil(current_position[0])][ceil(current_position[1])] = 0 

        # if tail_number > 10:
        #     speed_increase(0)
        # elif tail_number > 9:
        #     speed_increase(9)
        # elif tail_number > 7:
        #     speed_increase(7)
        # elif tail_number > 5:
        #     speed_increase(5)
        # elif tail_number > 3:
        #     speed_increase(3)

        # p.forward(1)

        p.goto(current_position[0] + direction[0], current_position[1] + direction[1])

        # current_position = p.pos()

        # print(current_position)
        
        grid[ceil(current_position[0])][ceil(current_position[1])] = 1

        
    # snake_head_position = snake_head.pos()

    # grid[ceil(snake_head_position[0])][ceil(snake_head_position[1])] = 0 
    
    update_directions()

    scr.ontimer(move, intervel_ms)



def input_timer():
    global can_take_input, intervel_ms
    can_take_input = True
    scr.ontimer(input_timer, intervel_ms // 4)



def snake_piece_maker(position, direction):
    global grid

    snake_piece = Turtle()
    
    snake_piece.hideturtle()
    snake_piece.penup()
   
    snake_piece.shape('square')
    snake_piece.color("white")
    average = (width + height) // 2
    snake_piece.shapesize(2 / (average / 10)) 
    snake_piece.speed(0.1)
    
    snake_piece.goto(position)

    # print(position)
    
    grid[ceil(position[0])][ceil(position[1])] = 1

    snake_piece.showturtle()

    snake_pieces.append([snake_piece, direction])

    global tail_number, intervel_ms 
    
    tail_number += 1

    if intervel_ms >= 70:
        intervel_ms -= 5

    #print(tail_number)

    # print(grid)

    return snake_piece



def move_up():
    global can_take_input
    if can_take_input:
        directions.append([(0, 1), 0])
        can_take_input = False

def move_down():
    global can_take_input
    if can_take_input:
        directions.append([(0, -1), 0])
        can_take_input = False


def move_right():
    global can_take_input
    if can_take_input:
        directions.append([(1, 0), 0])
        can_take_input = False


def move_left():
    global can_take_input
    if can_take_input:
        directions.append([(-1, 0), 0])
        can_take_input = False



def game_over_check():
    global snake_head, game_over, scr, snake_pieces
    snake_head_position = snake_head.pos()

    if floor(snake_head_position[0]) >= width or floor(snake_head_position[1]) >= height or floor(snake_head_position[0]) < 0 or floor(snake_head_position[1]) < 0:
        game_over = True
        scr.bye()

    for snake_piece in snake_pieces[1:]:
        if snake_head_position == snake_piece[0].pos():
            game_over = True
            scr.bye()
            break

    
    scr.ontimer(game_over_check, intervel_ms)



def first_fruit_spawn():
    global fruit_spawn_location, grid, fruit_exist, fruit, intervel_ms
    if not fruit_exist:
        while True:
            fruit_spawn_location = (random.randint(1, width), random.randint(1, height))
            # print(fruit_spawn_location)
            if grid[fruit_spawn_location[0]][fruit_spawn_location[1]] == 0:
                grid[fruit_spawn_location[0]][fruit_spawn_location[1]] = 2
                break
    
        fruit_exist = True
        
        fruit = Turtle()
        fruit.hideturtle()
        fruit.penup()
    
        fruit.shape('circle')
        fruit.color('purple')
        average = (width + height) // 2
        fruit.shapesize(3 / (average / 10)) 
        fruit.speed(0)
        
        fruit.goto((fruit_spawn_location[0] - offset_w, fruit_spawn_location[1] - offset_h))
        
        fruit.showturtle()


        scr.ontimer(spawn_fruit, intervel_ms)

        return fruit
    else:
        scr.ontimer(spawn_fruit, intervel_ms)

        return None


def spawn_fruit():
    global fruit_spawn_location, grid, fruit_exist, fruit, intervel_ms
    if not fruit_exist:
        while True:
            fruit_spawn_location = (random.randint(1, width), random.randint(1, height))
            # print(fruit_spawn_location)
            if grid[fruit_spawn_location[0]][fruit_spawn_location[1]] == 0:
                grid[fruit_spawn_location[0]][fruit_spawn_location[1]] = 2
                break
    
        fruit_exist = True
        
        # fruit = Turtle()
        # fruit.hideturtle()
        # fruit.penup()
    
        # fruit.shape('circle')
        # fruit.color('red')
        # fruit.shapesize(2) 
        # fruit.speed(0)
        
        fruit.goto((fruit_spawn_location[0] - offset_w, fruit_spawn_location[1] - offset_h))
        
        fruit.showturtle()


        scr.ontimer(spawn_fruit, intervel_ms)

        return fruit
    else:
        scr.ontimer(spawn_fruit, intervel_ms)

        return None



def fruit_pickup_checker():
    global snake_head, fruit_spawn_location, fruit_exist, score, fruit, snake_tail, intervel_ms
    position = (snake_head.pos()[0] + offset_w, snake_head.pos()[1] + offset_h)


    #print(position)
    #if abs(position[0] - fruit_spawn_location[0]) < 0.01 and abs(position[1] - fruit_spawn_location[1]) < 0.01:
    if abs(position[0] - fruit_spawn_location[0]) < 0.1 and abs(position[1] - fruit_spawn_location[1]) < 0.1:

        # print("fruit_eaten")


        tail = snake_pieces[-1]
        tail_piece = tail[0]
        tail_position = tail_piece.pos()
        tail_direction = tail[1]



        new_tail = snake_piece_maker((tail_position[0] - tail_direction[0], tail_position[1] - tail_direction[1]), tail_direction)
        snake_tail = new_tail 
        
        fruit_exist = False
        score += 1

        scr.title(f"Score: {score}")

        fruit.hideturtle()
        # del fruit
    scr.ontimer(fruit_pickup_checker, intervel_ms)
        

def stop_window():
    global intervel_ms
    scr.tracer(0)

    scr.ontimer(stop_window, intervel_ms)

def update_window():
    global intervel_ms

    scr.update()

    scr.ontimer(update_window)

snake_pieces = []
snake_head = None
snake_tail = None

snake_pieces = []


grid_maker()
gui_grid_maker()


#Snake Head and Tail Setup
snake_head = snake_piece_maker((offset_w, offset_h), snake_head_direction)
snake_tail = snake_piece_maker((offset_w - snake_head_direction[0], offset_h - snake_head_direction[1]), snake_head_direction)


stop_window()
first_fruit_spawn()
# fruit = replacement
# if replacement != None:
#     fruit = spawn_fruit()


update_directions()
move()
input_timer()
game_over_check()
fruit_pickup_checker()

update_window()

scr.listen()
scr.onkey(fun = move_up, key='Up')
scr.onkey(fun = move_down, key='Down')
scr.onkey(fun = move_left, key='Left')
scr.onkey(fun = move_right, key='Right')




# scr.exitonclick()

mainloop()
