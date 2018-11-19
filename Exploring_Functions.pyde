
 # Draw 3 Clouds in the background of the sky


def setup():
    size(700, 480)
    background(28, 41, 188)
    noStroke()
    noLoop()
    
def draw():
    drawCloud("143, 223, 2", 100, 300)
    drawCloud("48, 199, 24", 600, 200)
    drawCloud("188, 204, 2", width/2, height/2)
    
        
def drawCloud(colour, xloc, yloc):
    for i in range (3):
        ellipse(xloc, yloc, 150, 80)
        ellipse(xloc -40, yloc -50, 150, 100)
        ellipse(xloc +60, yloc +35, 150, 100)
        
