# weekStr = "一二三四五六日"
# weekId = eval(input("请输入星期数字:"))
# print("星期"+weekStr[weekId-1])

'''字符串操作
len(x)返回字符串x的长度
str(x)任意类型x所对应的字符串形式
hex(x)或oct(x)整数x的十六进制或八进制小写形式字符串
chr(u)u为Unicode编码,返回其对应的字符
ord(x)x为字符,返回其对应的Unicode编码 

str.lower()或str.upper()返回字符串的副本,全部字符小写/大写
str.split(sep = None)返回一个列表,由str根据sep被分隔的部分组成
str.count(sub)返回字串sub再str中出现的次数
str.replace(old,new)返回字符串str副本,所有old子串被替换为new
str.center(width,[fillchar])字符串str根据宽度width居中
str.strip(chars)从str中去掉其左侧和右侧chars中列出的字符
str.join(iter)在iter变量除最后元素外每个元素外每个元素后增加一个str","主要用于字符串分隔
capitalize()
str.title()
isupper()
upper()
center() 
ljust()
rjust()

'''
'''random库包括两类函数,常用的有8种
基本随机数函数:seed(),random()
扩展随机函数:randint()整数,getrandbits(k),uniform(a,b),randrange(m,n,k),choice(序列seq),shuffle()返回打乱后的序列
'''
'''函数的定义与使用
函数的使用及调用过程
函数的参数传递
函数的返回值
局部变量和全局变量
lambda函数
~x = -(x+1)
'''

'''组合数据类型
集合类型、序列类型、字典类型
'''
'''操作符及应用
并S|T 返回一个新集合,包括在集合S和T中的所有元素
差S-T 返回一个新集合,包括在集合S但不在T中的元素
交S&T 返回一个新集合,包括同时在集合S和T中的元素
补s^T 返回一个新集合,包括集合S和T中的非相同元素
增强操作符
S|=T更新集合S,包括在集合S和T的所有元素
S-=T更新集合S,包括在集合S但不在T的元素
S&=T更新集合S,包括同时在集合S和T中的元素
S^=T更新集合S,包括集合S和T中的非相同元素
'''

'''
S.add(x)如果x不在集合S中,将x增加到S
S.discard(x)移除S中的元素,如果x不在集合S中,不报错
S.remove(x)移除S中的元素x,如果x不在集合S中,产生KeyError异常
S.clear()移除S中所有元素
S.pop()随即返回S的一个元素,更新S,若S为空产生KeyError异常
S.copy()返回集合S的一个副本
len(S)返回集合S的元素个数
x in S判断S中的元素x,x在集合S中,返回True,否则返回False
x not in S 判断S中的元素x,x不在集合S中,返回True,否则返回False
set(x)将其他类型变量x转变为集合类型

'''

'''
append 在列表末尾添加元素
extend 在列表末尾添加另一个序列的所有元素
insert按照索引将元素插入到列表的指定位置
'''
'''元素排序
sort    #有序的元素会覆盖原来的列表元素,不产生新列表
sorted  #产生排序后的新列表,排序操作不会对原表产生影响
reverse #逆置列表,即把原列表中的元素从右至左依次排序存放

del li_one[0]
remove()
pop()
clear()
'''
'''
S.add(x)
S.remove(x)
S.discard(x)删除集合S中的元素x,若x不存在不做处理
S.pop()
S.clear()
S.copy()
S.isdisjoint(T)判断集合S和T是否有相同元素,没有放回True
'''
# word = '中国'
# string = '你好,中国'
# result = string.find(word)
# print(result)

# s = 'AbcDeFGhIj'
# uppercase = 0
# lowercase = 0
# for c in  s:
#     if(c.isupper==True):
#         uppercase +=1
#         break
#     else:
#         lowercase +=1
# print("大写有{}个,小写有{}个".format(uppercase,lowercase))



# str='Life is short.I use python'
# if 'python' in str:
#     print(str.replace('python','Python'))
# else:
#     print(str)

s = 'AbcDeFGjIJ'
lowercase = 0
uppercase = 0
for i in s:
    if i.islower():
         lowercase += 1
    else:
        uppercase +=1
print("小写有{}大写有{}".format(lowercase,uppercase))
        






