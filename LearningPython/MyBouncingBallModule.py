import turtle
class BouncingBallGenerator:
    def CreateBouncingBall(self):
        wn = turtle.Screen()
        wn.title("Bouncing Ball Program")
        wn.bgcolor('black')
        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("green")
        ball.penup()
        ball.speed()
        ball.goto(0, 0)
        ball.dy = 0
        ball.dx = 0
        gravity = 0.1
        while True:
            ball.dy = round((ball.dy - gravity),2)
            ball.dx = round((ball.dx + gravity),2)

            ball.sety(round((ball.ycor() + ball.dy), 2))
            ball.setx(round((ball.xcor() + ball.dx), 2))
     
            print ('ball.dx = ' + str(ball.dx) + ", ball.x = " + str(ball.xcor()) + "\r\n")
            
            if ball.ycor() < -300:
                ball.sety(-300)
                ball.dy = round((ball.dy * -1),2)
            elif ball.xcor() > 300:
                ball.setx(300)
                ball.dx = round((ball.dx * -1),2)
            
        wn.mainloop()
       