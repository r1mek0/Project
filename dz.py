result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a должно быть больше или равно b")
        if b == 0:
            raise ZeroDivisionError("b не должно быть равно нулю")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as ze:
        print(f"ZeroDivisionError: {ze}")
    except Exception as e:
        print(f"Other Exception: {e}")
    return None

data = {(10, 2): 2, (2, 5): 5, ("123", 4): 4, (18, 0): 0, (8, 4): 4}

for key in data:
    res = divider(key[0], data[key])
    if res is not None:
        result.append(res)

print(result)

