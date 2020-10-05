# # def fn():
# #     '''
# #     将指定列表中的偶数元素过滤并打印出来
# #     '''
# #     print('hello')
# #     a=[1,2,3,4,5,6,7,8,12]
# #     def fn1():
# #         s=[]
# #         for i in a:
# #             # print(i)
# #             if i % 2 == 0:
# #                 s.append(i)
# #             # print(s)
# #         return s
# #     s=fn1()
    
# #     def fn2():
# #         b=[]
# #         for i in s:
# #             if i > 5:
# #                 b.append(i)
# #         return b
    
# #     a=fn1()
# #     b=fn2()
# #     print(b)
# #     return a

# # s=fn()
# # print(s)


# def fn(a,b):
#     return a+b


# nu=lambda a,b: a+b
# print(nu(1,2))

# l=(1,2,3,4,5,6,7,8,9)
# ne=lambda i: i % 3 == 0 ;print(ne(13.5))
# fi=filter(lambda i: i%3 ==0,l)
# print(list(fi))
# l=[1,2,3,4,5,6,7,8,9]
# fi=map(lambda i: i*3 ,l)
# print(l.sort())


def number(a,b):
    '''
    求任意两个数的和
    '''
    return a+b

# def mul(a,b):
#     '''
#     求任意两个数的积
#     '''
    
#     return a*b



def fn():
    print('hello')




def fn2():
    print('开始打印')
    fn()
    print('打印结束')

def bend(a):
    def new_function(*ole,**keyole):
        print('开始打印')
        r = a(*ole,**keyole)
        print('打印结束')
        return r
    return new_function
# @fn2
@bend
def number(a,b):
    '''
    求任意两个数的和
    '''
    return a+b

def sya_hello():
    print('大家好')    

chen=number(123,456)
print(chen)
# f1=bend(number)
# f2=bend(number)
# r=f1(123,456)
# print(r)