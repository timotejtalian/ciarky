from PIL import Image, ImageDraw
Image = Image.new('RGB', (400,400), 'white')
pixels = Image.load()
draw = ImageDraw.Draw(Image)

#egz sektor
x1 = 0
x2 = 0
for x1 in range (0,201,20):
    draw.line((0,200,x1,0), fill=(0,0,0), width=1)
    x1 += 20
for x2 in range (0,201,20):
    draw.line((200,200,x2,0), fill=(0,0,0), width=1)
    x2 += 20



stred = (300, 100)
#ketto sektor
for i in range (200,401,20):
    draw.ellipse([stred[0]-20, stred[1]-20, stred[0]+20, stred[1]+20], outline='black', width=1)
    draw.ellipse([stred[0]-20, stred[1]-20, stred[0]+20, stred[1]+20], outline='black', width=1)


#harom sektor
for x in range (0,200,20):
    for y in range (200,400,20):
        draw.rectangle([x, y, x+20, y+20], outline='black', width=1, fill = 'cyan')
        if (x//20 + y//20) % 2 == 0:
            draw.rectangle([x, y, x+20, y+20], outline='black', width=1, fill = 'olivedrab')


#negyto sektor
for x in range (200,400,20):
    for y in range (200,400,20):
        if (x//60 + y//60) % 2 == 0:
            draw.rectangle([x,y,x+20,y+20], outline='black', width=1, fill = 'cyan')





Image.show()