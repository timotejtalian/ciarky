import datetime as dt, math, tkinter as tk
win = tk.Tk()
win.title('Hany ora van?')
s1 = 400
s2 = 400
kratka_ruc = 75
dlha_ruc = 150
polomer_cisla = dlha_ruc + 5
hrubka_h = 3
hrubka_m = 1
hrubka_s = 0.5

cas = dt.datetime.now()
print(cas.hour, cas.minute, cas.second)
uhol_minuta = math.radians(cas.minute * 6 - 90)
uhol_sekunda = math.radians(cas.second * 6 - 90)
uhol_hodina = math.radians((cas.hour * 30 + cas.minute * 0.5) - 90)


canvas = tk.Canvas(win, width=800, height=800, bg='white')
canvas.pack() 


canvas.create_line(s1, s2, s1 + dlha_ruc * math.cos(uhol_minuta), s2 + dlha_ruc * math.sin(uhol_minuta), fill='black', width=hrubka_m)
canvas.create_line(s1, s2, s1 + kratka_ruc * math.cos(uhol_sekunda), s2 + kratka_ruc * math.sin(uhol_sekunda), fill='red', width=hrubka_s)
canvas.create_line(s1, s2, s1 + hrubka_h * math.cos(uhol_hodina), s2 + kratka_ruc * math.sin(uhol_hodina), fill='black', width=hrubka_h)
canvas.create_text


win.mainloop()





