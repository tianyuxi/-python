import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = ' ')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))




# for i in range(2,200):
#     isPrint = True
#     for j in range(2,i):
#         if (i%j == 0):
#             isPrint = False
#             break
#     if(isPrint == True):
#         print(i," ",end ="")



# for i in range(2,200):
#     if(i % 2 == 0):
#         print(i," ",end ="")
 

# a = eval(input("请输入要判断的数字"))
# if a > 0:
#     print("正数")
# if a < 0:
#     print("负数")
# if a == 0:
#     print("不是正数也不是负数")