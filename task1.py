# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Car:
    def __int__(self, brand: Union[str], mileage: Union[int, float], year_of_manufacture: Union[int]):

        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Бренд автомобиля
        :param mileage: Пробег автомобиля
        :param year_of_manufacture: Год выпуска автомобиля

        Примеры:
        >>> my_car = Car("Nissan", 124873.4, 2011)  # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Наименование марки автомобиля должно быть строкой (str)")
        if not isinstance(mileage, str):
            raise TypeError("Значение пробега должно быть числом (int, float)")
        if year_of_manufacture <= 1800:
            raise ValueError("Год выпуска не может быть ниже 1800 года. Значение должно быть целым числом")

        self.brand = brand
        self.model = mileage
        self.year_of_manufacture = year_of_manufacture

    def is_rare_car(self) -> bool:
        """
        Функция, проверяющая редкий ли автомобиль
        :return: редкий ли автомобиль

        Примеры:
        >>> my_car = Car("Nissan", 124873.4, 2011)
        >>> my_car.is_rare_car()
        """
        ...

    def age_of_car(self, this_year: int) -> int:
        """
        Функция, определяющая возраст автомобиля
        :param this_year: текущий год
        :return: возраст автомобиля

        Примеры:
        >>> my_car = Car("Nissan", 124873.4, 2011)
        >>> my_car.age_of_car(2025)
        """
        ...

    def service_is_needed(self, mileage_last_service: [int, float]) -> bool:
        """
        Функция, проверяющая нужно ли техобслуживание автомобилю
        :param mileage_last_service: значеие пробега на последнем техобслуживании
        :return: нужно ли техобслуживание

        Примеры:
        >>> my_car = Car("Nissan", 124873.4, 2011)
        >>> my_car.service_is_needed(11583.2)
        """
        ...


class Plant:
    def __int__(self, name_of_plant: Union[str], type_of_plant: Union[str]):

        """
        Создание и подготовка к работе объекта "Растение"

        :param name_of_plant: Название растения
        :param type_of_plant: Тип(вид) растения

        Примеры:
        >>> my_plant = Plant("Пахифитум", "Суккулент")  # инициализация экземпляра класса
        """

        if not isinstance(name_of_plant, str):
            raise TypeError("Название растения должно быть строкой (str)")
        if not isinstance(type_of_plant, str):
            raise TypeError("Название типа(вида) должно быть строкой (str)")

        self.name_of_plant = name_of_plant
        self.type_of_plant = type_of_plant

    def need_water(self) -> bool:
        """
        Функция, проверяющая нужно ли полить растение
        :return: нужен ли полив

        Примеры:
        >>> my_plant = Plant("Пахифитум", "Суккулент")
        >>> my_plant.need_water()
        """
        ...

    def need_more_light(self, level_light: int) -> bool:
        """
        Функция, определяющая возраст автомобиля
        :param level_light: текущий показатель освещенности
        :raise ValueError: Указывается значение освещенности по шкале от 1 до 10.
        Если уровень освещенности указан выше или ниже вызывается ошибка
        :return: нужно ли больше света

        Примеры:
        >>> my_plant = Plant("Пахифитум", "Суккулент")
        >>> my_plant.need_more_light(9)
        """
        ...


class Dish:
    def __int__(self, name_of_dish: Union[str], calories: Union[int]):

        """
        Создание и подготовка к работе объекта "Блюдо"

        :param name_of_dish: Название блюда
        :param calories: сколько калорий содержит блюдо

        Примеры:
        >>> my_dish = Dish("Салат", 150)  # инициализация экземпляра класса
        """

        if not isinstance(name_of_dish, str):
            raise TypeError("Название блюда должно быть строкой (str)")
        if not isinstance(calories, int):
            raise TypeError("Количество калорий должно быть целым числом (int)")

        self.name_of_dish = name_of_dish
        self.calories = calories

    def is_right_food(self, fats: float, proteins: float, carbohydrates: float) -> bool:
        """
        Функция, проверяющая правильная ли это еда в зависимости от диеты и состава
        :param fats: жиры
        :param proteins: белки
        :param carbohydrates: углеводы
        :return: правильная ли еда

        Примеры:
        >>> my_dish = Dish("Салат", 150)
        >>> my_dish.is_right_food(8.0, 3.5, 6.9)
        """
        ...

    def add_food_intake(self, calories: int) -> int:
        """
        Добавление приема пищи
        :param calories: калории добавлемой пищи
        :return: общий размер калорий за день

        Примеры:
        >>> my_dish = Dish("Салат", 150)
        >>> my_dish.add_food_intake(240)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
