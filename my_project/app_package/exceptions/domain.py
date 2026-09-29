"""Модуль доменних виключень."""

class BaseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"

class ValidationError(BaseError):
    def __init__(self, message, field_name):
        super().__init__(message)
        self.field_name = field_name

    def __str__(self):
        return f"Помилка у полі '{self.field_name}': {self.message}"

class ResourceError(BaseError):
    def __init__(self, message, resource_id):
        super().__init__(message)
        self.resource_id = resource_id

    def __str__(self):
        return f"Помилка ресурсу '{self.resource_id}': {self.message}"

class BusinessLogicError(BaseError):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"Помилка логіки (Код {self.error_code}): {self.message}"