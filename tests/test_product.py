"""Тесты для класса Product."""

import pytest

from product import Product


class TestProduct:
    """Основные тесты для класса Product."""

    def test_product_initialization(self):
        """Тест 1: Проверить корректность инициализации товара."""
        product = Product("Samsung Galaxy", "256GB, Черный", 180000.0, 5)

        assert product.name == "Samsung Galaxy"
        assert product.description == "256GB, Черный"
        assert product.price == 180000.0
        assert product.quantity == 5

    def test_product_validation_valid_data(self):
        """Тест 2: Проверить создание товара с валидными данными."""
        product = Product("Test", "Description", 100.0, 10)
        assert product.price == 100.0
        assert product.quantity == 10

    def test_product_validation_invalid_price(self):
        """Тест 3: Проверить ошибку при некорректной цене."""
        with pytest.raises(ValueError, match="положительным числом"):
            Product("Test", "Desc", -100.0, 5)

    def test_product_validation_invalid_quantity(self):
        """Тест 4: Проверить ошибку при некорректном количестве."""
        with pytest.raises(ValueError, match="неотрицательным"):
            Product("Test", "Desc", 100.0, -5)

    def test_product_price_property(self):
        """Тест 5: Проверить свойство price."""
        product = Product("Test", "Desc", 100.0, 5)

        assert product.price == 100.0

        product.price = 200.0
        assert product.price == 200.0

        with pytest.raises(ValueError, match="положительным числом"):
            product.price = -50.0
