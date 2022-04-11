# name = input("请输入名字")
# age = eval(input("请输入年龄"))
# print("我的名字叫{},今年{}岁".format(name,age))


# day = eval(input("请输入读的天数:"))
# print('还剩下{}页没有读'.format(368-12*day))

# import math
# radius = eval(input("请输入半径"))
# print("园的直径为{},圆的面积为{}".format(2*radius,radius**2*math.pi))

# print("还需要运送{}次".format((29.5-4*3)/2.5))

# TemStr = eval(input("请输入温度值:"))
# Kelvins = TemStr - 273.15
# print("转换后的绝对温度为{:.2f}K".format(Kelvins))

# weight = eval(input("请输入你的体重:"))
# height = eval(input("请输入你的身高:"))
# BMI = weight / height**2
# print("你的体质指数为",BMI)

year = 2020
month = 2
if month in [1,3,5,7,8,10,12]:
    print("%d月有31天"%month)
elif month in [4,6,9,11]:
    print("%d月有30天"%month)
elif month == 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("%d年%d月有29天"%(year,month))
    else:
        print("%d年%d月有28天"%(year,month))








