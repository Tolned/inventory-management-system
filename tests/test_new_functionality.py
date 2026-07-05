"""Тесты для новой функциональности на unittest."""

import sys
import unittest
from io import StringIO

# Добавляем src в sys.path для корректного импорта
sys.path.insert(0, "./src")

from category import Category  # noqa: E402
from product import Product  # noqa: E402


class TestNewFunctionality(unittest.TestCase):
    """Тесты для новой функциональности."""

    def setUp(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    # === Тесты add_product ===
    def test_add_product_increments_count_by_one(self):
        """add_product прибавляет 1 к product_count."""
        category = Category("Тест", "Описание")
        p1 = Product("P1", "D1", 100.0, 5)
        p2 = Product("P2", "D2", 200.0, 10)

        category.add_product(p1)
        self.assertEqual(Category.product_count, 1)

        category.add_product(p2)
        self.assertEqual(Category.product_count, 2)

    def test_add_product_returns_none(self):
        """add_product не возвращает значение."""
        category = Category("Тест", "Описание")
        p1 = Product("P1", "D1", 100.0, 5)
        result = category.add_product(p1)
        self.assertIsNone(result)

    def test_add_product_uses_append(self):
        """Продукт добавляется через append в _products."""
        category = Category("Тест", "Описание")
        p1 = Product("P1", "D1", 100.0, 5)
        category.add_product(p1)
        self.assertIn(p1, category._products)

    # === Тесты геттера products ===
    def test_products_getter_returns_string(self):
        """Геттер products возвращает строку."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 10),
        ]
        category = Category("Тест", "Описание", products)

        result = category.products
        self.assertIsInstance(result, str)

        expected_str = (
            "Product 1, 100.0 руб. Остаток: 5 шт.\n"
            "Product 2, 200.0 руб. Остаток: 10 шт.\n"
        )
        self.assertEqual(result, expected_str)

    def test_products_getter_empty(self):
        """Геттер products для пустой категории возвращает пустую строку."""
        category = Category("Тест", "Описание")
        self.assertEqual(category.products, "")

    def test_products_getter_template(self):
        """Каждый продукт соответствует шаблону."""
        product = Product("TestName", "Desc", 150.5, 7)
        category = Category("Тест", "Описание", [product])
        expected = "TestName, 150.5 руб. Остаток: 7 шт.\n"
        self.assertEqual(category.products, expected)

    # === Тесты new_product ===
    def test_new_product_classmethod(self):
        """new_product создает Product из словаря."""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 5,
        }
        product = Category.new_product(product_data)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "New Product")
        self.assertEqual(product.description, "New Description")
        self.assertEqual(product.price, 150.0)
        self.assertEqual(product.quantity, 5)

    # === Тесты сеттера price ===
    def test_price_setter_negative_prints_message(self):
        """Сеттер price выводит сообщение при отрицательной цене."""
        product = Product("Test", "Desc", 100.0, 5)

        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            product.price = -50.0
        finally:
            sys.stdout = sys.__stdout__

        expected_msg = "Цена не должна быть нулевая или отрицательная"
        self.assertEqual(captured_output.getvalue().strip(), expected_msg)
        self.assertEqual(product.price, 100.0)

    def test_price_setter_zero_prints_message(self):
        """Сеттер price выводит сообщение при нулевой цене."""
        product = Product("Test", "Desc", 100.0, 5)

        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            product.price = 0
        finally:
            sys.stdout = sys.__stdout__

        expected_msg = "Цена не должна быть нулевая или отрицательная"
        self.assertEqual(captured_output.getvalue().strip(), expected_msg)
        self.assertEqual(product.price, 100.0)

    def test_price_setter_valid_value(self):
        """Сеттер price обновляет цену при валидном значении."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 200.0
        self.assertEqual(product.price, 200.0)

    def test_price_getter(self):
        """Геттер price возвращает значение приватного атрибута."""
        product = Product("Test", "Desc", 100.0, 5)
        self.assertEqual(product.price, 100.0)


if __name__ == "__main__":
    unittest.main()
