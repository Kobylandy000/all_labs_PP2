import mymodule

a = mymodule.person1["age"]
print(a)


from mymodule import person1

print (person1["age"])


import mymodule as mx

a = mx.person1["age"]
print(a)