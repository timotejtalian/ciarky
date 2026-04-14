from PIL import Image

def emberek_input():
    Ax = int(input("Zadejte x-ovou souřadnici bodu A: "))
    Ay = int(input("Zadejte y-ovou souřadnici bodu A: "))
    Bx = int(input("Zadejte x-ovou souřadnici bodu B: "))
    By = int(input("Zadejte y-ovou souřadnici bodu B: "))
    return Ax, Ay, Bx, By

def bundas_kenyer(Ax, Bx, Ay, By):
    if Ay == By:
        return 0, Ay
    if Ax == Bx:
        return 0, Ax
    if abs(Ax - Bx) > abs(Ay - By):
        a = (By - Ay) / (Bx - Ax)
        b = Ay - a * Ax
        print("predpis je y = " + str(round(a, 4)) + "x + " + str(round(b, 4)))
    else:
        a = (Bx - Ax) / (By - Ay)
        b = Ax - a * Ay
        print("predpis je x = " + str(round(a, 4)) + "y + " + str(round(b, 4)))
    return a, b

def sator(Ax, Ay, Bx, By):
    image = Image.new("RGB", (300, 300), (255, 255, 255))
    pixels = image.load()

    Ax = max(0, min(Ax, 299))
    Ay = max(0, min(Ay, 299))
    Bx = max(0, min(Bx, 299))
    By = max(0, min(By, 299))

    a, b = bundas_kenyer(Ax, Bx, Ay, By)

    if Ay == By:
        for x in range(min(Ax, Bx), max(Ax, Bx) + 1):
            pixels[x, Ay] = (0, 0, 0)
    elif Ax == Bx:
        for y in range(min(Ay, By), max(Ay, By) + 1):
            pixels[Ax, y] = (0, 0, 0)
    else:
        if abs(Ax - Bx) > abs(Ay - By):
            for x in range(min(Ax, Bx), max(Ax, Bx) + 1):
                y = a * x + b
                if 0 <= y < 300:
                    pixels[x, int(y)] = (0, 0, 0)
        else:
            for y in range(min(Ay, By), max(Ay, By) + 1):
                x = a * y + b
                if 0 <= x < 300:
                    pixels[int(x), y] = (0, 0, 0)

    pixels[Ax, Ay] = (255, 0, 0)  
    pixels[Bx, By] = (0, 0, 255)  

    image.save("ciara.png")
    image.show()
    return image

Ax, Ay, Bx, By = emberek_input()
sator(Ax, Ay, Bx, By)