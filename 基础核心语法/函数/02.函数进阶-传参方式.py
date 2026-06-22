# #一：位置参数
# def x(a,b,c):
#     return a+b+c
#
# total=x(1,2,3)
# print(total)

# 二：关键字参数--->传参的顺序可以不固定
# def x(a,b,c):
#     return a+b+c
#
# total=x(b=1,a=2,c=3)
# print(total)

# 三：混合式--->传参时前面的必须是位置参数，后面是关键词参数
def x(a,b,c):
    return a+b+c

total=x(1,c=2,b=3)
print(total)
