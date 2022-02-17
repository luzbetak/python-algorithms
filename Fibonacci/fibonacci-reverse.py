# Function for Fibonacci number
# https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    # if n is 1,2 return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Driver Program
    print(fibonacci(9))
