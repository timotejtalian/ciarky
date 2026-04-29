import tkinter as tk
win = tk.Tk()
win.title('Szeretem a halat')
canvas = tk.Canvas(win, width=800, height=800, bg='white')
canvas.pack()
positio_x = -1
position_y = -1


def click(event):
    global position_x, position_y
    print('Urobil si klik', event.x, event.y)
    objekty = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
    print('objekty', objekty)
    if szabo in objekty:
        position_x = event.x
        position_y = event.y





def move_it(event):
    global position_x, position_y
    if position_x != -1:
        vector_x = event.x - position_x
        vector_y = event.y - position_y
        position_x = event.x
        position_y = event.y
        canvas.move(szabo, vector_x, vector_y)
    print('Au to boli, dost, prestan!!!!!!!')

def sundikuj(event):
    global position_x, position_y
    position_x = -1
    position_y = -1
    print('Sundikujem!')

szabo = canvas.create_rectangle(0, 0, 100, 100, fill='indianred', outline='darkkhaki', width=2)




canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move_it)
canvas.bind('<ButtonRelease-1>', sundikuj)

win.mainloop()