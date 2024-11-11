# non-recursive 

def fibonacci(n):
    num1, num2 = 0, 1
    for _ in range(n):
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2

# Main Function
if __name__ == "__main__":
    print("Fibonacci numbers by non-recursive")
    N = int(input("Enter an integer: "))
    fibonacci(N)
print(" ")



# recursive 

def fib(n):
    # Function 
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Main function 
if __name__ == "__main__":
    print("Fibonacci numbers by recursive")
    N = int(input("Enter an integer: "))
    for i in range(N):
        print(fib(i), end=" ")