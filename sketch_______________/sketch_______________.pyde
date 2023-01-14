x = 0

def setup():
    size(600,600)
    
def draw():
    global x
    img = loadImage("2.jpg")
    image(img, 0,0, 600,600)
    img = loadImage("3.jpg")
    image(img, 300,100, 200,200)
    img = loadImage("4.jpg")
    image(img, 100,100, 200,200)
    img = loadImage("5.jpeg")
    image(img, x,350, 200,200)
    x=x+1
    
