# 类型
# +，-，*，/(小数），%，
# 新增：//（整除，浮点数参与计算得到浮点数，整数除得到整数），**（幂指数）

# # 1.//
# print(10//3)
#
# # 2.**
# print(10**3)
#
# # 3.注意事项，精度损失（由于input得到的是字符串，必须转换类型才能正确运算）
# a=float(input("第一个数字为："))#0.5
# b=float(input("第二个数字为："))#0.4
# print("a+b=",a+b)
# print("a-b=",a-b)#得到0.099999999

# # 案例一：计算三个输入整数的平均数
# x=int(input("第一个数为："))
# y=int(input("第二个数为："))
# z=int(input("第三个数为："))
# avg=(x+y+z)/3
#
# print("平均数为：",avg)

# # 案例二：输入梯形的上下底长和高，算面积
# up=float(input("上底为："))
# down=float(input("下底为："))
# h=float(input("高为："))
# s=(up+down)*h/2
#
# print("梯形面积为：",s)

# # 案例三：输入圆的半径，得到圆的周长和面积
# r=int(input())
# c=2*3.1415926*r
# s=3.1415926*r**2
#
# print(f"圆的周长为{c},圆的面积为{s}")

# 案例四：输入身高体重，计算BMI（BMI=体重（kg)/身高（m)**2
weight=float(input("请输入体重（kg）："))
height=float(input("请输入身高（m）："))
BMI=weight/(height**2)
print(f"你的BMI指数为：{BMI}")
