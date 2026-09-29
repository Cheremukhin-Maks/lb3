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
       return f"Помилка у полі '{self.resource_id}': {self.message}"


class BusinessLogicError(BaseError):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code


    def __str__(self):
        return f"Помилка у полі '{self.error_code}': {self.message}"



def check_balance(bal):
        if bal < 0:
            raise ValidationError("Баланс не може бути від'ємним", field_name = "Баланс")
        print("Баланс перевірено")


print("Test 1")
try:
    check_balance(-1)
except ValidationError as er:
    print(er)


print("Test 2")
try:
    check_balance(-5)
except BaseError as er:
    print(er)



def load(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError as e:
        raise ResourceError("Не вдалося відкрити файл", resource_id = filename) from e


print("Test 3")
try:
    load("file.txt")
except ResourceError as er:
    print(er)
    print(f"Першопричина: {repr(er.__cause__)}")


def payment(amount):
    try:
        if amount <= 0:
            raise BusinessLogicError("Сумма платежу повинна бути більша за 0", error_code = 87)
    except BusinessLogicError as e:
        print("Помилка платежу")
        raise


print("Test 4")
try:
    payment(-175)
except BusinessLogicError as e:
    print(e)
