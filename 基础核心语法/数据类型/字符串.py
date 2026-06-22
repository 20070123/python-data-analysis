# # 一、字符串的三种定义方式
# # 1.
# print("hello world")
# # 2.
# print('hello world')
# # 3.
# # 注意：三引号字符串可以是多行
# print('''hello
#         world''')
#
# # 二、转义字符及其作用
# # 1.\'
# # 例如：print('It's good')会报错
# print('It\'s good') #这样就成了对的
#
# # 2.\"同上
#
# # 3.\n换行符
# print('hello \nworld')
#
# # 4.\t制表符
# print('hello\tworld')

# 三、字符串拼接
# 1.
s="生活不易"     "小常叹气"
print(s)

# 2.
s1="生活"
s2="不易"
s3="小常叹气"
print(s1+s2+','+s3)

# 3.案例（+号只能拼接字符串，要把别的数据类型通过str转换成字符串）
# name="常健"
# age=19
# major="Date Science and Big Date Technology"
# hobby="游戏，动漫，健身，敲代码，装13"
# print("我的名字是"+name+",今年"+str(age) + "岁了，我的专业是" + major + "，我的爱好有" + hobby)

# 4.字符串格式化
# (1 利用百分号占位符快速拼接，百分号占位符会将后面的数据自动转换为字符串再放到前面，不用str
name="常健"
age=19
major="Date Science and Big Date Technology"
hobby="游戏，动漫，健身，敲代码，装13"
print("我的名字是%s,今年%s岁了，我的专业是%s，我的爱好有%s"%(name,age,major,hobby))

# (2 f"...{变量名/表达式}..."     --->推荐方式
name="常健"
age=19
major="Date Science and Big Date Technology"
hobby="游戏，动漫，健身，敲代码，装13"
print(f"我的名字是{name},今年{age}岁了，我的专业是{major}，我的爱好有{hobby}")