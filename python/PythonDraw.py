import turtle
turtle.setup(800,800,200,200)#设定一个窗体(width,height,starx,starty)
turtle.penup()
turtle.fd(-250)#fd:海龟的正前反向运行,bk表示向海龟的反方向运行
turtle.pendown()
turtle.pensize(25)#画笔宽度
turtle.pencolor("purple")#颜色
turtle.seth(-40)#改变行进反向，海龟走角度括号里是角度
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)#以海归当前位置左侧的某一个点为圆心进行曲线运行
turtle.fd(40 * 2/3)


turtle.penup()#抬笔

turtle.left(45)#向左反向旋转45°
turtle.pendown()#落笔
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)

turtle.done()
