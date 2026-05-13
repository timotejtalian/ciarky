import tkinter as tk
import random
sirka = 20
dlzka = 300
wires = []
cas = 60
colors = ['indianred', 'blue', 'green', 'purple', 'darkkhaki']
win = tk.Tk()    
random.shuffle(colors)
win.title('3! 2! 1! ..... buuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuum')
canvas = tk.Canvas(win, width=800, height=800, bg='white')

def explode(event):
    objekty = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
    if winner in objekty:
        print('Nem vybuchol, mozno nabuduce')
        canvas.create_text(20,20, text='Nem vybuchol, mozno nabuduce', fill='black', font=('Arial', 30), anchor='nw')

def timer():
    global cas
    cas = cas - 1
    canvas.itemconfig(ora, text=cas)
    if cas > 0:
        canvas.after(1000, timer)
    else:
        canvas.create_text(20,20, text='Asi si vzbuchol', fill='black', font=('Arial', 30), anchor='nw')


ora = canvas.create_text(500, 325, text=cas, fill='black', font=('Arial', 30), anchor='n')
for i in range(len(colors)):
    wires.append(canvas.create_rectangle(100, 300+i*sirka, 100+dlzka, 300+(i+1)*sirka, width=2, fill=colors[i], outline='black'))



winner = random.choice(wires)
print(winner)

canvas.bind('<Button-1>', explode)
canvas.pack()
timer()
win.mainloop()