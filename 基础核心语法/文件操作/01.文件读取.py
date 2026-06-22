#1.访问文件
# f =open("E:\\Develop\\Python\\测试.txt","r",encoding="utf-8")--->这么写也行
f =open("E:/Develop/Python/测试.txt","r",encoding="utf-8")
# print(type(f))

#2.读取文件(同一程序中，打开文件后，所有的方法都会在上一次读取方法的结尾处进行）
'''1.
read()方法:
文件对象.read(num)
num表示要从文件中读取的数据的长度(单位是字节),如果没有传入num,那么就表示读取文件中所有的数据。
'''
# print(f"读取2个字节的内容：{f.read(2)}")
# print(f"读取剩下的所有内容：{f.read()}")
# print("--------------------------------------")

'''2.
readlines()方法:
readlines可以按照行的方式把整个文件中的内容进行一次性读取,并且返回的是一个列表,其中每一行的数据为一个 元素。
# '''
# lines=f.readlines()
# print(f"lines的类型{type(lines)}")
# print(f"lines的内容{lines}")#------>如果不把12和13行注释掉，这里就是个空列表

'''3.
readline()方法
一次读取一行，可以利用for循环读取所有内容
'''
# 演示一、
# line1=f.readline()
# lien2=f.readline()
# # print(line1)#---->中间空一行是因为他把文件里最后的换行符也读进去了，同是print本身就会换行，可以用end控制
# print(line1,end="")
# print(lien2)

# # 演示二、
# for line in f:
#     print(line,end="")

# 3.with open("python.txt", "r") as f: f.readlines()
# 通过在with open的语句块中对文件进行操作
# 可以在操作完成后自动关闭close文件,避免遗忘掉close方法
with open("E:/Develop/Python/测试.txt","r",encoding="utf-8"):
    for line in f:
        print(line,end="")



















# import os

# # 检查目录是否存在
# path = "E:/Develop/Python/"
# if os.path.exists(path):
#     print(f"目录存在，内容如下：")
#     for item in os.listdir(path):
#         print(item)
# else:
#     print(f"目录 {path} 不存在！")
#
# # 如果不存在，尝试常见变体
# for alt in ["E:/Python/", "E:/Develop/", "C:/Python/"]:
#     if os.path.exists(alt):
#         print(f"发现替代目录：{alt}")