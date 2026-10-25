"""Модуль доменних винятків.

Містить базові та спеціалізовані класи винятків для обробки помилок.
"""


class BaseError(Exception):
    """Базовий клас для всіх доменних винятків."""

    def __init__(self, message: str) -> None:
        """Ініціалізує базовий виняток.

        Args:
            message: Текстовий опис помилки.
        """
        super().__init__(message)
        self.message: str = message

    def __str__(self) -> str:
        return f"{self.message}"


class ValidationError(BaseError):
    """Виняток, що виникає при помилці валідації даних."""

    def __init__(self, message: str, field_name: str) -> None:
        """Ініціалізує виняток валідації.

        Args:
            message: Текстовий опис помилки.
            field_name: Назва поля з помилкою.
        """
        super().__init__(message)
        self.field_name: str = field_name

    def __str__(self) -> str:
        return f"Помилка у полі '{self.field_name}': {self.message}"


class ResourceError(BaseError):
    """Виняток, що виникає при операціях із ресурсами."""

    def __init__(self, message: str, resource_id: str) -> None:
        """Ініціалізує виняток ресурсу.

        Args:
            message: Текстовий опис помилки.
            resource_id: Ідентифікатор ресурсу.
        """
        super().__init__(message)
        self.resource_id: str = resource_id

    def __str__(self) -> str:
        return f"Помилка ресурсу '{self.resource_id}': {self.message}"


class BusinessLogicError(BaseError):
    """Виняток, що виникає при порушенні правил бізнес-логіки."""

    def __init__(self, message: str, error_code: int) -> None:
        """Ініціалізує виняток бізнес-логіки.

        Args:
            message: Текстовий опис помилки.
            error_code: Унікальний код помилки.
        """
        super().__init__(message)
        self.error_code: int = error_code

    def __str__(self) -> str:
        return f"Помилка логіки (Код {self.error_code}): {self.message}"
