class CheckOrder:

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.__name} должно быть числом")
        elif value < 0:
            raise ValueError(f"{self.__name} должно быть положительным числом")

        instance.__dict__[self.__name] = value


class Order:
    price = CheckOrder()
    count = CheckOrder()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total_cost(self):
        print(self.price * self.count)


o = Order('apple', 5, 10)
o.total_cost()
print('test')
