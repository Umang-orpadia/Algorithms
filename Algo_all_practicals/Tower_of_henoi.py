def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
print(factorial(5)) # Output: 120



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10)) # Output: 55



def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
tower_of_hanoi(3, 'A', 'C', 'B') # Output: Moves required to solve the puzzle



def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
print(iterative_factorial(5)) # Output: 120




def iterative_fibonacci(n):
    if n <= 1:
        return n
    else:
        fib_0 = 0
        fib_1 = 1
        for i in range(2, n+1):
            fib = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib
        return fib_1

# Example usage
print(iterative_fibonacci(10)) # Output: 55
