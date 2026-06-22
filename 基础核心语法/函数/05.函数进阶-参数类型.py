#目前所学的所有数据类型都可以作为参数，甚至函数也可以作为参数
# 案例1：
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def calc_num(x,y,oper):
    return oper(x,y)

total=calc_num(1,2,multiply)
print(total)