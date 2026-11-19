# Lab Exercise 7: Fibonacci Series Using Recursion
# Student: SHAREVSH.S | USN: 25BTRAD105
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")

