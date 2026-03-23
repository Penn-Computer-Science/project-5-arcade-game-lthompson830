import tkinter as tk
import random

#constants
WIDTH = 600
HEIGHT = 300
count = 30

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
cars= []
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

frog_img = make_frog_sprite()
car_img = make_car_sprite()

def make_cars():
    start_x =0
    start_y = random.randint(10, 200)
    car = canvas.create_image(start_x, start_y, image=car_img, anchor="s" )
    cars.append(car)
    
def move_cars():
    for car in cars:
        canvas.move(car, 10, 0)
   
def move_left(event):
    canvas.move(frog, -15, 0)
def move_right(event):
    canvas.move(frog, 15, 0)
def move_up(event):
    canvas.move(frog, 0, -15)
def move_down(event):
    canvas.move(frog, 0, 15)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

def countdown(count):
    label.config(text=count)

    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        alive = False
        label.config(text="TIME'S UP")
        canvas.delete("all")
        
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "red")

alive = True

def start():
    global frog, cars
    cars.clear()
    frog =  canvas.create_image(300, HEIGHT, image=frog_img, anchor="c")
    game_loop()
    
def game_loop():
    global alive
    if not alive:
        canvas.delete("all")
        
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "red")
        return
    elif count <= 0:
        alive = False
    if fx1 < -1 or fx2 > 601:
        alive = False
    if random.randint(0, 1) ==1:
        make_cars()
    move_cars()

    for car in cars[:]:
        cx1, cy1, cx2, cy2 = canvas.bbox(car)
        fx1, fy1, fx2, fy2 = canvas.bbox(frog)

        if (cx1 < fx2 and cx2 > fx1 and cy1 < fy2 and cy2 > fy1):
            alive = False
        if cx1 > WIDTH:
            canvas.delete(car)
            cars.remove(car)
        
        if fy1 <= 0:
            canvas.delete("all")
            canvas.create_text(WIDTH//2, HEIGHT//2, text = "YOU WIN", fill = "Blue")

    root.after(40, game_loop)

    
root.after(0, countdown, count)
start()
root.mainloop()