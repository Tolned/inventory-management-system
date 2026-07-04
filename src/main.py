"""Главный модуль для демонстрации работы системы."""

from category import Category  # ✅ без src.
from product import Product  # ✅ без src.


def main() -> None:
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14
    )

    print("=== Товары ===")
    for p in (product1, product2, product3):
        print(p)
    print()

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(f"=== Категория: {category1.name} ===")
    print(category1.products_display)
    print(f"Количество товаров: {category1.products_count}")
    print(f"Общее количество единиц: {category1.total_quantity}")
    print(f"Общая стоимость: {category1.get_total_value():.2f} руб.")
    print(f"Средняя цена: {category1.get_average_price():.2f} руб.")

    most_expensive = category1.get_most_expensive_product()
    if most_expensive:
        print(f"Самый дорогой товар: {most_expensive}")

    cheapest = category1.get_cheapest_product()
    if cheapest:
        print(f"Самый дешёвый товар: {cheapest}")

    found = category1.get_product_by_name("Iphone 15")
    if found:
        print(f"Найден товар: {found}")
    print()

    print("=== Удаление товара ===")
    print(f"До удаления: {category1.products_count} товаров")
    category1.remove_product(product3)
    print(f"После удаления: {category1.products_count} товаров")
    print(
        f"Общее количество единиц после удаления: "
        f"{Category.product_count}"
    )
    print()

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться "
        "просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(f"=== Категория: {category2.name} ===")
    print(category2.products_display)
    print(f"Общая стоимость: {category2.get_total_value():.2f} руб.\n")

    print("=== Общая статистика ===")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Общее количество товаров (единиц): {Category.product_count}")


if __name__ == "__main__":
    main()
