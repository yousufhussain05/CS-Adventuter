
import turtle
import random
import pygame

turtle.speed(10)
s = turtle.getscreen()
size_for_canvas = 500
s.setup(width=size_for_canvas + 10, height=size_for_canvas + 10)
s.screensize(size_for_canvas, size_for_canvas)
global initial_character_position
initial_character_position = 0  
global easy_count, medium_count, hard_count

easy_count = 0
medium_count = 0
hard_count = 0

def write(x, y, text, font = ("FontleroyBrown", 10, "bold")):
    turtle_write = turtle.Turtle()
    turtle_write.penup()
    turtle_write.goto(x, y)
    turtle_write.pendown()
    turtle_write.write(text, align = "center", font = font)
    turtle_write.hideturtle()
    return turtle_write

def you_win_screen():
    s.clearscreen()
    s.bgpic("you_win.gif")
    pygame.init()
    pygame.mixer.music.load('you_win_music.mp3')
    pygame.mixer.music.play(1)
    turtle.penup()
    turtle.goto(-100,200)
    turtle.pendown()
    for side in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.penup()
    turtle.goto(75,200)
    turtle.pendown()
    for side in range(4):
        turtle.forward(20)
        turtle.right(90)
        turtle.hideturtle()
    file1 = open(("restart")+"."+"txt")
    lst1 = file1.readlines()
    for line in lst1:
        split_list = line.strip('\n')
    write(0, -205, split_list, font=("FontleroyBrown", 10, "bold"))
    restart_rect1 = rectangle("rectangle.gif", 0, -200)
    restart_rect1.onclick(restart_game)

def you_lose_screen():
    s.clearscreen()
    s.bgpic("game_over.gif")
    pygame.init()
    pygame.mixer.music.load('you_lost_music.mp3')
    pygame.mixer.music.play(1)
    file = open(("restart")+"."+"txt")
    lst = file.readlines()
    for line in lst:
        split_list= line.strip('\n')
    write(5, -225, split_list, font=("FontleroyBrown", 10, "bold"))
    restart_rect1 = rectangle("rectangle.gif", 0, -215)
    restart_rect1.onclick(restart_game)
    
def restart_game(x, y):
    reset_character_position(-200,-170)
    # retro_character.goto(-200,-170)
    screen_2(x,y)

def screen_1():
    global play_button
    screen = turtle.Screen()
    screen.bgcolor("light gray")
    play_button = turtle.Turtle()
    turtle.addshape("play_button.gif")
    play_button.shape("play_button.gif")
    play_button.showturtle()
    play_button.penup()
    play_button.goto(0, -100)

    write(0,150, "CODE QUEST CHRONICLES:", font = ("Bahnschrift", 15, "bold" ))
    write(0, 130, "A JOURNEY THROUGH THE DAY IN THE LIFE OF CS ADVENTURER!", font = ("Bahnschrift", 10, "bold" ))
    play_button.onclick(screen_2)

def screen_2(x, y):
    global play_button
    play_button.hideturtle()
    s.clearscreen()
    screen = turtle.Screen()
    screen.bgcolor("light gray")

    difficulty = turtle.Turtle()
    turtle.addshape("difficulty.gif")
    difficulty.shape("difficulty.gif")
    difficulty.showturtle()
    difficulty.penup()
    difficulty.goto(0, 110)

    global easy
    easy = turtle.Turtle()
    turtle.addshape("easy.gif")
    easy.shape("easy.gif")
    easy.showturtle()
    easy.penup()
    easy.goto(0, 40)

    global medium
    medium = turtle.Turtle()
    turtle.addshape("medium.gif")
    medium.shape("medium.gif")
    medium.showturtle()
    medium.penup()
    medium.goto(0, -25)

    global hard
    hard = turtle.Turtle()
    turtle.addshape("hard.gif")
    hard.shape("hard.gif")
    hard.showturtle()
    hard.penup()
    hard.goto(0, -85)

    write(0, -170, "RULES", font=("Bahnschrift", 10, "bold"))
    write(0, -190, " 3 QUESTIONS FOR EACH. BUT COMPLETING VARIES ON DIFFICULTY", font=("Bahnschrift", 9, "bold"))

    easy.onclick(easy_click)
    medium.onclick(medium_click1)
    hard.onclick(hard_click1)

