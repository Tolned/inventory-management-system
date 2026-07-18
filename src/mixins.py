"""Модуль содержит класс-миксин InfoMixin."""


class InfoMixin:
    """Миксин, печатающий информацию о создании объекта."""

    def __init__(self) -> None:
        """Печатает repr объекта после инициализации."""
        super().__init__()
        print(repr(self))
