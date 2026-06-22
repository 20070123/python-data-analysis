class Car:
    # 类属性是整个类都有的属性
    wheel=4
    tax_rate=0.1
    # 实例属性是实例对象self独有的属性，对象不同实例属性就不一定相同
    def __init__(self,brand,name,color,price):
        self.brand=brand
        self.name=name
        self.color=color
        self.price=price
        # self.wheel=2#----->实例对象访问属性时查找顺序：先找实例属性，再找类属性，所以定义的实例属性会覆盖相同的类属性

    def run(self):
        print(f"{self.brand}{self.name}正在高速行驶！！！")

    def total_price(self,discount,rate=0.1):
        cost=self.price*rate+self.price*discount
        return cost

c=Car("BMW","X9","Black",100000)
c.run()
# 可以通过实例对象访问实例属性，也可以访问类属性，还可以用类名访问类属性
print(c.brand)
print(c.wheel)
print(Car.wheel)
