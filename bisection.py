import math

def f(x):
    return x**2 + math.sin(x) - 12 * x - 0.25

def find_root_by_bisection(a, b, epsilon):
    c = (a + b) / 2
    n = 0
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c, n
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        n += 1
    return (a + b) / 2, n

a = -1
b = 1
epsilon = 10**-4
root, n = find_root_by_bisection(a, b, epsilon)

print("Найменший додатній корінь:", root)
print("Кількість кроків:", n)
