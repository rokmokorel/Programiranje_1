odgovor = 42


def fibonacci(n):
    a = b = 0
    for i in range(n):
        a, b = b, a + b
    return a
print(fibonacci(42))
