import math

def f(x):
    return x**2 + math.sin(x) - 12 * x - 0.25

def df(x):
    return 2 * x + math.cos(x) - 12

def find_root_by_newton(x0, epsilon, max_iterations):
    n = 0
    while n < max_iterations:
        x1 = x0 - f(x0) / df(x0)
        if x1 > 0:
            if abs(x1 - x0) < epsilon:
                return x1, n+1
            else:
                x0 = x1
        else:
            x0 = x1
        n += 1
    return None, None

x0 = 6
epsilon = 10**-4
max_iterations = 1000
root, n = find_root_by_newton(x0, epsilon, max_iterations)

print("Найменший додатній корінь:", root)
print("Кількість кроків:", n)
