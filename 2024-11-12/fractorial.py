def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

# Example usage:
n = 10
print(f"Sum of factorials 1!+2!+...+{n}! is: {sum_of_factorials(n)}")