# #将两个列表合并并去掉重复元素
#
# s1=[1,2,3,4,5,6]
# s2=[4,6,84,15,44,66]
#
# for i in s2:
#     s1.append(i)
#
# new_list=[]
#
# for j in s1:
#     if j not in new_list:#这一块学习一下，逻辑运算符。就是判断一个元素在不在列表中
#         new_list.append(j)
#
# print(f"最终的列表为：{new_list}")

'''
思考：
    1.range（）到底咋用的？range(len(s1))是什么意思？
'''

# 简化

# s1=[1,2,3,4,5,6]
# s2=[4,6,84,15,44,66]
#
# num_list=[*s1,*s2]#————>解包：把列表这一容器解开成一个个独立的元素。
#
# new_list=[]
#
# for j in num_list:
#     if j not in new_list:
#         new_list.append(j)
#
# print(f"最终的列表为：{new_list}")

#解包：把列表这一容器解开成一个个独立的元素。
# 补充；
#   1.组包：将多个值合并进一个容器

# 再简化
s1=[1,2,3,4,5,6]
s2=[4,6,84,15,44,66]

num_list=s1+s2

new_list=[]

for j in num_list:
    if j not in new_list:
        new_list.append(j)

print(f"最终的列表为：{new_list}")