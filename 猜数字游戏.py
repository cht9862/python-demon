'''
game_name：猜数字
author：Chen Haotian
目的：
    系统给出一个两位数的数字，用户通过猜数字输入答案，判断是否对应系统所给出的
数字，如果对应则通关程序。

'''

print('hello')

print('你好')

print('再见')



def fn():
    print('这是我的第一个函数')
    print('今天天气真不错')
print(type(fn))
fn()
#定义一个函数，可以用来求任意两个数的和
def sumb(a1,a2,argument=3):
    # Number_a=int(input('请输入第一个数字'))
    # Number_b=int(input('请输入第二个数字'))
    # print(argument+Number_b+a)
    print(a1)
    print(a2)
    print(argument)

sumb(a2=3,a1=2)

a=[1,2,3,4]
c=a.copy
print(id(a),'\n',id(c))
