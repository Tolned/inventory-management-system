"""Тесты для класса Product."""

import sys

sys.path.insert(0, "./src")

from product import Product  # noqa: E402


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self, capsys):
        """Тест 1: Проверить корректность инициализации продукта."""
        product = Product("Samsung", "Смартфон", 50000.0, 10)
        capsys.readouterr()  # очищаем вывод миксина

        assert product.name == "Samsung"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_validation_valid_data(self, capsys):
        """Тест 2: Проверить валидацию корректных данных."""
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()
        assert product.price == 100.0
        assert product.quantity == 5

    def test_product_validation_invalid_price(self, capsys):
        """Тест 3: Проверить поведение при некорректной цене.

        По ТЗ: выводится print, цена не меняется.
        """
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()

        # При некорректной цене price не должен измениться
        product.price = -50
        captured = capsys.readouterr()

        assert product.price == 100.0  # осталось старое значение
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_product_validation_invalid_quantity(self, capsys):
        """Тест 4: Проверить корректность количества.

        param: quantity — публичный атрибут, можно менять.
        """
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()

        # quantity — публичный атрибут, можно менять
        product.quantity = 0
        assert product.quantity == 0

        product.quantity = -5
        assert product.quantity == -5

    def test_product_price_property(self, capsys):
        """Тест 5: Проверить свойство price."""
        product = Product("Test", "Desc", 100.0, 5)
        capsys.readouterr()

        assert product.price == 100.0

        product.price = 200.0
        assert product.price == 200.0

        # При невалидной цене значение не меняется
        product.price = -10
        captured = capsys.readouterr()
        assert product.price == 200.0
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_product_str(self, capsys):
        """Тест 6: Проверить __str__."""
        product = Product("Samsung", "Смартфон", 50000.0, 10)
        capsys.readouterr()

        expected = "Samsung, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_repr(self, capsys):
        """Тест 7: Проверить __repr__."""
        product = Product("Samsung", "Смартфон", 50000.0, 10)
        captured = capsys.readouterr()

        expected = "Product('Samsung', 'Смартфон', 50000.0, 10)"
        assert captured.out.strip() == expected
        assert repr(product) == expected

    def test_product_add_same_class(self, capsys):
        """Тест 8: Сложение продуктов одного класса."""
        p1 = Product("A", "D", 100.0, 10)
        p2 = Product("B", "D", 200.0, 5)
        capsys.readouterr()

        result = p1 + p2
        expected = 100.0 * 10 + 200.0 * 5  # 2000
        assert result == expected
