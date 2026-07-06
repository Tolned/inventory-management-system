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
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return (
            f"{self.name}, {self.__price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other: "Product") -> float:
        """Сложение двух продуктов."""
        if not isinstance(other, Product):
            raise TypeError(
                "Можно складывать только объекты класса Product"
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
