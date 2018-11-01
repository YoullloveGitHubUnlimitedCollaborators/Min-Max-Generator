import random

def FindMax(data):          # Функция поиска максимума
    Max = 0
    for x in data:
        if type(x) == int:
            if x > Max:
                Max = x
    return Max



def FindMin(data):          # Функция поиска минимума
    Min = 0
    for x in data:
        if type(x) == int:
            if x < Min:
                Min = x
    return Min


data = ['string',4,0,8,9,6,5,4,3,'string','gav',5.5,6]
print("Max:",FindMax(data))
print("Min:",FindMin(data))

print("Числа кратные 6:")
generator = [ x  for x in range(0,100) if x % 6 == 0]  # Генератор чисел кратных 6
for i in generator:                                    # Итеретор генератора
    print(i)

