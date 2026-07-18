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

    def test_category_initialization(self, capsys):
        """Тест 1: Проверить корректность инициализации категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        capsys.readouterr()  # очищаем вывод миксина
        category = Category("Смартфоны", "Мобильные устройства", products)

        assert category.name == "Смартфоны"
        assert category.description == "Мобильные устройства"
        # products — это строка, проверяем наличие товаров
        assert "Product 1" in category.products
        assert "Product 2" in category.products

    def test_category_count_increment(self):
        """Тест 2: Проверить инкремент счетчика категорий."""
        Category.category_count = 0
        Category("Кат1", "Описание1")
        assert Category.category_count == 1
        Category("Кат2", "Описание2")
        assert Category.category_count == 2

    def test_product_count_increment(self, capsys):
        """Тест 3: Проверить подсчет количества добавленных товаров."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        capsys.readouterr()  # очищаем вывод миксина
        Category("Тест", "Описание", products)
        # product_count — это количество добавлений (по ТЗ add_product +1)
        assert Category.product_count == 2

    def test_add_product(self, capsys):
        """Тест 4: Проверить добавление товара в категорию."""
        category = Category("Тест", "Описание")
        product = Product("Новый товар", "Описание", 150.0, 7)
        capsys.readouterr()

        category.add_product(product)

        # products — строка, проверяем наличие товара
        assert "Новый товар" in category.products
        assert Category.product_count == 1

    def test_category_statistics(self, capsys):
        """Тест 5: Проверить статистику категории."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
            Product("Product 3", "Desc 3", 50.0, 3),
        ]
        capsys.readouterr()
        category = Category("Тест", "Описание", products)

        # Правильное имя атрибута — product_count
        assert category.product_count == 3
        # Проверяем __str__
        assert "Тест" in str(category)
        assert "18" in str(category)  # 5 + 10 + 3 = 18
