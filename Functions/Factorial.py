# Recursion: Calling fn inside a fn
# Exit check is main thing to check
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))    