def easy_click(x, y):
    global easy_rect1, easy_rect_copy1
    change_screen(x, y, move_character = False)

    write(-10, 75, "    YOU HAVE AN IMPORTANT LECTURE TO ATTEND.\n                 WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "     SLEEP IN YOUR \n COMFY WARM BED", font = ("FontleroyBrown", 10, "bold"))
    write(143, -227, "MOTIVATE YOURSELF\n      TO GET UP ", font=("FontleroyBrown", 10, "bold"))

    easy_rect1 = rectangle("rectangle.gif", -128, -206)
    easy_rect_copy1 = rectangle("rectangle_copy.gif", 135, -208)

    easy_rect1.onclick(easy_on_click1_1)
    easy_rect_copy1.onclick(easy_on_click1_2)

def easy_on_click1_1(x,y):
    global easy_count, easy_rect2, easy_rect_copy2
    no_move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    easy_rect2 = rectangle("rectangle.gif", -128, -206)
    easy_rect_copy2 = rectangle("rectangle_copy.gif", 135, -208)

    easy_rect2.onclick(easy_on_click1_3)
    easy_rect_copy2.onclick(easy_on_click1_4)

def easy_on_click1_2(x,y):
    global easy_count, easy_rect3, easy_rect_copy3
    easy_count += 1
    move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    easy_rect3 = rectangle("rectangle.gif", -128, -206)
    easy_rect_copy3 = rectangle("rectangle_copy.gif", 135, -208)

    easy_rect3.onclick(easy_on_click1_3)
    easy_rect_copy3.onclick(easy_on_click1_4) 

def easy_on_click1_3(x,y):
    global easy_count, easy_rect4, easy_rect_copy4
    easy_count += 1
    move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    easy_rect4 = rectangle("rectangle.gif", -128, -206)
    easy_rect_copy4 = rectangle("rectangle_copy.gif", 135, -208)

    easy_rect4.onclick(easy_final_counter)
    easy_rect_copy4.onclick(easy_counter) 

def easy_on_click1_4(x,y):
    global easy_count, easy_rect5, easy_rect_copy5
    no_move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    easy_rect5 = rectangle("rectangle.gif", -128, -206)
    easy_rect_copy5 = rectangle("rectangle_copy.gif", 135, -208)

    easy_rect5.onclick(easy_final_counter)
    easy_rect_copy5.onclick(easy_counter) 

def easy_final_counter(x,y):
    global easy_count
    easy_count+= 1
    easy_counter_1()

def easy_counter_1():
    if easy_count >= 0:
        you_win_screen()
    else:
        you_lose_screen()

def easy_counter(x,y):
    global easy_count
    if easy_count >= 1:
        you_win_screen()
    else:
        you_lose_screen()

def medium_click1(x, y):
    global medium_rect1, medium_rect_copy1
    change_screen(x, y, move_character = False)

    write(-10, 75, "    YOU HAVE AN IMPORTANT LECTURE TO ATTEND.\n                 WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "     SLEEP IN YOUR \n COMFY WARM BED", font = ("FontleroyBrown", 10, "bold"))
    write(143, -227, "MOTIVATE YOURSELF\n      TO GET UP ", font=("FontleroyBrown", 10, "bold"))

    medium_rect1 = rectangle("rectangle.gif", -128, -206)
    medium_rect_copy1 = rectangle("rectangle_copy.gif", 135, -208)

    medium_rect1.onclick(medium_on_click1_1)
    medium_rect_copy1.onclick(medium_on_click1_2)

def medium_on_click1_1(x,y):
    global medium_count, medium_rect2_1, medium_rect_copy2_1
    
    no_move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    medium_rect2_1 = rectangle("rectangle.gif", -128, -206)
    medium_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    medium_rect2_1.onclick(medium_on_click1_3)
    medium_rect_copy2_1.onclick(medium_on_click1_4)

def medium_on_click1_2(x,y):
    global medium_count, medium_rect2_2, medium_rect_copy2_2
    medium_count += 1
    move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    medium_rect2_2 = rectangle("rectangle.gif", -128, -206)
    medium_rect_copy2_2 = rectangle("rectangle_copy.gif", 135, -208)

    medium_rect2_2.onclick(medium_on_click1_3)
    medium_rect_copy2_2.onclick(medium_on_click1_4) 

def medium_on_click1_3(x,y):
    global medium_count, medium_rect2_1, medium_rect_copy2_1
    medium_count += 1
    move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    medium_rect2_1 = rectangle("rectangle.gif", -128, -206)
    medium_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    medium_rect2_1.onclick(medium_counter)
    medium_rect_copy2_1.onclick(medium_counter) 

def medium_on_click1_4(x,y):
    global medium_count, medium_rect2_2, medium_rect_copy2_2
    no_move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    medium_rect2_1 = rectangle("rectangle.gif", -128, -206)
    medium_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    medium_rect2_1.onclick(medium_counter)
    medium_rect_copy2_1.onclick(medium_counter) 

def medium_counter(x,y):
    if medium_count >= 2:
        you_win_screen()
    else:
        you_lose_screen()
    
def hard_click1(x, y):
    global hard_rect1, hard_rect_copy1
    change_screen(x, y, move_character = False)

    write(-10, 75, "    YOU HAVE AN IMPORTANT LECTURE TO ATTEND.\n                 WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "     SLEEP IN YOUR \n COMFY WARM BED", font = ("FontleroyBrown", 10, "bold"))
    write(143, -227, "MOTIVATE YOURSELF\n      TO GET UP ", font=("FontleroyBrown", 10, "bold"))

    hard_rect1 = rectangle("rectangle.gif", -128, -206)
    hard_rect_copy1 = rectangle("rectangle_copy.gif", 135, -208)

    hard_rect1.onclick(hard_on_click1_1)
    hard_rect_copy1.onclick(hard_on_click1_2)

def hard_on_click1_1(x,y):
    global hard_count, hard_rect2_1, hard_rect_copy2_1
    
    no_move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    hard_rect2_1 = rectangle("rectangle.gif", -128, -206)
    hard_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    hard_rect2_1.onclick(hard_on_click1_3)
    hard_rect_copy2_1.onclick(hard_on_click1_4)

def hard_on_click1_2(x,y):
    global hard_count, hard_rect2_2, hard_rect_copy2_2
    hard_count += 1
    move_character(x,y)
    write(0, 75, "YOU HAVE A LECTURE LAB DUE TONIGHT.\n          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "   LISTEN DURING\n       LECTURE", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "TALK DURING LECTURE ", font=("FontleroyBrown", 10, "bold"))

    hard_rect2_2 = rectangle("rectangle.gif", -128, -206)
    hard_rect_copy2_2 = rectangle("rectangle_copy.gif", 135, -208)

    hard_rect2_2.onclick(hard_on_click1_3)
    hard_rect_copy2_2.onclick(hard_on_click1_4) 

def hard_on_click1_3(x,y):
    global hard_count, hard_rect2_1, hard_rect_copy2_1
    hard_count += 1
    move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    hard_rect2_1 = rectangle("rectangle.gif", -128, -206)
    hard_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    hard_rect2_1.onclick(final_counter)
    hard_rect_copy2_1.onclick(hard_counter) 

def hard_on_click1_4(x,y):
    global hard_count, hard_rect2_2, hard_rect_copy2_2
    no_move_character(x,y)
    write(0, 75, "YOU ARE STRUGGLING WITH A DIFFICULT BUG IN YOUR CODE.\n                          WHAT DO YOU WANT TO DO?", font =("FontleroyBrown", 10, "bold"))
    write(-135, -225, "       WORK ON YOUR\n      ERROR HANDLING", font = ("FontleroyBrown", 10, "bold"))
    write(143, -220, "GO TO TA IMMEDIATELY ", font=("FontleroyBrown", 10, "bold"))

    hard_rect2_1 = rectangle("rectangle.gif", -128, -206)
    hard_rect_copy2_1 = rectangle("rectangle_copy.gif", 135, -208)

    hard_rect2_1.onclick(hard_count)
    hard_rect_copy2_1.onclick(hard_counter) 

def final_counter(x,y):
    global hard_count
    hard_count+= 1
    hard_counter_1()

def hard_counter_1():
    if hard_count == 3:
        you_win_screen()
    else:
        you_lose_screen()

def hard_counter(x,y):
    if hard_count == 3:
        you_win_screen()
    else:
        you_lose_screen()
character_position = 0

def character():
    global character_position, retro_character
    retro_character = turtle.Turtle()
    turtle.addshape("retro_character.gif")
    retro_character.shape("retro_character.gif")
    retro_character.showturtle()
    retro_character.penup()
    retro_character.goto(-205 + character_position, -96)
    
def change_screen(x, y, move_character):
    global easy, medium, hard, character, count, character_position
    s.clearscreen()
    s.bgpic("retro_background.gif")
    if move_character:
        character_position += 210
        character()
    else:
        character()

def reset_character_position(x,y):
    global character_position, retro_character
    character_position = initial_character_position
    retro_character.goto(x,y)

def rectangle(shape, x, y):
    rectangle = turtle.Turtle()
    turtle.addshape(shape)
    rectangle.shape(shape)
    rectangle.showturtle()
    rectangle.penup()
    rectangle.goto(x,y)
    return rectangle

def move_character(x,y):
    change_screen(x, y, move_character=True)

def no_move_character(x,y):
    change_screen(x, y, move_character=False)


if __name__ == "__main__":
    screen_1()
    turtle.mainloop()
