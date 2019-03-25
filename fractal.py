from tkinter import *
from turtle import *
menu = Tk()

def generateFractal():
    points = []
    length = 200
    branches = 0
    ratio = 0
    angle = 0
    offset = 0
    iterations = 0
    branches = int(E.get())
    ratio = float(E1_2.get())
    angle = float(E2.get())
    offset = float(E3.get())
    iterations = int(E4.get())
    points.append(((0,0),90))
    turtle = Turtle()
    turtle.home()
    turtle.speed(10)
    while(iterations > 0):
        i = len(points)
        for j in range(0,i):
            coor = points.pop(0)
            turtle.up()
            turtle.setpos(coor[0][0], coor[0][1])
            turtle.seth(coor[1])
            turtle.down()
            turtle.right(offset)
            for k in range(0,branches):
                turtle.fd(length)
                points.append((turtle.pos(), turtle.heading()))
                turtle.bk(length)
                turtle.left(angle)
            #endFor
        #endFor
        iterations = iterations - 1
        length = length * ratio
    #endWhile
    return


F = Frame(menu)
F.pack(side = TOP)
F1_2 = Frame(menu)
F1_2.pack(side = TOP)
F2 = Frame(menu)
F2.pack(side = TOP)
F3 = Frame(menu)
F3.pack(side = TOP)
F4 = Frame(menu)
F4.pack(side = TOP)
F5 = Frame(menu)
F5.pack(side = TOP)

L = Label(F, text="Branches:", width = 12, relief = GROOVE)
L.pack(side = LEFT)
E = Entry(F)
E.pack(side = RIGHT)

L1_2 = Label(F1_2, text="Ratio:", width = 12, relief = GROOVE)
L1_2.pack(side = LEFT)
E1_2 = Entry(F1_2)
E1_2.pack(side = RIGHT)

L2 = Label(F2, text="Angle:", width = 12, relief = GROOVE)
L2.pack(side = LEFT)
E2 = Entry(F2)
E2.pack(side = RIGHT)

L3 = Label(F3, text="°Offset:", width = 12, relief = GROOVE)
L3.pack(side = LEFT)
E3 = Entry(F3)
E3.pack(side = RIGHT)

L4 = Label(F4, text="Iterations:", width = 12, relief = GROOVE)
L4.pack(side = LEFT)
E4 = Entry(F4)
E4.pack(side = RIGHT)

B5 = Button(F5, text="Generate", width = 30, command = generateFractal)
B5.pack(side = LEFT)

menu.mainloop()
