import math
import time
import functools

# Task 1
def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

# Task 2
def count_case(s):
    return sum(map(str.isupper, s)), sum(map(str.islower, s))

# Task 3
def is_palindrome(s):
    return s == s[::-1]

# Task 4
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}")

# Task 5
def all_true(t):
    return all(t)

# Test
print(multiply_list([2, 3, 4]))  
print(count_case("HelloWorld"))  
print(is_palindrome("madam"))  
delayed_sqrt(25100, 2123)  
print(all_true((True, True, False)))
