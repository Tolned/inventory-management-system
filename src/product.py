"""Модуль содержит класс Product для представления товара."""


class Product:
    """Класс продукта."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        # Приватный атрибут с двойным подчёркиванием (name mangling)
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для приватного атрибута цены с проверкой на положительность."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
