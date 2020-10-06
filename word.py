file_name = 'C:/Users/Administrator/Desktop/python学习/python-demon/'
# file_name1 = 'C:/Users/Administrator/Desktop/python学习/python-demon/demon.txt'

# try:
#     with open(file_name,'r+',encoding='utf-8') as a_read:    # 打开文件的权限有'r''w''a'     a是追加的权限，不会覆盖原先的值
#         # print(a_read.readlines())
#         # print(a_read.readline())
#         r=a_read.read()
#         with open(file_name1,'x',encoding='utf-8') as b_read:
#             b_read.write(r)
#         # a_read.read('美好的一天\n')                #通过write 写入会覆盖原有内容，并且写入多个默认不换行，需要在每一句后面加\n
#         # r = a_read.write('chenhaotian')                 #write有返回值，他的返回值是写入字符的数量
#                                                         # 在同一次打开文件的多个写入动作不会覆盖，会追加
#             # a_read.close
#         # print(a_read.read())
# except Exception as 错误类型:
#     print('出错了~~~~~')




import os
r=os.listdir(file_name)
s=os.listdir()
os.chdir('E:\腾讯课堂')
a=os.listdir()
b=os.getenv()
print(b)
print(r)
print(s)
print(a)