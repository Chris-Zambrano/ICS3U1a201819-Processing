click_number = 0

delta_x = 101
delta_y = 101
cloud_speed_x = 6
cloud_speed_y = 4

x = 0

image_pos_x = 100
image_pos_y = 100
image_size_x = 100
image_size_y = 100
image_speed_x = 5
image_speed_y = 2
def setup():
    global img, soccer_ball
    size(800, 600)

    img = loadImage("bernabeu4.jpg")
    soccer_ball = loadImage("soccerball.png")

def draw():
    global click_number
    global delta_x, delta_y, cloud_speed_x, cloud_speed_y
    global image_pos_x, image_pos_y
    global image_size_x, image_size_y, image_speed_x, image_speed_y
    background(img)

    noStroke()  # remove border on shapes
    # ellipse(x, y, width, height)
    fill("#2A3D45")  # change shape fill color
    ellipse(width/3, height/3, 100, 100)
    
    # rect(x, y, width, height)
    fill("#C17C74")
    rect(width/4, height/4, -200, -200)
    
    # rect(x, y, width, height)
    if click_number == 0:
        fill(33, 39, 89)
    else:
        fill(0)
    rect(width/2, height/2, -100, -100)

    #Bouncing Cloud
    noStroke()
    fill(124, 19, 23)
    ellipse(delta_x, height/2, 50, 50)
    ellipse(delta_x+30, height/2, 50, 50)
    ellipse(delta_x-10, height/2-20, 50, 50)

    delta_x += cloud_speed_x
    delta_y += cloud_speed_y
    print(delta_x)
    if delta_x < 100 or delta_x > 600:
        cloud_speed_x *= -1
    elif delta_y <= 100 or delta_y >= 600:
        cloud_speed_y *= -1
        
    if click_number == 1:
        background("#ffffff")
        fill("#000000")
        textAlign(CENTER)
        textSize(35)
        text("Press \'c' to see a bouncing image on other side", width/2, height/2)
        if key == "c":
            background(255)
            imageMode(CENTER)
            image(soccer_ball, image_pos_x, image_pos_y, image_size_x, image_size_y)
            image_pos_x += image_speed_x
            image_pos_y += image_speed_y
            if image_pos_x < image_size_x/2 or image_pos_x > width-image_size_x/2:
                image_speed_x *= -1
            elif image_pos_y < image_size_y/2 or image_pos_y > height-image_size_y/2:
                image_speed_y *= -1


def mouseClicked():
    global click_number
    click_number += 1
    if click_number == 2:
        click_number = 0


# def keyPressed():
    # global click_number
    # if  click_number == 1 and key == "c":
