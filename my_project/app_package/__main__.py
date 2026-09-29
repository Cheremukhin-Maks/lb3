"""Головний модуль для тестування функцій обробки помилок."""

import sys
from typing import Union, Optional
from app_package.exceptions.domain import BaseError, ValidationError, ResourceError, BusinessLogicError

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
            raise BusinessLogicError("Сумма платежу повинна бути більша за 0", error_code=87)
        return True
    except BusinessLogicError:
        print("Помилка платежу")
        raise

if __name__ == "__main__":
    print("Print(\"Test 1\")")
    try:
        check_balance(-1)
    except ValidationError as er:
        print(er)

    print("\nPrint(\"Test 2\")")
    try:
        check_balance(-5)
    except BaseError as er:
        print(er)

    print("\nPrint(\"Test 3\")")
    try:
        load("file.txt")
    except ResourceError as er:
        print(er)
        print(f"Першопричина: {repr(er.__cause__)}")

    print("\nPrint(\"Test 4\")")
    try:
        payment(-175)
    except BusinessLogicError as e:
        print(e)

    print("\n" + "="*20 + " ДЕМОНСТРАЦІЯ ІНТРОСПЕКЦІЇ " + "="*20)
    print(f"Ім'я функції (__name__): {check_balance.__name__}")
    print(f"Анотації типів (__annotations__): {check_balance.__annotations__}")
    print(f"Текст docstring (__doc__):\n{check_balance.__doc__}")
    print("="*67)

    print("\n=== ВИКЛИК СИСТЕМНОЇ ФУНКЦІЇ help() ===")
    help(payment)
