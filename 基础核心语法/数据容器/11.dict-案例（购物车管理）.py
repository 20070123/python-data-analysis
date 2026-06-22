# 1.创建购物车数据结构
shopping_cart={}

# 2..打印菜单
print(f"欢迎使用购物车管理系统！！！")

menu='''
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 删除购物车         #
#         3. 查询购物车         #
#         4. 修改购物车         #
#         5. 退出购物车         #
################################
'''

while True:
    print(menu)
    choice = int(input("请输入你要执行的操作（1-5）："))

    # 3.利用match-case选择执行操作
    match choice:
        case 1:  # 添加商品进入购物车
            shopping_name = input("请输入商品名称：")
            shopping_price = float(input("请输入商品价格："))
            shopping_account = int(input("请输入商品数量："))

            if shopping_name in shopping_cart:
                print(f"你选择的商品已经存在，请重新选择。")
            else:
                shopping_cart[shopping_name] = {"price": shopping_price, "account": shopping_account}
                print(f"商品添加成功！")
        case 2:  # 删除购物车商品
            shopping_name = input("请输入商品名称：")

            if shopping_name in shopping_cart:
                del shopping_cart[shopping_name]
                print(f"商品删除成功！")
            else:
                print(f"购物车中没有该商品，请重新选择。")
        case 3:  # 查询购物车信息
            for name in shopping_cart:
                print(f"商品名称：{name} 价格：{shopping_cart[name]["price"]} 数量{shopping_cart[name]["account"]}")
        case 4:
            shopping_name = input("请输入要修改的商品名称：")
            shopping_price = input("请输入要修改的商品价格：")
            shopping_account = input("请输入要修改的商品数量：")

            for name in shopping_cart:
                if name == shopping_name:
                    shopping_cart[name]["price"] = shopping_price
                    shopping_cart[name]["account"] = shopping_account
                    print(f"商品信息修改成功！")
                else:
                    print(f"购物车中不存在该商品，无法修改！！！")
        case 5:  # 退出购物车
            print(f"退出成功，欢迎下次光临！！！")
            break
        case _:
            print(f"非法输入，不支持！！！")