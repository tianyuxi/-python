# list_one=[]
# list1 = list()
# list_two = ['p','y','t','h','o','n']
# list_three = ['1','a','&',2.3]
# list_four = [1,'a','&',2.3,list_three]
# print(list_two)

# for li in list_two:
#     print(li,end='*')
# li_one = list('python')
# print(li_one[1:4:2])#第三个数字是步长

# li_five = []

li_num1 = [4,5,2,7]
li_num2 = [3,6]
li_num3 = li_num1+li_num2
print(li_num3)
li_num3.sort(reverse=True)
print(li_num3)


tu_num1 = ('p','y','t',['o','n'])
tu_num1[-1].append('y')
print(tu_num1)