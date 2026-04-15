import tkinter as tk
pocitadlo = 0


def akcia():
    global pocitadlo
    print(f'Jo napot kivanok{pocitadlo}')
    pocitadlo += 1
    farba = canvas.itemcget(obj2, 'fill')#
    print(farba)
    canvas.itemconfig(obj2, fill='black', width=5)
    if farba == 'green':
        canvas.itemconfig(obj2, fill='cyan')
    else:
        canvas.itemconfig(obj2, fill='green')
dzukel = tk.Tk()
dzukel.title('Moje ciarocky ale prve hej tak poyor na mna.')
canvas = tk.Canvas(dzukel, width=800, height=800, bg = 'white')
canvas.pack() #vytvorene objekty dava pod seba da sa aj inak napr grid
button = tk.Button(dzukel, text='Klikni ma', width = 50, bg = 'cyan', command=akcia)
button.pack()
obj1 = canvas.create_line(50,50,400,400)
obj2 = canvas.create_rectangle(50,50,400,400, outline='black', fill = 'green')
obj3 = canvas.create_oval(400,400,800,700, fill='salmon', outline='black')

dzukel.mainloop()