"""Главный модуль для демонстрации работы магазина."""

import os
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from category import Category  # noqa: E402
from exceptions import ZeroQuantityException  # noqa: E402
from product import LawnGrass, Product, Smartphone  # noqa: E402


def main() -> None:
    """Точка входа в программу."""
    print("=== Создание продуктов (миксин печатает repr) ===")
    smartphone1 = Smartphone(
        "iPhone 15 Pro", "Флагман Apple",
        150000.0, 5, 98.5, "iPhone 15 Pro", 256, "Титан"
    )
    smartphone2 = Smartphone(
        "Samsung Galaxy S24", "Флагман Samsung",
        100000.0, 10, 95.0, "Galaxy S24 Ultra", 512, "Чёрный"
    )
    grass1 = LawnGrass(
        "Зелёная трава", "Газонная трава",
        500.0, 20, "Россия", 7, "Зелёный"
    )
    regular_product = Product(
        "Садовый инвентарь", "Набор инструментов", 3000.0, 10
    )
    print()

    print("=== Продукты разных типов ===")
    print(smartphone1)
    print(smartphone2)
    print(grass1)
    print(regular_product)
    print()

    electronics = Category(
        "Электроника", "Смартфоны и гаджеты",
        [smartphone1, smartphone2]
    )
    garden = Category(
        "Сад", "Товары для сада",
        [grass1, regular_product]
    )

    print("=== Категории ===")
    print(electronics)
    print(garden)
    print()

    print("=== Сложение одинаковых классов ===")
    print(f"Стоимость смартфонов: {smartphone1 + smartphone2} руб.")
    print()

    print("=== Попытка сложить разные классы ===")
    try:
        smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    print("=== Проверка наследования ===")
    from base_product import BaseProduct
    print(f"Product наследует BaseProduct: "
          f"{issubclass(Product, BaseProduct)}")
    print(f"Smartphone наследует Product: "
          f"{issubclass(Smartphone, Product)}")
    print(f"LawnGrass наследует Product: "
          f"{issubclass(LawnGrass, Product)}")
    print()

    print("=== Попытка создать BaseProduct (должна быть ошибка) ===")
    try:
        eval("BaseProduct('Test', 'Desc', 100.0, 5)")
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    print("=== Защита add_product ===")
    invalid_items: list[Any] = ["строка", 100, {"name": "A"}]
    for invalid in invalid_items:
        try:
            electronics.add_product(invalid)
        except TypeError as e:
            print(f"Ошибка при добавлении {type(invalid).__name__}: {e}")

    print("\n=== Обработка исключений ===")
    print("\n--- Попытка создать продукт с quantity=0 ---")
    try:
        Product("Тест", "Описание", 100.0, 0)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- Средний ценник товаров ---")
    print(f"Средний ценник 'Электроника': {electronics.average_price()} руб.")
    print(f"Средний ценник 'Сад': {garden.average_price()} руб.")

    empty_category = Category("Пустая", "Без товаров")
    print(f"Средний ценник 'Пустая': {empty_category.average_price()} руб.")

    print("\n--- Пользовательское исключение ZeroQuantityException ---")
    try:
        # Создаём продукт в обход __init__, чтобы получить quantity=0
        bad_product = Product.__new__(Product)  # type: ignore[call-overload]
        bad_product.name = "Невалидный товар"
        bad_product.description = "Товар с нулевым количеством"
        bad_product._Product__price = 100.0
        bad_product.quantity = 0
        electronics.add_product(bad_product)
    except ZeroQuantityException as e:
        print(f"Перехвачено исключение: {e}")


if __name__ == "__main__":  # pragma: no cover
    main()
