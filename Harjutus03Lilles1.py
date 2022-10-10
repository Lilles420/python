import turtle

#tekitan akna ja lisan muutujasse
aken = turtle.Screen()
aken.setup(300,300)
aken.title("kilpkonna harjutus03")

konn1 = turtle.Turtle()
turtle.speed(10)
for i in range(10):
    konn1.left(36)
    for i in range(3):
        konn1.forward(100)
        konn1.rt(120)
    





turtle.exitonclick()