class Car:
    def __init__(self,brand,name,color,price):
        self.brand=brand
        self.name=name
        self.color=color
        self.price=price

    def run(self):
        print(f"{self.brand}{self.name}正在高速行驶！！！")

    def total_price(self,discount,rate=0.1):
        cost=self.price*rate+self.price*discount
        return cost

c=Car("BMW","X9","Black",100000)
c.run()
print(c.total_price(0.9))