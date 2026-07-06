"""Тесты для магических методов на unittest."""

import sys
import unittest

sys.path.insert(0, "./src")

from category import Category, CategoryIterator  # noqa: E402
from product import Product  # noqa: E402


class TestMagicMethods(unittest.TestCase):
    """Тесты для магических методов."""

    def setUp(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    # === Тесты __str__ для Product ===
    def test_product_str_format(self):
        """__str__ возвращает строку в правильном формате."""
        product = Product("Samsung", "Описание", 80.0, 15)
        expected = "Samsung, 80.0 руб. Остаток: 15 шт."
        self.assertEqual(str(product), expected)

    def test_product_str_with_different_values(self):
        """__str__ работает с разными значениями."""
        product = Product("iPhone", "Смартфон", 100000.0, 5)
        expected = "iPhone, 100000.0 руб. Остаток: 5 шт."
        self.assertEqual(str(product), expected)

    # === Тесты __str__ для Category ===
    def test_category_str_format(self):
        """__str__ возвращает строку с общим количеством товаров."""
        products = [
            Product("P1", "D1", 100.0, 10),
            Product("P2", "D2", 200.0, 20),
        ]
        category = Category("Электроника", "Описание", products)
        expected = "Электроника, количество продуктов: 30 шт."
        self.assertEqual(str(category), expected)

    def test_category_str_empty(self):
        """__str__ для пустой категории показывает 0."""
        category = Category("Пустая", "Описание")
        expected = "Пустая, количество продуктов: 0 шт."
        self.assertEqual(str(category), expected)

    # === Тесты __add__ для Product ===
    def test_product_add(self):
        """__add__ возвращает сумму произведений цены на количество."""
        a = Product("A", "D", 100.0, 10)
        b = Product("B", "D", 200.0, 2)
        result = a + b
        expected = 100.0 * 10 + 200.0 * 2  # 1400
        self.assertEqual(result, expected)

    def test_product_add_with_zero_quantity(self):
        """__add__ работает с нулевым количеством."""
        a = Product("A", "D", 100.0, 0)
        b = Product("B", "D", 200.0, 5)
        result = a + b
        expected = 100.0 * 0 + 200.0 * 5  # 1000
        self.assertEqual(result, expected)

    def test_product_add_type_error(self):
        """__add__ вызывает TypeError при сложении с не-Product."""
        a = Product("A", "D", 100.0, 10)
        # Намеренно передаём int для проверки TypeError
        with self.assertRaises(TypeError):
            a + 100  # type: ignore[arg-type]

    # === Тесты оптимизированного геттера products ===
    def test_products_getter_uses_str(self):
        """Геттер products использует __str__ для продуктов."""
        products = [
            Product("P1", "D1", 100.0, 10),
            Product("P2", "D2", 200.0, 20),
        ]
        category = Category("Тест", "Описание", products)
        result = category.products
        expected = "P1, 100.0 руб. Остаток: 10 шт.\nP2, 200.0 руб. Остаток: 20 шт.\n"
        self.assertEqual(result, expected)

    # === Тесты CategoryIterator ===
    def test_category_iterator(self):
        """CategoryIterator перебирает все товары."""
        products = [
            Product("P1", "D1", 100.0, 10),
            Product("P2", "D2", 200.0, 20),
        ]
        category = Category("Тест", "Описание", products)
        iterator = CategoryIterator(category.get_products_list())

        result = [str(product) for product in iterator]
        expected = [
            "P1, 100.0 руб. Остаток: 10 шт.",
            "P2, 200.0 руб. Остаток: 20 шт.",
        ]
        self.assertEqual(result, expected)

    def test_category_iterator_for_loop(self):
        """Category работает в цикле for."""
        products = [
            Product("P1", "D1", 100.0, 10),
            Product("P2", "D2", 200.0, 20),
        ]
        category = Category("Тест", "Описание", products)

        result = []
        for product in category:
            result.append(product.name)

        self.assertEqual(result, ["P1", "P2"])

    def test_category_iterator_empty(self):
        """Итерация по пустой категории не возвращает товаров."""
        category = Category("Пустая", "Описание")
        result = list(category)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
