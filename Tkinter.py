import tkinter as tk
import turtle
t = turtle.Pen()
t.speed(100)

class Buttons:
        def __init__(self, master):
                #create a frame in the main window "master"
                frame = Frame(master)
                frame.pack()

def draw_a_left_spiral():
    for x in range (200):
        t.forward(x)
        t.left(91)

def draw_a_right_spiral():
  for x in range (200):
        t.forward(x)
        t.right(91)

def draw_a_left_tri():
    for x in range (200):
        t.forward(x)
        t.left(121)

def draw_a_right_tri():
   for x in range (200):
        t.forward(x)
        t.right(121)
        
def make_it_blue():
    t.pencolor("blue")

def make_it_red():
    t.pencolor("red")

def make_it_yellow():
    t.pencolor("yellow")
    
root = tk.Tk()
root.title("~~~Turtle Drawing~~~")
frame = tk.Frame(root)
frame.pack()

###color buttons
self.blue_button = tk.Button(colorframe, 
                   text="Blue", 
                   fg="blue",
                   command=make_it_blue)
#blue_button.pack(side=tk.LEFT)

self.red_button = tk.Button(colorframe, 
                   text="Red", 
                   fg="red",
                   command=make_it_red)
#red_button.pack(side=tk.LEFT)

self.yellow_button = tk.Button(colorframe, 
                   text="Yellow", 
                   fg="yellow",
                   command=make_it_yellow)
#yellow_button.pack(side=tk.LEFT)

###shape buttons
self.left_spiral_button = tk.Button(shapeframe, 
                   text="Left Spiral", 
                   fg="black",
                   command=draw_a_left_spiral)
#left_spiral_button.pack(side=tk.LEFT)

self.right_spiral_button = tk.Button(shapeframe, 
                   text="Right Spiral", 
                   fg="black",
                   command=draw_a_right_spiral)
#right_spiral_button.pack(side=tk.LEFT)

self.left_tri_button = tk.Button(frame, 
                   text="Left Triangle", 
                   fg="black",
                   command=draw_a_left_tri)
#left_tri_button.pack(side=tk.LEFT)

self.right_tri_button = tk.Button(shapeframe, 
                   text="Right Triangle", 
                   fg="black",
                   command=draw_a_right_tri)
#right_tri_button.pack(side=tk.LEFT)

###the quit button
self.quit_button = tk.Button(bottomframe,
                   text="Quit",
                   command=quit)
self.quit_button.pack(side=tk.LEFT)

###the frames
colorframe = Frame(root)
colorframe.pack()
shapeframe = Frame(root)
shapeframe.pack()
bottomframe =Frame(root)
bottomframe.pack(side=BOTTOM)

root.mainloop()
    
    
                    
    
