"""Главный модуль для демонстрации работы магазина."""

import os
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from category import Category  # noqa: E402
from product import LawnGrass, Product, Smartphone  # noqa: E402


def main() -> None:
    """Точка входа в программу."""
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
    grass2 = LawnGrass(
        "Премиум трава", "Элитная газонная трава",
        800.0, 15, "Германия", 5, "Изумрудный"
    )
    regular_product = Product(
        "Садовый инвентарь", "Набор инструментов", 3000.0, 10
    )

    print("=== Продукты разных типов ===")
    print(smartphone1)
    print(smartphone2)
    print(grass1)
    print(grass2)
    print(regular_product)
    print()

    electronics = Category(
        "Электроника", "Смартфоны и гаджеты",
        [smartphone1, smartphone2]
    )
    garden = Category(
        "Сад", "Товары для сада",
        [grass1, grass2, regular_product]
    )

    print("=== Категории ===")
    print(electronics)
    print(garden)
    print()

    print("=== Сложение одинаковых классов ===")
    print(f"Стоимость смартфонов: {smartphone1 + smartphone2} руб.")
    print(f"Стоимость травы: {grass1 + grass2} руб.")
    print()

    print("=== Попытка сложить разные классы ===")
    try:
        smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    print("=== Перебор товаров в категории ===")
    for product in electronics:
        print(f"  - {product.name}: {product.price} руб.")
    print()

    print("=== Защита add_product ===")
    invalid_items: list[Any] = ["строка", 100, {"name": "A"}]
    for invalid in invalid_items:
        try:
            electronics.add_product(invalid)
        except TypeError as e:
            print(f"Ошибка при добавлении {type(invalid).__name__}: {e}")
    print()

    print("=== Проверка наследования ===")
    print(f"Smartphone наследует Product: {issubclass(Smartphone, Product)}")
    print(f"LawnGrass наследует Product: {issubclass(LawnGrass, Product)}")
    print(f"smartphone1 — экземпляр Product: {isinstance(smartphone1, Product)}")
    print(f"grass1 — экземпляр Product: {isinstance(grass1, Product)}")


if __name__ == "__main__":
    main()
