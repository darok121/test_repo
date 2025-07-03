import test

class Drink:
    _volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price 
        self._remains = self._volume


    def drink_info(self):
        print(f"Name: {self.name}. Price: {self.price}. Start Volume: {self._volume}, Left drink: {self._remains}")


    def _is_enough(self, need):
        if self._remains >= need and self._remains > 0:
            return True
        else:
            print('Недостаточно напитка')
            return False 

    def sip(self):
        if self._is_enough(20) == True:
            self._remains -= 20
            print("Друг сделал глоток")

    def small_sip(self):
        if self._is_enough(10) == True:
            self._remains -= 10
            print('Друг сделал маленький глоток')
        
    def drink_all(self):
        if self._is_enough(0) == True:
            self._remains = 0
            print("Друг выпил весь напиток")

    def tell_price(self):
        print(f"цена")
        return self.price

class Juice(Drink):
    _juice_name = 'сок'

    def __init__(self, price, taste):
        super().__init__(self._juice_name, price)
        self.taste = taste

    def drink_info(self):
        print(f"Taste juice: {self.taste}. Price: {self.price}. Start Volume: {self._volume}, Left drink: {self._remains}")




apple_juice = Juice(250, 'яблочный')
apple_juice.small_sip()
apple_juice.sip()
apple_juice.drink_info()
apple_juice.drink_all()
print(apple_juice.tell_price())


print(test.add(4, 5))
