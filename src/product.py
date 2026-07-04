"""Модуль содержит класс Product для представления товара."""


class Product:
    """Класс продукта.

    Атрибуты:
        name: Название товара.
        description: Описание товара.
        price: Цена товара в рублях.
        quantity: Количество товара на складе.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ) -> None:
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Название товара должно быть непустой строкой")
        if not isinstance(description, str):
            raise TypeError("Описание товара должно быть строкой")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена товара должна быть положительным числом")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество товара должно "
                             "быть неотрицательным целым числом")

        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Цена товара должна быть положительным числом")
        self._price = float(value)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, description={self.description!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __hash__(self) -> int:
        return hash((self.name, self.price))
