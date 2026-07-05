"""Модуль содержит класс Product для представления товара."""


class Product:
    """Класс продукта."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):
        self.name = name
        self.description = description
        # Атрибут «цена» имеет приватный режим доступа
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для приватного атрибута цены с проверкой на положительность."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value
