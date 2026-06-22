#案例1：生成1-20的平方列表
# 法一：传统，不推荐
# num_list=[]
#
# for i in range(1,21):
#     num_list.append(i**2)
#
# print(num_list)

# # 法二：列表推导式
# num_list=[i**2 for i in range(1,21)]
# print(num_list)

# 案例2：从列表中提取所有偶数，并将其平方存入心得列表中
# 法一：传统，不推荐
# list=[22,56,8,65,67,49,34,41,61]
# new_list=[]
#
# for i in list:
#     if i%2==0:
#         new_list.append(i**2)
#
# print(new_list)

# 法二：列表推导式
list=[22,56,8,65,67,49,34,41,61]
new_list=[i**2 for i in list if i%2==0]
print(new_list)






