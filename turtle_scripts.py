import turtle

window = turtle.Screen()
window.bgcolor('red')
def draw_square():
    brad = turtle.Turtle()
    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)

draw_square()

def draw_circle():
    window = turtle.Screen()
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)
draw_circle()

def draw_triangle():
    bard = turtle.Turtle()
    for i in range(1, 5):
        bard.right(120)
        bard.forward(100)
draw_triangle()

window.exitonclick()