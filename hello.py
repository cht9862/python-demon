# # # 定义一个人类
# # class Pe():
        
# #     def __init__(self,*name):      #魔术方法不用自己调用
# #         self.name=name
# #         if __name__ == "__main__":
# #             print(self.name)

# #     def Pe_run():
# #         print('正在疯狂的奔跑~~~')

    
# class Dog():
#     #name
#     #age
#     #gender
#     #height
#     def __init__(self,name,age,gender,height):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.height=height
    
#     def Dog_run():
#         print('Dog runing ~~~')
#     def Dog_jiao():
#         print('Dog speak ~~~~')


# # Dog.Dog_run()
# # a=Dog('旺财',2,'母狗',180)
# # b=Dog('杰瑞',3,'母狗',134)
# # print(a.name,a.gender,a.age,a.height)
# # print(b.name,b.gender,b.age,b.height)

# Dog(name='wang',age=12,gender='hello',height=123)
# print(Dog.name())


# print('hello {} {}'.format('my','pengyou'))
# a=['chen','hello']
# del a[0]

# print(a)
class A():
    
    def __init__(self,age):
        self.age=age
    
    # def __repr__(self):
    #     return 'hello word'
    
    # def __lt__(self,other):
    #     return self < other


a=A(age=22)
b=A(age=12)
print(a.age<b.age)
# if b.age > a.age:
#     print(True)
# else:
#     print(False)