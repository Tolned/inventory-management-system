"""Главный модуль для демонстрации работы системы."""

from category import Category
from product import Product


def main() -> None:
    # Создание товаров
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
    print(f"1. {product1.name}: {product1.price} руб., остаток {product1.quantity} шт.")
    print(f"2. {product2.name}: {product2.price} руб., остаток {product2.quantity} шт.")
    print(f"3. {product3.name}: {product3.price} руб., остаток {product3.quantity} шт.")
    print()

    # Создание категории с товарами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(f"=== Категория: {category1.name} ===")
    print(f"Описание: {category1.description}")
    print("\nТовары в категории:")
    print(category1.products)

    print(f"Количество категорий: {Category.category_count}")
    print(f"Общее количество товаров (по единицам): {Category.product_count}")
    print()

    # Демонстрация класс-метода new_product
    print("=== Создание товара из словаря ===")
    product_data = {
        "name": "Новый смартфон",
        "description": "Тестовый товар",
        "price": 50000.0,
        "quantity": 10
    }
    new_product = Category.new_product(product_data)
    print(f"Создан товар: {new_product.name}, цена: {new_product.price} руб.")
    print()

    # Демонстрация сеттера цены
    print("=== Изменение цены товара ===")
    print(f"Старая цена {product1.name}: {product1.price} руб.")
    product1.price = 190000.0
    print(f"Новая цена {product1.name}: {product1.price} руб.")

    print("\nПопытка установить отрицательную цену:")
    product1.price = -100.0  # Выведет сообщение об ошибке
    print(f"Цена осталась: {product1.price} руб.")
    print()

    # Создание второй категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        [product4]
    )

    print(f"=== Категория: {category2.name} ===")
    print(category2.products)

    print("=== Общая статистика ===")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Общее количество товаров (по единицам): {Category.product_count}")


if __name__ == "__main__":
    main()
