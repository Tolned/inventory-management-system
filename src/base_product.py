"""Модуль содержит абстрактный базовый класс BaseProduct."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение двух продуктов."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Официальное строковое представление."""
        pass
