def scenario1(value):
    number = 50
    try:
        res = number + value
        print(f"Успішний результат: {res}")
    except TypeError as e:
        print(f"Перехоплено помилку {e}")


def scenario2(num1, num2):
    try:
        res = num1/num2
    except ZeroDivisionError as e:
        print(f"Перехоплено помилку {e}")
    else:
        print(f"Результат ділення: {res}")
    finally:
        print("Блок finally")


def scenario3(us_input):
    test_l = [1,2,3]
    try:
        index = int(us_input)
        value = test_l[index]
        print(f"Знайдено елемент: {value}")
    except (ValueError, IndexError) as e:
        print(f"Перехоплено помилку {e}")




scenario1(10)
scenario1("string")


scenario2(10, 5)
scenario2(10, 0)


scenario3(1)
scenario3("string")
scenario3(10)

with open("text.txt", "a+", encoding="utf8") as file:
        file.write("Тестовий запис для демонстрації роботи з ресурсом.\n")
        print("Контекстний менеджер успішно відкрив та автоматично закрив файл text.txt.")


