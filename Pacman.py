"""
File: pacman.py
----------------



import tkinter

#from tkinter import font
import time
#import random


#from simpleimage import SimpleImage
from PIL import Image, ImageTk

CANVAS_WIDTH = 800      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels

global count
global j
top = tkinter.Tk()
top.minsize(width=1420, height=800)
top.title('Pacman')
canvas = tkinter.Canvas(top, width=1420, height=800, bg="black")
canvas.pack()

# ________________________________________________________________________________________________ #
image2 = Image.open("images/Bonus.png")  # 1 - 30
bonus = ImageTk.PhotoImage(image2)

image3 = Image.open("images/Fire.png")
fire = ImageTk.PhotoImage(image3)



count = 0
timer = 0

for i in range(30):
    canvas.create_image((125 + 40*i), 50, image=bonus)  # top blue

for i in range(30):
    canvas.create_image((125 + 40*i), 130, image=bonus)  # top blue

for i in range(30):
    canvas.create_image((125 + 40 * i), 220, image=bonus)  # above pac

for i in range(6):
    canvas.create_image(90, (225 + 40*i), image=bonus)     # p

for i in range(4):
    canvas.create_image(295, (265 + 40*i), image=bonus)     # a

for i in range(4):
    canvas.create_image(497, (265 + 40*i), image=bonus)     # c

for i in range(4):
    canvas.create_image(705, (265 + 40*i), image=bonus)     # m

for i in range(4):
    canvas.create_image(910, (265 + 40*i), image=bonus)     # a

for i in range(4):
    canvas.create_image(1112, (265 + 40*i), image=bonus)     # n

for i in range(6):
    canvas.create_image(1320, (225 + 40*i), image=bonus)     # after n

for i in range(4):
    canvas.create_image(1085, (535 + 40*i), image=bonus)     # double white square left

for i in range(4):
    canvas.create_image(1285, (535 + 40*i), image=bonus)     # double white square left

for i in range(6):
    canvas.create_image((1085 + 40 * i), 490, image=bonus)  # double white square top

for i in range(30):
    canvas.create_image((125 + 40 * i), 430, image=bonus)  # below pac

for i in range(10):
    canvas.create_image((85 + 40 * i), 470, image=bonus)  # side blue top

for i in range(11):
    canvas.create_image((455 + 40 * i), 550, image=bonus)  # centre gold top

for i in range(11):
    canvas.create_image((455 + 40 * i), 630, image=bonus)  # centre gold top

for i in range(14):
    canvas.create_image((795 + 40 * i), 690, image=bonus)  # right cyan top

for i in range(4):
    canvas.create_image(50, (585 + 40*i), image=bonus)     # vertical coral left

for i in range(4):
    canvas.create_image(130, (585 + 40*i), image=bonus)    # vertical coral right

for i in range(6):
    canvas.create_image(270, (545 + 40*i), image=bonus)    # vertical VioletRed left

for i in range(6):
    canvas.create_image(350, (545 + 40*i), image=bonus)    # vertical VioletRed right



score_board = canvas.create_rectangle(1100, 770, 1410, 800, fill="white")  # 233
score = canvas.create_text(1200, 785, font=("Courier", 30), text="Score : ")  # 234
count_score = canvas.create_text(1300, 785, font=("Courier", 30), text=count)  # 235

image1 = Image.open("images/Pacman.png")
pac_img = ImageTk.PhotoImage(image1)

line1 = canvas.create_line(20, 20, 1400, 20, width=4.0, fill="white")
line2 = canvas.create_line(1400, 18, 1400, 765, width=4.0, fill="white")
line3 = canvas.create_line(1400, 765, 20, 765, width=4.0, fill="white")
line4 = canvas.create_line(20, 20, 20, 765, width=4.0, fill="white")

#  _________________________________________________________________________________________________________________ #

rect1 = canvas.create_rectangle(120, 80, 1320, 100, width=4.0, outline="blue")
rect2 = canvas.create_rectangle(120, 250, 140, 400, width=4.0, outline="green2")
rect3 = canvas.create_rectangle(140, 250, 245, 270, width=4.0, outline="green2")
rect4 = canvas.create_rectangle(245, 250, 265, 345, width=4.0, outline="green2")
rect5 = canvas.create_rectangle(245, 345, 140, 325, width=4.0, outline="green2")

#  _________________________________________________________________________________________________________________ #

line5 = canvas.create_line(325, 400, 387, 250, width=4.0, fill="white")
line6 = canvas.create_line(387, 250, 407, 250, width=4.0, fill="white")
line7 = canvas.create_line(407, 250, 470, 400, width=4.0, fill="white")
line8 = canvas.create_line(325, 400, 345, 400, width=4.0, fill="white")
line9 = canvas.create_line(470, 400, 450, 400, width=4.0, fill="white")
line10 = canvas.create_line(345, 400, 397, 270, width=4.0, fill="white")
line11 = canvas.create_line(450, 400, 397, 270, width=4.0, fill="white")

#  _________________________________________________________________________________________________________________ #

rect6 = canvas.create_rectangle(530, 250, 550, 400, width=4.0, outline="red2")
rect7 = canvas.create_rectangle(550, 250, 675, 270, width=4.0, outline="red2")
rect8 = canvas.create_rectangle(550, 380, 675, 400, width=4.0, outline="red2")

#  _________________________________________________________________________________________________________________ #

rect9 = canvas.create_rectangle(735, 250, 755, 400, width=4.0, outline="cyan")
rect10 = canvas.create_rectangle(860, 250, 880, 400, width=4.0, outline="cyan")
line12 = canvas.create_line(755, 250, 807, 305, width=4.0, fill="cyan")
line13 = canvas.create_line(807, 305, 860, 250, width=4.0, fill="cyan")
line14 = canvas.create_line(755, 275, 797, 325, width=4.0, fill="cyan")
line15 = canvas.create_line(797, 325, 817, 325, width=4.0, fill="cyan")
line16 = canvas.create_line(817, 325, 860, 275, width=4.0, fill="cyan")

#  _________________________________________________________________________________________________________________ #

line17 = canvas.create_line(940, 400, 1002, 250, width=4.0, fill="dark orange")
line18 = canvas.create_line(1002, 250, 1022, 250, width=4.0, fill="dark orange")
line29 = canvas.create_line(1022, 250, 1085, 400, width=4.0, fill="dark orange")
line20 = canvas.create_line(940, 400, 960, 400, width=4.0, fill="dark orange")
line21 = canvas.create_line(1085, 400, 1065, 400, width=4.0, fill="dark orange")
line22 = canvas.create_line(960, 400, 1012, 270, width=4.0, fill="dark orange")
line23 = canvas.create_line(1065, 400, 1012, 270, width=4.0, fill="dark orange")

#  _________________________________________________________________________________________________________________ #

rect11 = canvas.create_rectangle(1145, 250, 1165, 400, width=4.0, outline="gold")
rect12 = canvas.create_rectangle(1270, 250, 1290, 400, width=4.0, outline="gold")
line24 = canvas.create_line(1165, 250, 1270, 370, width=4.0, fill="gold")
line25 = canvas.create_line(1165, 280, 1270, 400, width=4.0, fill="gold")

#  _________________________________________________________________________________________________________________ #

rect13 = canvas.create_rectangle(80, 500, 470, 520, width=4.0, outline="blue")
rect14 = canvas.create_rectangle(450, 580, 880, 600, width=4.0, outline="gold")
rect15 = canvas.create_rectangle(1135, 540, 1235, 640, width=4.0, outline="white")
rect16 = canvas.create_rectangle(1115, 520, 1255, 660, width=4.0, outline="white")
rect17 = canvas.create_rectangle(80, 580, 100, 720, width=4.0, outline="coral")
rect18 = canvas.create_rectangle(300, 540, 320, 750, width=4.0, outline="VioletRed1")
rect19 = canvas.create_rectangle(800, 720, 1340, 740, width=4.0, outline="cyan")

fire1 = canvas.create_image(1165, 690, image=fire)  # 280
fire2 = canvas.create_image(160, 470, image=fire)   # 281


pacman = canvas.create_image(50, 50, image=pac_img)  # 282


def game_over():
    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x, y, x, y)
    if overlap[0] == 280 or overlap[0] == 281:
        canvas.delete(pacman)
        time.sleep(1.)
        canvas.create_rectangle(100, 100, 1300, 700, fill="white", outline="black")
        canvas.create_text(400, 400, font=("Courier", 100), text="          GAME OVER!")

# ball = canvas.create_oval(0, 0, 10, 10)
def game_win():
    global count
    if count == 2300:
        canvas.create_rectangle(100, 100, 1300, 700, fill="white", outline="black")
        canvas.create_text(400, 400, font=("Courier", 100), text="          YOU WIN!")


def eat_food():
    global count
    global j

    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x-20, y-20, x+10, y+10)

    if len(overlap) > 1:
        if 1 <= overlap[0] <= 232:
            canvas.delete(overlap[0])
            count += 10
            canvas.create_rectangle(1250, 770, 1410, 800, fill="white")
            canvas.create_text(1300, 785, font=("Courier", 30), text=count)


def top_is_blocked():
    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x - 6, y - 18, x + 6, y - 30)

    if len(overlap) > 1:
        if 1 <= overlap[0] <= 232 or overlap[0] == 280 or overlap[0] == 281:
            return False
        else:
            return True
    else:
        return False


def bottom_is_blocked():
    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x - 6, y + 18, x + 6, y + 30)
    if len(overlap) > 1:
        if 1 <= overlap[0] <= 232 or overlap[0] == 280 or overlap[0] == 281:
            return False
        else:
            return True
    else:
        return False

def front_is_blocked():
    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x + 18, y - 6, x + 30, y + 6)
    if len(overlap) > 1:
        if 1 <= overlap[0] <= 232 or overlap[0] == 280 or overlap[0] == 281:
            return False
        else:
            return True
    else:
        return False

def back_is_blocked():
    coordinates = canvas.coords(pacman)
    x = int(coordinates[0])
    y = int(coordinates[1])

    overlap = canvas.find_overlapping(x - 18, y - 6, x - 30, y + 6)
    if len(overlap) > 1:
        if 1 <= overlap[0] <= 232 or overlap[0] == 280 or overlap[0] == 281:
            return False
        else:
            return True
    else:
        return False

# __________________________________________________________________________________________________ #
def left(event):
    coordinates = canvas.coords(pacman)
    

    if int(coordinates[0]) == 30 or back_is_blocked():
        x = 0
        y = 0
        canvas.move(pacman, x, y)
    else:
        x = -10
        y = 0
        canvas.move(pacman, x, y)

    eat_food()
    game_over()
    game_win()

def right(event):
    coordinates = canvas.coords(pacman)

    if int(coordinates[0]) == 1400 or front_is_blocked():
        x = 0
        y = 0
        canvas.move(pacman, x, y)
    else:
        x = 10
        y = 0
        canvas.move(pacman, x, y)


    eat_food()
    game_over()
    game_win()

def up(event):
    coordinates = canvas.coords(pacman)

    if int(coordinates[1]) == 30 or top_is_blocked():
        x = 0
        y = 0
        canvas.move(pacman, x, y)
    else:
        x = 0
        y = -10
        canvas.move(pacman, x, y)

    eat_food()
    game_over()
    game_win()


def down(event):
    coordinates = canvas.coords(pacman)
    if int(coordinates[1]) == 780 or bottom_is_blocked():
        x = 0
        y = 0
        canvas.move(pacman, x, y)
    else:
        x = 0
        y = 10
        canvas.move(pacman, x, y)

    eat_food()
    game_over()
    game_win()

top.bind("<Left>", left)
top.bind("<Right>", right)
top.bind("<Up>", up)
top.bind("<Down>", down)


top.mainloop()

