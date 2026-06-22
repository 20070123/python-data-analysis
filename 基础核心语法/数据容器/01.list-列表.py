# 列表：可以存重复元素，有序支持索引下标访问，可以遍历其中每个元素，可以修改
#常用方法

s=[44,10,50.70,88,92,65,44,66]
print(s)

# count方法
print(s.count(44))

# 1.append方法
s.append(66)
print(s)

# 2.insert方法
s.insert(0,11)
print(s)

#3.remove方法（找到第一个指定元素并删去+）
s.remove(44)
print(s)

# 4.pop方法（找到指定索引的元素并删去，没指定索引默认最后一个）
s.pop(1)
print(s)

s.pop()
print(s)

# 5.sort方法（只有列表内都是同一数据类型才能排序）
s.sort()
print(s)

# 6.reverse方法
s.reverse()
print(s)


