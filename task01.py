                            # Task 1: Calculate Factorial Using a Recursion

n = int(input("enter a number :"))
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
print("factorial of" ,n ,"is" ,factorial_recursive(n))


# output
# enter a number :5
# factorial of 5 is 120
