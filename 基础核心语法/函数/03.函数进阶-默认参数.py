#设定了默认参数，在传参时就可以省略对和相应形参的赋值
def x(a,b,c=2):
    return a+b+c

total=x(1,b=3)
print(total)
