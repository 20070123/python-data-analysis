# 练习：求1-100以内的偶数累加和
i = 1
sum=0

while i<=100:
    if i%2==0:
        sum+=i
    i+=1

print(f"累加和为：{sum}")