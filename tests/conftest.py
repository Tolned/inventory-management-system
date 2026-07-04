"""Фикстуры и настройка путей для тестов."""

import sys
from pathlib import Path

import pytest

# Добавляем src в sys.path, чтобы импорты работали
src_path = str(Path(__file__).parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from category import Category  # noqa: E402
from product import Product  # noqa: E402


@pytest.fixture
def sample_product():
    """Создать тестовый товар."""
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_products():
    """Создать список тестовых товаров."""
    return [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 10),
        Product("Product 3", "Description 3", 50.0, 3),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Создать тестовую категорию."""
    return Category("Test Category", "Test Description", sample_products)


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбросить счётчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
