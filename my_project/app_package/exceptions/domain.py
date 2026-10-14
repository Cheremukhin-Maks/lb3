"""Модуль доменних винятків.

Цей модуль містить базові та спеціалізовані класи винятків,
що використовуються для обробки помилок у доменній логіці додатка.
"""

class BaseError(Exception):
    """Базовий клас для всіх доменних винятків.

    Attributes:
        message: Повідомлення з описом помилки.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        """Ініціалізує базовий виняток.

        Args:
            message: Текстовий опис помилки.
        """

    def __str__(self):
        return f"{self.message}"
        

class ValidationError(BaseError):
    """Виняток, що виникає при помилці валідації даних.

    Attributes:
        field_name: Назва поля, у якому виникла помилка.
    """
    def __init__(self, message, field_name):
        super().__init__(message)
        self.field_name = field_name
        """Ініціалізує виняток валідації.

        Args:
            message: Текстовий опис помилки.
            field_name: Назва поля, де виявлено некоректні дані.
        """

    def __str__(self):
        return f"Помилка у полі '{self.field_name}': {self.message}"

class ResourceError(BaseError):
    """Виняток, що виникає при операціях із ресурсами (наприклад, ресурс не знайдено).

    Attributes:
        resource_id: Ідентифікатор ресурсу, з яким пов'язана помилка.
    """
    def __init__(self, message, resource_id):
        super().__init__(message)
        self.resource_id = resource_id
        """Ініціалізує виняток ресурсу.

        Args:
            message: Текстовий опис помилки.
            resource_id: Унікальний ідентифікатор ресурсу.
        """

    def __str__(self):
        return f"Помилка ресурсу '{self.resource_id}': {self.message}"

class BusinessLogicError(BaseError):
    """Виняток, що виникає при порушенні правил бізнес-логіки.

    Attributes:
        error_code: Внутрішній код помилки для категорії або системи.
    """
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
        """Ініціалізує виняток бізнес-логіки.

        Args:
            message: Текстовий опис помилки.
            error_code: Унікальний код помилки.
        """

    def __str__(self):
        return f"Помилка логіки (Код {self.error_code}): {self.message}"
