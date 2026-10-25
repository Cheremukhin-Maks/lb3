"""Точка входу для запуску пакета через `python -m app_package`."""

# Форма імпорту 2: Абсолютний імпорт цілого модуля
import app_package.services.processors

# Форма імпорту 3: Вибірковий імпорт конкретних імен
from app_package.exceptions.domain import BaseError, ValidationError, ResourceError, BusinessLogicError
from app_package.services.processors import check_balance, load, payment


def main() -> None:
    print('Print("Test 1")')
    try:
        check_balance(-1)
    except ValidationError as er:
        print(er)

    print('\nPrint("Test 2")')
    try:
        check_balance(-5)
    except BaseError as er:
        print(er)

    print('\nPrint("Test 3")')
    try:
        load("file.txt")
    except ResourceError as er:
        print(er)
        print(f"Першопричина: {repr(er.__cause__)}")

    print('\nPrint("Test 4")')
    try:
        payment(-175)
    except BusinessLogicError as e:
        print(e)

    print("\n" + "=" * 20 + " ДЕМОНСТРАЦІЯ ІНТРОСПЕКЦІЇ " + "=" * 20)
    print(f"Ім'я функції (__name__): {check_balance.__name__}")
    print(f"Анотації типів (__annotations__): {check_balance.__annotations__}")
    print(f"Текст docstring (__doc__):\n{check_balance.__doc__}")
    print("=" * 67)

    print("\n=== ДЕМОНСТРАЦІЯ ОБМЕЖЕННЯ __all__ ===")
    from app_package import check_balance as cb, payment as p
    print(f"Успішно імпортовано через __all__: {cb.__name__}, {p.__name__}")


if __name__ == "__main__":
    main()
