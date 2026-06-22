# 案例
# 注意：break直接跳出循环，break以后while后面的else语句内代码不会执行
ok_account1=19355860982
ok_passwd1=111111
ok_account2=2025083085
ok_passwd2=222222
ok_account3=2007123
ok_passwd3=333333
cnt=0

while True:
    if cnt==5:
        print(f"验证失败，请稍后重试！")
        break

    account = int(input("输入账号："))
    passward = int(input("输入密码："))

    if account =="" or passward =="":
        print(f"账号或密码不能为空。")
        cnt+=1
        continue

    if account==ok_account1 and passward==ok_passwd1:
        print(f"输入正确，登陆成功！")
        break
    elif account==ok_account2 and passward==ok_passwd2:
        print(f"输入正确，登陆成功！")
        break
    elif account==ok_account3 and passward==ok_passwd3:
        print(f"输入正确，登陆成功！")
        break
    else:
        print(f"账号或密码错误，请重新输入。")
        cnt+=1