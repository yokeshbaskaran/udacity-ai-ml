print("Hello World!")
print("Hello Python!")

x = 10
print("The value of x is", x)


x = 10
for i in range(10):
    # x += 5
    print("value of i is :", i)

# Error:
#     Traceback (most recent call last):
#   File "d:\Project\2026\python\udacity\tempCodeRunnerFile.py", line 2, in <module>
#     for i in range:
# TypeError: 'type' object is not iterable

# After learning the steps:
x = 10
for i in range(20):
    i += 1
    print("value of i is :", i)
