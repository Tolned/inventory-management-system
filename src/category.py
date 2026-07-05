"""Модуль содержит класс Category для представления категории товаров."""

from product import Product


class Category:
    """Класс категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        # Атрибут списка товаров имеет приватный режим доступа
        self._products = []

        Category.category_count += 1

        # Если товары переданы при создании, добавляем их через add_product
        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self):
        """Геттер, возвращающий строку со всеми продуктами по шаблону."""
        result = ""
        for product in self._products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания продукта из словаря."""
        return Product(**product_data)

    def add_product(self, product):
        """Метод добавления продукта в приватный список и увеличения счетчика."""
        self._products.append(product)
        Category.product_count += 1
