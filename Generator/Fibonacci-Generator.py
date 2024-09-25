def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci_generator()

# Generate and print the first 10 Fibonacci numbers
for _ in range(20):
    print(next(fib_gen), end=" ")
