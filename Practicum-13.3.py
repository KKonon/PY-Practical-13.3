#На вход приходит случайно 10-ти значное число,нужно посчитать сумму его цифр.

import random

a = random.randint(1000000000, 9999999999)
r = 0

for i in str(a):
    m = i
    s = r
    r = int(i) + int(r)
print("10-ти значное число:", a, "Сумма 10-ти знач числа:", r)
