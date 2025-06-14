'''''''''
a = float(input('Введите число: '))
b = float(input('Введите число: '))
if a > b:
    print(a)
else:
    print(b)

------------------------------------ 
a = float(input('Введите число: '))
b = float(input('Введите число: '))
if ((a - b) == 135 or (b - a) == 135):
    print('Yes')
else:
    print('No')

-------------------------------------
x = int(input('Введите число от 1 до 12: '))
if x in [1, 2, 12]:
    print('Зима')
elif x in [3, 4, 5]:
    print('Весна')
elif x in [6, 7, 8]:
    print('Лето')
elif x in [9, 10, 11]:
    print('Осень')
else:
    print('Некорректный номер месяца')

--------------------------------------
def number(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')


a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
number(a, b, c)

-----------------------------------
def numbers(a, b, c, d, e):
    if a > 0:
        pologit.append(a)
    if b > 0:
        pologit.append(b)
    if c > 0:
        pologit.append(c)
    if d > 0:
        pologit.append(d)
    if e > 0:
        pologit.append(e)
    print(pologit)

x1 = float(input('Введите число: '))
x2 = float(input('Введите число: '))
x3 = float(input('Введите число: '))
x4 = float(input('Введите число: '))
x5 = float(input('Введите число: '))
n = [x1, x2, x3, x4, x5]
pologit = []
numbers(x1, x2, x3, x4, x5)

--------------------------
def year(x):
    if a > 0:
        g.append(a)
def month(y):
    if b > 0 and b <= 12:
        v.append(b)
    else:
        print('Некорректный номер месяца')
    print(g,v)

a = int(input('Введите число (кол-во лет): '))
b = int(input('Введите число (кол-во месяцев): '))
g = [] # Список куда мы будем складывать введённое значение (год)
v = [] # Список куда мы будем складывать введённое значение (месяц)
year(a)
month(b)
#Так как у нас 1 месяц = 29 дней. Умножим - 12 месяцев * 29 дней = 348 дней в 1 году и т. д.
# Тестовый пример. Укажем a = 7 лет и b = 3 месяца.
# Тогда нужно будет 7 лет * 348 дней в 1 году = 2436 дней в 7 годах
# Затем нужно будет 29 дней * 3 месяца = 87 дней в 3 месяцах
# В конце складываем 2436 + 87 = 2523 дней

result1 = [u * 348 for u in g] # 348 - Кол-во дней в 1 году
result2 = [u * 29 for u in v] # 29 - Кол-во дней в 1 месяце
result3 = result1 + result2
print(result1, result2)
print(result3)

day = sum(result3)
print(day, 'дней')
'''














