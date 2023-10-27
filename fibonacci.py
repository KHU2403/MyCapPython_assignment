#task 1
# Function to generate a Fibonacci series up to n terms
def generate_fibonacci(n):
    fibonacci_series = []
    if n <= 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
    elif n >= 2:
        fibonacci_series.extend([0, 1])
        for i in range(2, n):
            next_number = fibonacci_series[i - 1] + fibonacci_series[i - 2]
            fibonacci_series.append(next_number)
    return fibonacci_series

# Number of terms in the Fibonacci series
n = 13  

fib_series = generate_fibonacci(n)
print(f"Fibonacci series with {n} terms: {fib_series}")
