"""Модуль із сервісними функціями перевірки та обробки даних."""

from typing import Union, Optional
# Форма імпорту 1: Відносний імпорт між модулями одного пакета
from ..exceptions.domain import ValidationError, ResourceError, BusinessLogicError


def check_balance(bal: Union[int, float]) -> None:
    """Перевіряє баланс користувача на наявність від'ємного значення."""
    if bal < 0:
        raise ValidationError("Баланс не може бути від'ємним", field_name="Баланс")
    print("Баланс перевірено")


def load(filename: str) -> str:
    """Зчитує дані з текстового файлу."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        raise ResourceError("Не вдалося відкрити файл", resource_id=filename) from e


def payment(amount: Union[int, float]) -> Optional[bool]:
    """Виконує платіж за бізнес-логікою програми."""
    try:
        if amount <= 0:
            raise BusinessLogicError("Сума платежу повинна бути більша за 0", error_code=87)
        return True
    except BusinessLogicError:
        print("Помилка платежу")
        raise
