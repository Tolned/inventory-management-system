"""Тесты для класса Product."""

import sys

sys.path.insert(0, "./src")

from product import Product  # noqa: E402


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест 1: Проверить корректность инициализации продукта."""
        product = Product("Samsung", "Смартфон", 50000.0, 10)

        assert product.name == "Samsung"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_validation_valid_data(self):
        """Тест 2: Проверить валидацию корректных данных."""
        product = Product("Test", "Desc", 100.0, 5)
        assert product.price == 100.0
        assert product.quantity == 5

    def test_product_validation_invalid_price(self):
        """Тест 3: Проверить поведение при некорректной цене.
        По ТЗ: выводится print, а не исключение.
        """
        product = Product("Test", "Desc", 100.0, 5)
        # При некорректной цене price не должен измениться
        product.price = -50
        assert product.price == 100.0  # осталось старое значение

    def test_product_validation_invalid_quantity(self):
        """Тест 4: Проверить корректность количества."""
        product = Product("Test", "Desc", 100.0, 5)
        # quantity — публичный атрибут, можно менять
        product.quantity = 0
        assert product.quantity == 0

    def test_product_price_property(self):
        """Тест 5: Проверить свойство price."""
        product = Product("Test", "Desc", 100.0, 5)

        assert product.price == 100.0

        product.price = 200.0
        assert product.price == 200.0

        # При невалидной цене значение не меняется
        product.price = -10
        assert product.price == 200.0
