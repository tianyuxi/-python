dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))


s = "PYTHON"
while s != " ":
    for c in s:
        print(c,end = "")
    s = s[:-1]