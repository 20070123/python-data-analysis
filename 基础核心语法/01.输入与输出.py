# #通过函数input进行键盘录入,格式为input(提示信息)
# name=input("K米诺诺莫伊娃：")
# age=input("岁数；")
# print(f"五类瓦{name}，{age}岁")

# # 案例：ATM取款
# # 总金额
# total=10000
# # 取款金额
# num=input("要多少钱：")
# print(f"还剩{total-int(num)}")#键盘录入数据一律为字符串类型

# # 案例：求两数和
# num1=input("第一个多少：")
# num2=input("第二个多少：")
# print(f"和为{int(num1)+int(num2)}")
#
# # 逗号和加号不同
# # 1.逗号：参数分隔，类型原样保留
# print("数字是", 15, "是否在范围内:", True)
# # 输出：数字是 15 是否在范围内: True
# # 这里 15 还是 int，True 还是 bool，只是被 print 分别打印出来了
#
# # 2.加号的核心：字符串拼接，只能 “字符串 + 字符串”
# print("数字是" + "15" + "，是否在范围内:" + "True")
# # 输出：数字是15，是否在范围内:True

# 错误写法（字符串 + 布尔值）
print("结果是:" + True)  # 报错：TypeError
