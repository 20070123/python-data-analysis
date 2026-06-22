#猜数字游戏
import random
random_number = random.randint(1, 100)

while True:
    num =int(input("请输入一个数字："))

    if num == random_number:
        print(f"恭喜你！猜对了！")
        break
    elif num > random_number:
        print(f"猜大了")
        continue
    elif num < random_number:
        print(f"猜小了")
        continue

print(f"生成的随机数是：{num}")



