from turtle import * 

turtle = Turtle()

hexagonSideLength = int(input("Enter the length of a side of the hexagon: "))

for i in range(6):
    turtle.forward(hexagonSideLength)
    turtle.left(60)

mainloop()
