#输入10个数字，存入一个列表，并进行排序，输出最大值最小值和平均值

# 1.定义空列表
num_list=[]

# 2.存入数字
for i in range(10):
    num=int(input("请输入一个数字："))
    num_list.append(num)

# 3.排序
num_list.sort()

# # 4.得到平均值
# 法一
# sum=0
# for j in num_list:
#     sum+=j
# avg=sum/10




# 5.输出结果
print(f"最大值为：{num_list[-1]}")
print(f"最小值为：{num_list[0]}")
print(f"平均值为为：{sum(num_list)/len(num_list)}")#法二

'''
启发：
    1.定义空列表
    2.sum（）列表求和方法和len（）得到列表长度方法
    3.补充：max（）获取最大值，min()获取最小值

思考：1.为什么不能一次输入十个数字再依次录入？
'''