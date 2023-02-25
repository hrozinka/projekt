#Factorial_recursive
a=10
def factorial_recursive(a):
    if a == 0:
        return 1
    else:
        return a * factorial_recursive(a-1)
b = factorial_recursive (a)
print("Hodnota faktoriálu " + str(a) + " je " + str(b)+".")