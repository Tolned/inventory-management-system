"""Тесты для наследования и ограничений."""

import sys
import unittest

sys.path.insert(0, "./src")

from category import Category  # noqa: E402
from product import LawnGrass, Product, Smartphone  # noqa: E402


class TestInheritance(unittest.TestCase):
    """Тесты для классов-наследников."""

    def setUp(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    # === Тесты Smartphone ===
    def test_smartphone_inherits_product(self):
        """Smartphone является наследником Product."""
        self.assertTrue(issubclass(Smartphone, Product))

    def test_smartphone_attributes(self):
        """Smartphone имеет все нужные атрибуты."""
        phone = Smartphone(
            "iPhone 15", "Смартфон Apple",
            100000.0, 5,
            95.5, "iPhone 15 Pro", 256, "Чёрный"
        )
        self.assertEqual(phone.name, "iPhone 15")
        self.assertEqual(phone.price, 100000.0)
        self.assertEqual(phone.quantity, 5)
        self.assertEqual(phone.efficiency, 95.5)
        self.assertEqual(phone.model, "iPhone 15 Pro")
        self.assertEqual(phone.memory, 256)
        self.assertEqual(phone.color, "Чёрный")

    def test_smartphone_str(self):
        """__str__ работает для Smartphone."""
        phone = Smartphone(
            "iPhone 15", "Смартфон Apple",
            100000.0, 5,
            95.5, "iPhone 15 Pro", 256, "Чёрный"
        )
        expected = "iPhone 15, 100000.0 руб. Остаток: 5 шт."
        self.assertEqual(str(phone), expected)

    # === Тесты LawnGrass ===
    def test_lawn_grass_inherits_product(self):
        """LawnGrass является наследником Product."""
        self.assertTrue(issubclass(LawnGrass, Product))

    def test_lawn_grass_attributes(self):
        """LawnGrass имеет все нужные атрибуты."""
        grass = LawnGrass(
            "Зелёная трава", "Газонная трава",
            500.0, 10,
            "Россия", 7, "Зелёный"
        )
        self.assertEqual(grass.name, "Зелёная трава")
        self.assertEqual(grass.price, 500.0)
        self.assertEqual(grass.quantity, 10)
        self.assertEqual(grass.country, "Россия")
        self.assertEqual(grass.germination_period, 7)
        self.assertEqual(grass.color, "Зелёный")

    def test_lawn_grass_str(self):
        """__str__ работает для LawnGrass."""
        grass = LawnGrass(
            "Зелёная трава", "Газонная трава",
            500.0, 10,
            "Россия", 7, "Зелёный"
        )
        expected = "Зелёная трава, 500.0 руб. Остаток: 10 шт."
        self.assertEqual(str(grass), expected)

    # === Тесты ограничений __add__ ===
    def test_add_same_class_products(self):
        """Можно складывать объекты одного класса Product."""
        p1 = Product("A", "D", 100.0, 10)
        p2 = Product("B", "D", 200.0, 5)
        result = p1 + p2
        expected = 100.0 * 10 + 200.0 * 5
        self.assertEqual(result, expected)

    def test_add_same_class_smartphones(self):
        """Можно складывать два смартфона."""
        s1 = Smartphone(
            "iPhone", "D", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        s2 = Smartphone(
            "Samsung", "D", 80000.0, 10,
            90.0, "Galaxy S24", 128, "Белый"
        )
        result = s1 + s2
        expected = 100000.0 * 5 + 80000.0 * 10
        self.assertEqual(result, expected)

    def test_add_same_class_lawn_grass(self):
        """Можно складывать две газонные травы."""
        g1 = LawnGrass(
            "Трава 1", "D", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        g2 = LawnGrass(
            "Трава 2", "D", 600.0, 5,
            "США", 5, "Зелёный"
        )
        result = g1 + g2
        expected = 500.0 * 10 + 600.0 * 5
        self.assertEqual(result, expected)

    def test_add_different_classes_raises_type_error(self):
        """Нельзя складывать смартфон и траву."""
        phone = Smartphone(
            "iPhone", "D", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        grass = LawnGrass(
            "Трава", "D", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        with self.assertRaises(TypeError):
            phone + grass

    def test_add_product_and_smartphone_raises_type_error(self):
        """Нельзя складывать Product и Smartphone."""
        p = Product("A", "D", 100.0, 10)
        s = Smartphone(
            "iPhone", "D", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        with self.assertRaises(TypeError):
            p + s

    # === Тесты ограничений add_product ===
    def test_add_product_to_category(self):
        """Можно добавить Product в категорию."""
        category = Category("Тест", "Описание")
        product = Product("A", "D", 100.0, 10)
        category.add_product(product)
        self.assertIn("A", category.products)

    def test_add_smartphone_to_category(self):
        """Можно добавить Smartphone в категорию."""
        category = Category("Тест", "Описание")
        phone = Smartphone(
            "iPhone", "D", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        category.add_product(phone)
        self.assertIn("iPhone", category.products)

    def test_add_lawn_grass_to_category(self):
        """Можно добавить LawnGrass в категорию."""
        category = Category("Тест", "Описание")
        grass = LawnGrass(
            "Трава", "D", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        category.add_product(grass)
        self.assertIn("Трава", category.products)

    def test_add_invalid_object_raises_type_error(self):
        """Нельзя добавить не-Product в категорию."""
        category = Category("Тест", "Описание")
        with self.assertRaises(TypeError):
            category.add_product("не продукт")  # type: ignore[arg-type]

    def test_add_dict_raises_type_error(self):
        """Нельзя добавить словарь в категорию."""
        category = Category("Тест", "Описание")
        with self.assertRaises(TypeError):
            category.add_product({"name": "A"})  # type: ignore[arg-type]

    def test_add_int_raises_type_error(self):
        """Нельзя добавить число в категорию."""
        category = Category("Тест", "Описание")
        with self.assertRaises(TypeError):
            category.add_product(100)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
