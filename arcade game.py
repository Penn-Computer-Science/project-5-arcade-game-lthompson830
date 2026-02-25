import tkinter as tk
import random

#constants
WIDTH = 300
HEIGHT = 600

#window building
root = tk.Tk()
root.title("Frogger")

label = tk.Label(root, text = "TIME = 60")
label.pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

#frog creation
def make_frog_sprite():
    pattern = [
        "01000000010",
        "11044144011",
        "01041114010",
        "01111111110",
        "00011111000",
        "01111111110",
        "01011111010",
        "11001110011",
        "01000000010",
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("green", (x,y))
            if pattern[y][x] == "4":
                img.put("white", (x,y))
    return img

#car creation
def make_car_sprite():
    pattern = [
        "04440004440",
        "00100000100",
        "01111111110",
        "11311111111",
        "13311111111",
        "11311111111",
        "01111111110",
        "00100000100",
        "04440004440",
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("red", (x,y))
            if pattern[y][x] == "3":
                img.put("white", (x,y))
            if pattern[y][x] == "4":
                img.put("grey", (x,y))
    return img

#makeing the player spawn
player_img = make_frog_sprite







root.mainloop()