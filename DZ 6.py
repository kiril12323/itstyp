result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("The divisor is greater than the dividend.")
        if b > 100:
            raise IndexError("The divisor is too large (greater than 100).")
        return a / b
    except ZeroDivisionError:
        print(f"ZeroDivisionError: Division by zero is not allowed. a={a}, b={b}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Input data with corrected issue (keys should not include unhashable types like lists)
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        key = int(key)  # Ensure keys are integers
        res = divider(key, value)
        if res is not None:  # Only append valid results
            result.append(res)
    except (ValueError, TypeError) as e:
        print(f"Error with key-value pair ({key}, {value}): {e}")

print("Result:", result)