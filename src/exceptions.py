"""Модуль содержит пользовательские исключения для проекта."""


class ZeroQuantityException(Exception):
    """Исключение для товаров с нулевым количеством."""

    def __init__(
        self,
        message: str = "Товар с нулевым количеством не может быть добавлен",
    ) -> None:
        super().__init__(message)
        self.message = message
