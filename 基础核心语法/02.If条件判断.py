# #案例：输入账号密码检验是否正确
# account=int(input("输入账号："))#注意转换成int类型，不然后续不能和ok_account比较，后者是int类型
# passward=int(input("输入密码："))
#
# ok_account=19355860982#或者把ok的两个设置为字符串类型，如“19355860982”
# ok_passwd=111111
#
# if account==ok_account and passward==ok_passwd:
#     print(f"输入正确，登陆成功！")
# else:
#     print(f"账号或密码错误。")

# # 案例：判断是否为闰年
# year=int(input("请输入年份："))
#
# if year%400==0 or year%4==0 and year%100!=0:
#     print(f"{year}年为闰年。")
# else:
#     print(f"{year}年是平年。")

# # 练习：判断输入数字是奇数还是偶数
# num=int(input("请输入数字："))
#
# if num%2==0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# #elif案例：输入账号密码检验是否正确
# account=int(input("输入账号："))
# passward=int(input("输入密码："))
#
# ok_account1=19355860982
# ok_passwd1=111111
# ok_account2=2025083085
# ok_passwd2=222222
# ok_account3=2007123
# ok_passwd3=333333
#
# if account==ok_account1 and passward==ok_passwd1:
#     print(f"输入正确，登陆成功！")
# elif account==ok_account2 and passward==ok_passwd2:
#     print(f"输入正确，登陆成功！")
# elif account==ok_account3 and passward==ok_passwd3:
#     print(f"输入正确，登陆成功！")
# else:
#     print(f"账号或密码错误。")

# # elif练习：
# num=int(input("请输入度数："))
#
# if num>4800:
#     price=2800*0.4883+2000*0.5383+(num-4800)*0.7883
# elif num>2800 and num<=4800:
#     price=2800*0.4883+(num-2800)*0.5383
# elif num>0and num<=2800:
#     price=num*0.4883

