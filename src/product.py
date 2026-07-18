"""Модуль содержит классы продуктов: Product, Smartphone, LawnGrass."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base_product import BaseProduct  # noqa: E402
from mixins import InfoMixin  # noqa: E402


class Product(InfoMixin, BaseProduct):
    """Базовый класс продукта."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return (
            f"{self.name}, {self.__price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return (
            f"Product('{self.name}', '{self.description}', "
            f"{self.__price}, {self.quantity})"
        )

    def __add__(self, other: "Product") -> float:
        """Сложение двух продуктов одного класса."""
        if type(self) is not type(other):
            raise TypeError(
                "Нельзя складывать товары разных классов"
            )
        return (
            (self.__price * self.quantity)
            + (other.__price * other.quantity)
        )

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для приватного атрибута цены."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Smartphone(Product):
    """Класс смартфона — наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        # СНАЧАЛА присваиваем все атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # ПОТОМ вызываем super() — это вызовет repr() в миксине
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return (
            f"Smartphone('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity}, {self.efficiency}, "
            f"'{self.model}', {self.memory}, '{self.color}')"
        )


class LawnGrass(Product):
    """Класс газонной травы — наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        # СНАЧАЛА присваиваем все атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # ПОТОМ вызываем super() — это вызовет repr() в миксине
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return (
            f"LawnGrass('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity}, '{self.country}', "
            f"{self.germination_period}, '{self.color}')"
        )
