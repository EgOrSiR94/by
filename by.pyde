def setup():
    size(600,600)
def draw():
    if mousePressed and (mouseButton == LEFT):
        img = loadImage("y.jpg")
        image(img, 0,0)
    elif mousePressed and (mouseButton == RIGHT):
         img = loadImage("b.jpg")
         image(img, 0,0,600,600)
