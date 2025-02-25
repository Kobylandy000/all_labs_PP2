# Task 1
def square(n):
  for i in range(n):
    if i == 0:
      continue
    print(i**2)

square(5)

#Task 2
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            if i == n or (i == n - 1 and n % 2 == 1):
                print(i)
            else:
                print(i, end=', ')

n = int(input())
even(n)


#Task 3

def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for number in divisible_by_3_and_4(n):
    print(number)

#Task 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("a: "))
b = int(input("b: "))
for sq in squares(a, b):
    print(sq)

#Task 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("n : "))
for num in countdown(n):
    print(num)
