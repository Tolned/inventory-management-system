"""Модуль содержит класс Category для представления категории товаров."""

from product import Product


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
        # Приватный атрибут с двойным подчёркиванием (name mangling)
        self.__products: list[Product] = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self) -> str:
        """Геттер, возвращающий строку со всеми продуктами по шаблону."""
        result: str = ""
        for product in self.__products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Класс-метод для создания продукта из словаря."""
        return Product(**product_data)

    def add_product(self, product: Product) -> None:
        """Метод добавления продукта в приватный список и увеличения счетчика."""
        self.__products.append(product)
        Category.product_count += 1
