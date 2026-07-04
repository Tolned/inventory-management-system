"""Тесты для класса Category."""

from category import Category
from product import Product


class TestCategory:
    """Основные тесты для класса Category."""

    def test_category_initialization(self):
        """Тест 1: Проверить корректность инициализации категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        category = Category("Смартфоны", "Мобильные устройства", products)

        assert category.name == "Смартфоны"
        assert category.description == "Мобильные устройства"
        assert len(category.products) == 2

    def test_category_count_increment(self):
        """Тест 2: Проверить подсчет количества категорий."""
        Category("Категория 1", "Описание 1")
        assert Category.category_count == 1

        Category("Категория 2", "Описание 2")
        assert Category.category_count == 2

    def test_product_count_increment(self):
        """Тест 3: Проверить подсчет количества товаров."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        Category("Тест", "Описание", products)

        assert Category.product_count == 15  # 5 + 10

    def test_add_product(self):
        """Тест 4: Проверить добавление товара в категорию."""
        category = Category("Тест", "Описание")
        product = Product("Новый товар", "Описание", 150.0, 7)

        category.add_product(product)

        assert len(category.products) == 1
        assert category.products[0].name == "Новый товар"
        assert Category.product_count == 7

    def test_category_statistics(self):
        """Тест 5: Проверить статистику категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
            Product("Product 3", "Desc 3", 50.0, 3),
        ]
        category = Category("Тест", "Описание", products)

        assert category.products_count == 3
        assert category.total_quantity == 18  # 5 + 10 + 3

        expected_value = 100 * 5 + 200 * 10 + 50 * 3  # 2650
        assert category.get_total_value() == expected_value
