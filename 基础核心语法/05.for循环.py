# # 案例：计算1-100之间奇数累加和
# sum =0
# for i in range(1,101,2):
#     sum+=i
# else:
#     print(f"累加和为：{sum}")

# # 案例：计算100-500之间3的倍数累加和
# sum =0
# for i in range(100,501,):
#     if i % 3 == 0:
#         sum+=i
# else:
#     print(f"累加和为：{sum}")

# # 案例：输入矩形的长宽，用*号打印对应矩形
# a=int(input("输入矩形的长："))
# b=int(input("输入矩形的宽："))
#
# for i in range(b):
#     print("")
#     for j in range(a):
#         print('*',end='  ')

# # 案例：打印99乘法表
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}",end="  ")

# # 练习：输入直角边的边长打印对应边长等腰三角形
# a=int(input("直角边的边长："))
#
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()

# 练习：根据输入数字打印数字金字塔
a=int(input("金字塔的边长："))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(f"{j}",end="  ")
    print()