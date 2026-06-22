# #练习：简易计算器
# num1=int(input("第一个数："))
# num2=int(input("第二个数："))
# sign=input("运算符是：")
#
# match sign:
#     case "+":
#         print(f"{num1} + {num2} = {num1+num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1-num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1*num2}")
#     case "/" if num2!=0:#match case支持条件判断，条件不满足也不会进入case
#         print(f"{num1} / {num2} = {num1/num2}")
#     case _:
#         print(f"输入错误")

# 补充：一个case匹配多种值
day=int(input("输入星期几："))

match day:
    case 6|7:
        print(f"这一天是周末。")