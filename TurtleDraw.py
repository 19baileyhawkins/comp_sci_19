import turtle
t = turtle.Pen()
t.speed(100)
                    
def left_spiral():
    global size
    t_pencolor()
    t_size()
    for x in range (size):
        t.forward(x)
        t.left(91)

def right_spiral():
    global size
    t_pencolor()
    t_size()
    for x in range (size):
        t.forward(x)
        t.right(91)

def left_tri():
    global size
    t_pencolor()
    t_size()
    for x in range (size):
        t.forward(x)
        t.left(121)
        
def right_tri():
    global size
    t_pencolor()
    t_size()
    for x in range (size):
        t.forward(x)
        t.right(121)

def t_pencolor():
    color = input("""What would you like the color to be? blue, red, or yellow. """)
    if color == "blue":
        t.pencolor("blue")
    if color == "red":
        t.pencolor("red")
    if color == "yellow":
        t.pencolor("yellow")
            
def t_size():
    global size
    size = int(input("""What size would you like it to be? 50, 100, or 200. """))
    

while True:
    drawing = input("""What would you like to draw?
1 a left spiral 
2 a right spiral
3 a left triangle
4 a right triangle 
""")
    if drawing == "1":
        left_spiral()
    elif drawing == "2":
        right_spiral()
    elif drawing == "3":
        left_tri()
    elif drawing == "4":
        right_tri()




    
    
                    
    
