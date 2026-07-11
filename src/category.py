"""Модуль содержит класс Category для представления категории товаров."""

from product import Product


class CategoryIterator:
    """Класс-итератор для перебора товаров категории."""

    def __init__(self, products: list[Product]) -> None:
        self.__products = products
        self.__index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        raise StopIteration


class Category:
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product] | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return (
            f"{self.name}, "
            f"количество продуктов: {total_quantity} шт."
        )

    @property
    def products(self) -> str:
        """Геттер, возвращающий строку со всеми продуктами."""
        if not self.__products:
            return ""
        return "\n".join(
            str(product) for product in self.__products
        ) + "\n"

    def get_products_list(self) -> list[Product]:
        """Возвращает копию списка продуктов для итерации."""
        return list(self.__products)

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Класс-метод для создания продукта из словаря."""
        return Product(**product_data)

    def add_product(self, product: Product) -> None:
        """Метод добавления продукта с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса "
                "Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def __iter__(self) -> CategoryIterator:
        """Возвращает итератор для перебора товаров."""
        return CategoryIterator(self.get_products_list())
