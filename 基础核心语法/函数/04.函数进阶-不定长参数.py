# #一、位置传递--->通过（*args）,变量args会将传入的参数都收集进一个元组,args就是arguments，参数
# # 补充：形参不是必须叫args,这不是关键字，用其他合法变量名也是可以的，但是规范/约定俗成是这样
# def x(*args):
#     return sum(args)
#
# total=x(1,2,3,8,9)
# print(total)

# 二、关键字传递--->通过（**kwargs），变量kwargs会把传入的参数都封装进一个字典，kwargs就是keyword arguments
# # 补充：形参不是必须叫kwargs,这不是关键字，用其他合法变量名也是可以的，但是规范/约定俗成是这样
def calc_score(*args,**kwargs):
    max_num=max(*args)
    min_num=min(*args)
    avg_num=sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_num=round(avg_num,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最大值为：{max_num},最小值为：{min_num},平均值为：{avg_num}")

    return max_num,min_num,avg_num

s=calc_score(1,2,3,4,5,6,round=1,print=True)
print(s)



