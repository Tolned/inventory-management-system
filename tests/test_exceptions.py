"""Тесты для обработки исключений и метода average_price."""

import sys

import pytest

sys.path.insert(0, "./src")

from category import Category  # noqa: E402
from exceptions import ZeroQuantityException  # noqa: E402
from product import LawnGrass, Product, Smartphone  # noqa: E402


class TestProductZeroQuantity:
    """Тесты для проверки ValueError при quantity=0."""

    def test_product_zero_quantity_raises_value_error(self):
        """Product с quantity=0 выбрасывает ValueError."""
        with pytest.raises(
            ValueError,
            match="Товар с нулевым количеством не может быть добавлен"
        ):
            Product("Test", "Desc", 100.0, 0)

    def test_smartphone_zero_quantity_raises_value_error(self):
        """Smartphone с quantity=0 выбрасывает ValueError."""
        with pytest.raises(ValueError):
            Smartphone(
                "iPhone", "Desc", 100000.0, 0,
                95.5, "iPhone 15", 256, "Чёрный"
            )

    def test_lawn_grass_zero_quantity_raises_value_error(self):
        """LawnGrass с quantity=0 выбрасывает ValueError."""
        with pytest.raises(ValueError):
            LawnGrass(
                "Трава", "Desc", 500.0, 0,
                "Россия", 7, "Зелёный"
            )

    def test_product_positive_quantity_works(self, capsys):
        """Product с quantity>0 создаётся нормально."""
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()
        assert product.quantity == 5


class TestCategoryAveragePrice:
    """Тесты для метода average_price."""

    @staticmethod
    def setup_method():
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_average_price_with_products(self, capsys):
        """Средний ценник при наличии товаров."""
        products = [
            Product("A", "D", 100.0, 5),
            Product("B", "D", 200.0, 10),
            Product("C", "D", 300.0, 3),
        ]
        capsys.readouterr()
        category = Category("Тест", "Описание", products)
        assert category.average_price() == 200.0

    def test_average_price_empty_category(self):
        """Средний ценник для пустой категории — 0."""
        category = Category("Тест", "Описание")
        assert category.average_price() == 0.0

    def test_average_price_single_product(self, capsys):
        """Средний ценник при одном товаре."""
        product = Product("A", "D", 500.0, 10)
        capsys.readouterr()
        category = Category("Тест", "Описание", [product])
        assert category.average_price() == 500.0

    def test_average_price_with_smartphones(self, capsys):
        """Средний ценник для смартфонов."""
        phones = [
            Smartphone(
                "iPhone", "D", 100000.0, 5,
                95.5, "iPhone 15", 256, "Чёрный"
            ),
            Smartphone(
                "Samsung", "D", 80000.0, 10,
                90.0, "Galaxy S24", 128, "Белый"
            ),
        ]
        capsys.readouterr()
        category = Category("Электроника", "Описание", phones)
        assert category.average_price() == 90000.0


class TestZeroQuantityException:
    """Тесты для пользовательского исключения."""

    def test_zero_quantity_exception_message(self):
        """ZeroQuantityException содержит правильное сообщение."""
        exc = ZeroQuantityException()
        assert "Товар с нулевым количеством" in str(exc)

    def test_zero_quantity_exception_custom_message(self):
        """ZeroQuantityException принимает кастомное сообщение."""
        exc = ZeroQuantityException("Моё сообщение")
        assert "Моё сообщение" in str(exc)

    def test_zero_quantity_exception_is_exception(self):
        """ZeroQuantityException — наследник Exception."""
        assert issubclass(ZeroQuantityException, Exception)

    def test_add_product_with_zero_quantity_raises(self, capsys):
        """add_product с quantity=0 выбрасывает ZeroQuantityException."""
        category = Category("Тест", "Описание")
        product = Product.__new__(Product)  # type: ignore[call-overload]
        product.name = "Test"
        product.description = "Desc"
        product._Product__price = 100.0
        product.quantity = 0
        capsys.readouterr()

        with pytest.raises(ZeroQuantityException):
            category.add_product(product)

    def test_add_product_success_prints_message(self, capsys):
        """Успешное добавление продукта печатает сообщение."""
        category = Category("Тест", "Описание")
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()

        category.add_product(product)
        captured = capsys.readouterr()

        assert "успешно добавлен" in captured.out
        assert "Обработка добавления товара завершена" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
