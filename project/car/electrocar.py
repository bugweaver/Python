from Python.car.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self, brand, model, year, mileage):
        super().__init__(brand, model, year, mileage)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")
