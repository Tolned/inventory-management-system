"""Тесты для класса Category."""

import sys

sys.path.insert(0, "./src")

from category import Category  # noqa: E402
from product import Product  # noqa: E402


class TestCategory:
    """Тесты для класса Category."""

    @staticmethod
    def setup_method():
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест 1: Проверить корректность инициализации категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        category = Category("Смартфоны", "Мобильные устройства", products)

        assert category.name == "Смартфоны"
        assert category.description == "Мобильные устройства"
        assert "Product 1" in category.products
        assert "Product 2" in category.products

    def test_category_count_increment(self):
        """Тест 2: Проверить инкремент счетчика категорий."""
        Category.category_count = 0
        Category("Кат1", "Описание1")
        assert Category.category_count == 1
        Category("Кат2", "Описание2")
        assert Category.category_count == 2

    def test_product_count_increment(self):
        """Тест 3: Проверить подсчет количества добавленных товаров."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        Category("Тест", "Описание", products)
        assert Category.product_count == 2

    def test_add_product(self):
        """Тест 4: Проверить добавление товара в категорию."""
        category = Category("Тест", "Описание")
        product = Product("Новый товар", "Описание", 150.0, 7)

        category.add_product(product)

        assert "Новый товар" in category.products
        assert Category.product_count == 1

    def test_category_statistics(self):
        """Тест 5: Проверить статистику категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
            Product("Product 3", "Desc 3", 50.0, 3),
        ]
        category = Category("Тест", "Описание", products)

        assert category.product_count == 3
        assert "Тест" in str(category)
        assert "18" in str(category)
