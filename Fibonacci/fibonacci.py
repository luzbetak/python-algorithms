# Display the Fibonacci sequence
total = 10
last, prev = 0, 1
count = 0

print("Fibonacci sequence:")
while count < total:
    print(last)
    nth = last + prev

    # update values
    last = prev
    prev = nth
    count += 1
