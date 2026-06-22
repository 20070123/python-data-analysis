# #定义类：法一---->不推荐，可读性差不能直接看出类中有哪些属性，而且后续修改也很麻烦
# class Car:
#     pass
# # 动态添加属性
# c=Car()
# c.brand="BMW"
# c.color="black"
# c.price=100000
#
# print(c)#输出c这个对象的内存地址
# print(c.__dict__)#将c这个对象中的所有属性以字典形式输出（键值对）

# 定义类：法二
class Car:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        print(f"实例对象属性已添加完成")

c=Car("BMW","black","100000")

print(c)
print(c.__dict__)
