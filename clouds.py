click_number = 0


def setup():
    size(800, 600)
    
    img = loadImage("santiangober8.jpg")
    background(img)

def draw():
    global click_number
    noStroke()  # remove border on shapes
    # ellipse(x, y, width, height)
    fill("#2A3D45")  # change shape fill color
    ellipse(width/2, height/2, 100, 100)
    
    # rect(x, y, width, height)
    fill("#C17C74")
    rect(width/2, height/2, 200, 200)
    
    # rect(x, y, width, height)
    if click_number == 0:
        fill(33, 39, 89)
    else:
        fill(0)
    rect(width/2, height/2, -100, -100)


def mouseClicked():
    global click_number
    click_number += 1
    if click_number == 2:
        click_number = 0
        
