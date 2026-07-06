"""Главный модуль для демонстрации работы магазина."""

from category import Category
from product import Product


def main() -> None:
    """Точка входа в программу."""
    smartphone = Product(
        "Samsung Galaxy", "Смартфон с AMOLED экраном", 80000.0, 15
    )
    laptop = Product(
        "MacBook Pro", "Ноутбук для профессионалов", 150000.0, 5
    )
    tablet = Product(
        "iPad Air", "Планшет для работы и развлечений", 60000.0, 10
    )

    print("=== Продукты ===")
    print(smartphone)
    print(laptop)
    print(tablet)
    print()

    electronics = Category(
        "Электроника",
        "Устройства и гаджеты",
        [smartphone, laptop, tablet],
    )

    print("=== Категория ===")
    print(electronics)
    print()

    print("=== Список товаров в категории ===")
    print(electronics.products)

    print("=== Перебор товаров в цикле ===")
    for product in electronics:
        print(f"  - {product.name}: {product.price} руб.")
    print()

    print("=== Демонстрация __add__ ===")
    pair_value = smartphone + laptop
    print(f"Стоимость Samsung + MacBook: {pair_value} руб.")
    print(
        f"  (Samsung: {smartphone.price} x "
        f"{smartphone.quantity} = "
        f"{smartphone.price * smartphone.quantity} руб.)"
    )
    print(
        f"  (MacBook: {laptop.price} x "
        f"{laptop.quantity} = "
        f"{laptop.price * laptop.quantity} руб.)"
    )
    print()

    print("=== Общая стоимость товаров на складе ===")
    products = [smartphone, laptop, tablet]
    total_value = sum(p.price * p.quantity for p in products)
    print(
        f"Samsung: {smartphone.price} x "
        f"{smartphone.quantity} = "
        f"{smartphone.price * smartphone.quantity} руб."
    )
    print(
        f"MacBook: {laptop.price} x "
        f"{laptop.quantity} = "
        f"{laptop.price * laptop.quantity} руб."
    )
    print(
        f"iPad: {tablet.price} x "
        f"{tablet.quantity} = "
        f"{tablet.price * tablet.quantity} руб."
    )
    print(f"Итого: {total_value} руб.")
    print()

    print("=== Создание продукта через new_product ===")
    new_data = {
        "name": "AirPods Pro",
        "description": "Беспроводные наушники",
        "price": 25000.0,
        "quantity": 30,
    }
    airpods = Category.new_product(new_data)
    print(airpods)

    electronics.add_product(airpods)
    print()
    print("=== Категория после добавления AirPods ===")
    print(electronics)


if __name__ == "__main__":
    main()
