class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            raise ZeroDivisionError("Деление на ноль невозможно.")

# Тестирование функциональности калькулятора
if __name__ == "__main__":
    num1 = Calculator(10)
    num2 = Calculator(5)

    print(f"Сложение: {num1 + num2}")
    print(f"Вычитание: {num1 - num2}")
    print(f"Умножение: {num1 * num2}")
    print(f"Деление: {num1 / num2}")
