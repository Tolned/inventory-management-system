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
        products: list[Product] | None = None
    ) -> None:
        if not isinstance(name, str):
            raise TypeError(
                f"Название категории должно быть строкой, "
                f"получено {type(name).__name__}"
            )
        if not name.strip():
            raise ValueError("Название категории должно быть непустой строкой")
        if not isinstance(description, str):
            raise TypeError(
                f"Описание категории должно быть строкой, "
                f"получено {type(description).__name__}"
            )

        self.name = name
        self.description = description
        self._products: list[Product] = []

        Category.category_count += 1

        if products is not None:
            for product in products:
                self.add_product(product)

    @property
    def products(self) -> list[Product]:
        return self._products.copy()

    @property
    def products_count(self) -> int:
        return len(self._products)

    @property
    def total_quantity(self) -> int:
        return sum(product.quantity for product in self._products)

    @property
    def products_display(self) -> str:
        if not self._products:
            return "Товары отсутствуют"
        return "\n".join(str(product) for product in self._products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self._products.append(product)
        Category.product_count += product.quantity

    def remove_product(self, product: Product) -> None:
        if product not in self._products:
            raise ValueError(
                f"Товар '{product.name}' не найден в категории '{self.name}'"
            )
        self._products.remove(product)
        Category.product_count -= product.quantity

    def get_product_by_name(self, name: str) -> Product | None:
        for product in self._products:
            if product.name == name:
                return product
        return None

    def get_total_value(self) -> float:
        return sum(
            product.price * product.quantity for product in self._products
        )

    def get_average_price(self) -> float:
        if not self._products:
            return 0.0
        return (
            sum(product.price for product in self._products)
            / len(self._products)
        )

    def get_most_expensive_product(self) -> Product | None:
        if not self._products:
            return None
        return max(self._products, key=lambda p: p.price)

    def get_cheapest_product(self) -> Product | None:
        if not self._products:
            return None
        return min(self._products, key=lambda p: p.price)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def __repr__(self) -> str:
        return (
            f"Category(name={self.name!r}, "
            f"description={self.description!r}, "
            f"products_count={len(self._products)})"
        )
