import turtle,time
def drawGap():#绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):#绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDight(dight):#根据数字绘制七段数码管
    drawLine(True) if dight in[2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if dight in[0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,3,5,7,8,9] else drawLine(False)
    drawLine(True) if dight in[0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20) #为绘制后续数字确定位置
def DrawDate(date):#获得要输出的数字
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial",18,"normal"))
        elif i == '+':
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            drawDight(eval(i))#通过eval()函数将数字变为整数
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    DrawDate(time.strftime("%Y-%m=%d+",time.gmtime()))#date为日期
    turtle.hideturtle()
    turtle.done()
main()
