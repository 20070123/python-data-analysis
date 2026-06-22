def calc_order_price(*args,coupon=0,score=0,express=0):
#1.计算商品总金额
    price=[good[1]*good[2] for good in args]
    total_price=sum(price)
# 2.优惠券减免
    if coupon>=5000 and coupon<=total_price:
        cost=total_price-coupon
# 3.积分减免
    if score>=5000 and score//100<=total_price:#--->//是整除
        cost-=score
# 4.加上运费
    cost+=express
# 5.返回实际应付
    return cost

cost = calc_order_price(("电脑",6000,3),("相机",2000,6),("手机",5000,5),coupon=6000,score=400,express=500)
print(cost)




