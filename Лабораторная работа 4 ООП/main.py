if __name__ == "__main__":
    class Car:
        def __init__(self, brand: str, model: str, year: int):
            """Создание и подготовка к работе модели "Car"

            Args:
                brand: бренд
                model: модель
                year: год
            """
            if not isinstance(brand, str):
                raise TypeError("brand must be of the str type")
            self.brand = brand
            if not isinstance(model, str):
                raise TypeError("model must be of the str type")
            self.model = model
            if not isinstance(year, int):
                raise TypeError("year must be of the int type")
            if year <= 0:
                raise ValueError("the year must be a positive number")
            self.year = year

        def __str__(self):
            """магический метод для отображения информации об объекте класса для пользователей"""
            return f'{self.brand} {self.model} {self.year}'

        def __repr__(self):
            """возвращает информационную строку об объекте"""
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

        def engine(self):
            """Функция для запуска мотора"""
            ...

        def tyrning(self, side: str):
            """Функция для маневрирования автомобиля.

            Args:
                side: сторона поворота
            """
            ...

    class ElectricCar(Car):
        def __init__(self, brand: str, model: str, year: int, battery_capacity: float):
            """Создание и подготовка к работе модели "ElectricCar"

            Args:
                brand: бренд
                model: модель
                year: год
                battery_capacity: емкость аккумуляторной батареи
            """
            super().__init__(brand, model, year)
            if not isinstance(battery_capacity, float):
                raise TypeError("battery_capacity must be of the float type")
            if battery_capacity <= 0.0:
                raise ValueError("the battery_capacity must be a positive number")
            self.battery_capacity = battery_capacity

        def __str__(self):
            return super().__str__()

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, " \
                   f"battery_capacity={self.battery_capacity!r})"

        def engine(self):
            """Данный метод перегружен, т.к. запуск электродвигателя подразумевает выполнение специфических процессов"""
            ...

        def turning(self, side: str):
            super().tyrning(side)


    # Пример использования:
    car1 = Car('Toyota', 'Corolla', 2020)
    electric_car1 = ElectricCar('Tesla', 'Model S', 2021, 100.0)

    print(car1)  # Вывод: Toyota Corolla 2020
    print(electric_car1)  # Вывод: Tesla Model S 2021

    print(repr(car1))  # Вывод: Car(brand='Toyota', model='Corolla', year=2020)
    print(repr(electric_car1))  # Вывод: ElectricCar(brand='Tesla', model='Model S', year=2021, battery_capacity=100.0)

    pass
