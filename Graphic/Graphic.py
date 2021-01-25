from tkinter import *
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
matplotlib.use('TkAgg')
root=Tk()
root.title("Решение уравнения")
root.geometry("700x800")
x_list=[]
def text_to_lbl(event):
    global d,x1,x2,x,a,b,c,rx1,rx2,x_list, tick
    x_list = []
    a=float(enta.get())
    enta.delete(0, END)
    b=float(entb.get())
    entb.delete(0, END)
    c=float(entc.get())
    entc.delete(0, END)
    d=(b**2)-4*a*c
    lbl1["text"] = d
    if d>0:
        lblx.grid_remove()
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        rx1=round(x1,3)
        rx2=round(x2,3)
        x_list.append(rx1)
        x_list.append(rx2)
        lblx1["text"] = f"X1: {rx1}"
        lblx2["text"] = f"X2: {rx2}"
        lblx1.grid()
        lblx2.grid()
    elif d==0:
        lblx1.grid_remove()
        lblx2.grid_remove()
        x1 = x2 = (-b / 2*a)
        rx1 = round(x1, 3)
        rx2 = round(x2, 3)
        x_list.append(rx1)
        x_list.append(rx2)
        lblx["text"] = f"x: {x1}"
        lblx.grid()
    else:
        lblx.grid_remove()
        lblx1.grid_remove()
        lblx2.grid_remove()
        dd="Нет корней"
        lblx["text"] = dd
        lblx.grid()
def graf(event):
        global y,photo, lblimage
        y0=0,0
        points=x_list[0],x_list[1]
        print(points)
        freq = 100
        xi = np.linspace(x_list[0], x_list[1], freq)
        if x_list[1]>x_list[0]:
            y = [(a * t ** 2) + (b * t) + c for t in xi]
            plt.scatter(points, y0, color='red')
        else:
            plt.scatter(points, y0, color='red')
            y = [(-a * t ** 2) + (b * t) + c for t in xi]
        if x_list[1]==x_list[0]:
            if a>0:
                xii = np.linspace(x_list[0], -x_list[1], freq)
                yy=[t**2 for t in xii]
                plt.scatter(points, y0, color='red')
                plt.plot(xii+x_list[0],yy)
            else:
                xii = np.linspace(x_list[0], -x_list[1], freq)
                yy = [-t ** 2 for t in xii]
                plt.scatter(points, y0, color='red')
                plt.plot(xii + x_list[0], yy)
        plt.plot(xi, y)
        plt.tick_params(axis='both', labelsize=14)
        plt.grid(True)
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.savefig('sqrt.png')
        image = Image.open("sqrt.png")
        photo = ImageTk.PhotoImage(image)
        lblimage = Label(root, image=photo)
        lblimage.image =photo
        lblimage.grid(row=9, rowspan=5, column=0, columnspan=10)

lbl_Dformula=Label(root,text="D=b^2-4*a*c,",font="Arial 20")
lbl_formula=Label(root, text="Формула:(a*x^2+b*x+c=0)",font="Arial 20")
txta=Label(root,text="a:",font="Arial 20")
txtb=Label(root,text="b:",font="Arial 20")
txtc=Label(root,text="c:",font="Arial 20")
lbl1=Label(root,text="",font="Arial 15")
lbl2=Label(root, text="Дискриминант равен: ",font="Arial 15")
enta=Entry(root)
entb=Entry(root)
entc=Entry(root)
btn1=Button(root, text="Решение", font="Arial 15", width=15)
btn2=Button(root, text="График", font="Arial 15", width=15)
lblx=Label(root,text="",font="Arial 15")
lblx1=Label(root, text="",font="Arial 15")
lblx2=Label(root, text="",font="Arial 15")

lbl_Dformula.grid(row=0, column=0, columnspan=2,sticky="e")
lbl_formula.grid(row=0,column=3)
txta.grid(row=1,column=0)
txtb.grid(row=2,column=0)
txtc.grid(row=3,column=0)
enta.grid(row=1,column=1,columnspan=1)
entb.grid(row=2,column=1,columnspan=1)
entc.grid(row=3,column=1,columnspan=1)
btn1.bind("<Button-1>",text_to_lbl)
btn1.grid(row=4,column=1,columnspan=1)
btn2.bind("<Button-1>", graf)
btn2.grid(row=5, column=1,columnspan=1)
lbl2.grid(row=6,column=0,columnspan=2)
lbl1.grid(row=6,column=2)
lblx.grid(row=7,column=1,columnspan=10)
lblx1.grid(row=7,column=1,columnspan=5)
lblx2.grid(row=8,column=1,columnspan=5)
root.mainloop()
