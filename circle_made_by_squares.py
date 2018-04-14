import turtle

def draw_art():
        window=turtle.Screen()
        window.bgcolor('red')
        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.color('yellow')
        brad.speed(10)
        for i in range(1, 37):
            for i in range(1, 5):
                brad.forward(100)
                brad.left(90)
            brad.left(10)
        window.exitonclick()
draw_art()
