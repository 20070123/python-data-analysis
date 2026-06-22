#1计算每个学生总分，平均分，并输出

# 1.学生数据确定后不可修改，考虑用元组
students=(('s001','王琳',85,92,78),
          ('s002','李四',92,88,95),
          ('s003','十三',78,85,82),
          ('s004','增牛',88,79,91),
          ('s005','周铁',95,96,89),
          ('s006','王卓',76,82,77),
          ('s007','红蝶',89,91,94),
          ('s008','徐丽国',75,69,82),
          ('s009','许木',86,89,98),
          ('s010','遁天',66,59,72)
)

print(f"学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
# 法一：看第21行代码不能清晰知道都是什么数据
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {sum} \t {avg:.1f}")

#法二：解包
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
print()



# 2.输出班级各科平均分及最高最低分
c_grade=[s[2] for s in students]
c_avg=sum(c_grade)/len(c_grade)
m_grade=[s[3] for s in students]
m_avg=sum(m_grade)/len(m_grade)
e_grade=[s[4] for s in students]
e_avg=sum(e_grade)/len(e_grade)

print(f"语文最高分为：{max(c_grade)}，最低分为：{min(c_grade)},平均分为：{c_avg:.1f}")
print(f"数学最高分为：{max(m_grade)}，最低分为：{min(m_grade)},平均分为：{m_avg:.1f}")
print(f"英语最高分为：{max(e_grade)}，最低分为：{min(e_grade)},平均分为：{e_avg:.1f}")
print()

# 3.查找成绩优秀（平均分大于90）的学生
# 法一：
print(f'优秀学生名单如下：')
for s in students:
    total=s[2] + s[3]+s[4]
    avg=total/3
    if avg>=90:
        print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {avg:.1f}")
# 法二同上

