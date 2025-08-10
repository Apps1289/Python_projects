# Finding factorial of a number and trailling zeros of a given number

num = int(input("Enter a number to find factorial: "))

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
result = fact(num)
print(f"Factorial of {num} is: {result}")

# counting trailing zeros in factorial
def count_trailling_zeros(result):
    count = 0
    while result % 10 == 0:
        count += 1
        result /= 10
    return count

ans = count_trailling_zeros(result)
print(f"Number of trailing zeros in {num}! is: {ans}")