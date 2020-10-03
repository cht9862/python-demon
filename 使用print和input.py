

# # 文件地址：C:\Users\Administrator\Desktop\python学习
# # inpy=int(input('请输入一个数字：[ ]'))
# # print('您输入的是：','[',inpy,']')

# # print('What is this')
# # name=input('请输入这个物品的名称：')
# # print('Wo Wo this is = [',name,']')

# # print('hello','chenhaotian',sep=',',end='.')
# # import math
# # print(math.ceil(1.4))


# # import math
# # print(math.floor(1.4))


# # import math
# # print(math.trunc(1.4))


# a="python\n"
# # print(type(a))
# # print(a[0:3:2])

# # print(a.strip('pt'))

# s=a.endswith("\n")
# print(s)


# print(a.find('l'))

# print(a.replace('p','a'))

# print(a.center(17,'-'))

# print(a.title())


# print(a.count('p'))
# print('hello'+a)
# print('hello%s'%(a))


# # print('hello %s,%s'%('word','chen'))
# print('Im %.7f year old'%(16))
# print('hello {1} {0}'.format('chen','Hao'))
# print('hello my {name} im {age} year old'.format(name='Chenhaotian',age=12))
# print(3/1)
# print(bool(1.01))

# a=[1,3,4,5]
# a.append('chen')
# a.remove(1,'chen')
# print(a)



# a=('a','b')
# # print(type(a),'\n',a)
# # print(a[0:2])
# a=(2,1,6,2)
# print(min(a))


# a={                                 #另一种方法创建字典
#     'chen':'haotian',
#     'zhang':'xiaoping'
# }
# a['yang']='haonan'
# s=a.pop('chen')
# a.popitem()
# print(s)
# print(a)


a=dict(
    chen='haotian',
    zhang='xiaoping'
)
a['chen']='haonan'
a.update({'chen':'haotian'})
a.setdefault('a',10)
print(a['a'],'\n',a)

if 'chen' & a:
    print('hahah')
else:
    print('在里面')