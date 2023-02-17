number = int(input("Введите номер места: "))

if number in range(1,37):
    if number % 2 == 0:
        print("У Вас верхнее в купе")
    else:
        print("У Вас нижнее в купе")
if number in range(37,55):
    if number % 2 ==0:
        print("У Вас верхнее боковое")
    else:
        print("У Вас нижнее боковое")
if number not in range(1,55):
    print("Такого места нет")