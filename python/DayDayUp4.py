import time
def dayUp(df):
    dayUp = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayUp = dayUp*(1-0.01)
        else:
            dayUp = dayUp*(1+df)
    return dayUp
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))

for i in range(12):
    print(chr(9800+i),end = " ")
