import turtle
#定义turtle的初始化数据
canvas = turtle.Screen()
canvas.bgcolor("blue")
wu=turtle.Turtle()
wu.shape("turtle")
wu.speed(10)
init=1
direction=17
def draw_turtle():
   while(True):
       global init
       global direction
       wu.forward(100)
       wu.right(90)
       wu.forward(100)
       wu.right(90)
       wu.forward(100)
       wu.right(90)
       wu.forward(100)
       wu.right(90)
       
       wu.right(direction)
       #canvas.exitonclick()
draw_turtle()  










 