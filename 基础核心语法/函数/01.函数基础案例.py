#案例一：定义一个函数，根据输入的底和高计算三角形面积
def trangle_area(b,h):
    '''
    根据底和高计算三角形面积
    :param b: 底长
    :param h: 高
    :return: 三角形面积
    '''
    area=b*h*0.5
    return area

print("三角形面积为：",trangle_area(5,5))

# 案例二：计算传入的字符串中元音字母的个数
def count_aeiou(s):
    num=0
    for ch in s:
        if ch in "aeiouAEIOU":
            num+=1
    return num

print(count_aeiou("Hello-World-Hello-Python"))

# 案例三：计算传入的班级学生高考成绩列表中的最高分，最低分和平均分（保留一位小数)
def calc_score(score_list):
    max_num=max(score_list)
    min_num=min(score_list)
    avg_num=round(sum(score_list)/len(score_list),1)
    return max_num,min_num,avg_num


    

