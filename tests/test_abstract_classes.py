"""Тесты для абстрактных классов и миксинов."""

import sys

import pytest

sys.path.insert(0, "./src")

from base_product import BaseProduct  # noqa: E402
from category import Category  # noqa: E402
from product import LawnGrass, Product, Smartphone  # noqa: E402


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct."""

    def test_base_product_is_abstract(self):
        """BaseProduct является абстрактным классом."""
        import inspect
        assert inspect.isabstract(BaseProduct)
        assert len(BaseProduct.__abstractmethods__) > 0

    def test_product_inherits_base_product(self):
        """Product наследует BaseProduct."""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_product(self):
        """Smartphone наследует Product, а значит и BaseProduct."""
        assert issubclass(Smartphone, Product)
        assert issubclass(Smartphone, BaseProduct)

    def test_lawn_grass_inherits_product(self):
        """LawnGrass наследует Product, а значит и BaseProduct."""
        assert issubclass(LawnGrass, Product)
        assert issubclass(LawnGrass, BaseProduct)


class TestInfoMixin:
    """Тесты для класса-миксина InfoMixin."""

    def test_product_prints_on_creation(self, capsys):
        """Product печатает repr при создании."""
        Product("Test", "Desc", 100.0, 5)
        captured = capsys.readouterr()
        assert "Product(" in captured.out
        assert "Test" in captured.out
        assert "Desc" in captured.out
        assert "100.0" in captured.out

    def test_smartphone_prints_on_creation(self, capsys):
        """Smartphone печатает repr при создании."""
        Smartphone(
            "iPhone", "Desc", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        captured = capsys.readouterr()
        assert "Smartphone(" in captured.out
        assert "iPhone" in captured.out

    def test_lawn_grass_prints_on_creation(self, capsys):
        """LawnGrass печатает repr при создании."""
        LawnGrass(
            "Трава", "Desc", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        captured = capsys.readouterr()
        assert "LawnGrass(" in captured.out
        assert "Трава" in captured.out

    def test_product_repr_format(self):
        """__repr__ возвращает строку в правильном формате."""
        product = Product("Test", "Desc", 100.0, 5)
        expected = "Product('Test', 'Desc', 100.0, 5)"
        assert repr(product) == expected

    def test_smartphone_repr_format(self):
        """__repr__ Smartphone возвращает строку в правильном формате."""
        phone = Smartphone(
            "iPhone", "Desc", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        expected = (
            "Smartphone('iPhone', 'Desc', 100000.0, 5, "
            "95.5, 'iPhone 15', 256, 'Чёрный')"
        )
        assert repr(phone) == expected

    def test_lawn_grass_repr_format(self):
        """__repr__ LawnGrass возвращает строку в правильном формате."""
        grass = LawnGrass(
            "Трава", "Desc", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        expected = (
            "LawnGrass('Трава', 'Desc', 500.0, 10, "
            "'Россия', 7, 'Зелёный')"
        )
        assert repr(grass) == expected


class TestCategoryWithAbstract:
    """Тесты Category с абстрактными продуктами."""

    @staticmethod
    def setup_method():
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_with_smartphone(self, capsys):
        """Категория может содержать Smartphone."""
        phone = Smartphone(
            "iPhone", "Desc", 100000.0, 5,
            95.5, "iPhone 15", 256, "Чёрный"
        )
        capsys.readouterr()  # очищаем вывод миксина
        category = Category("Электроника", "Описание", [phone])
        assert "iPhone" in category.products

    def test_category_with_lawn_grass(self, capsys):
        """Категория может содержать LawnGrass."""
        grass = LawnGrass(
            "Трава", "Desc", 500.0, 10,
            "Россия", 7, "Зелёный"
        )
        capsys.readouterr()
        category = Category("Сад", "Описание", [grass])
        assert "Трава" in category.products


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
