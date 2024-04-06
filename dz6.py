import random


class Cipher:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self._perform_operation())

    def _perform_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            result = self.number + operand
        elif operation == '-':
            result = self.number - operand
        elif operation == '*':
            result = self.number * operand
        elif operation == '/':
            operand = operand if operand != 0 else 1
            result = self.number / operand

        return result


if __name__ == "__main__":
    number = int(input("Введите число: "))
    cipher = Cipher(number)
    print("Результат вычислений:", cipher)
