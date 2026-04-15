from PIL import Image, ImageDraw

y = 0
image = Image.new("RGB", (400, 400), 'white')
pixels = image.load()
draw = ImageDraw.Draw(image)



draw.line((200, 200, 400, 400), fill=(0,0,0), width=1)
draw.line((200, 400, 400, 200), fill=(0,0,0), width=1)

for i in range (0,201,20):
    draw.line((i, 0, i, 200), fill=(0,0,0), width=1)
    draw.line((0, i, 200, i), fill=(0,0,0), width=1)
    
for i in range (200,401,20):
    draw.line((i, 0, 200, i - 200), fill=(0,0,0), width=1)
    
for i in range (0,201,20):
    draw.line((i,200+i, i, 200+(i+20)), fill=(0,0,0), width=1)
    draw.line((i, i+220, (i+20), i + 220), fill=(0,0,0), width=1)

image.show()