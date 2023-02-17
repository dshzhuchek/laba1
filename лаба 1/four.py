color1 = input("Введите первый цвет")
color2 = input("Введите второй цвет")

if (color1 == 'красный' or color1 == 'синий' or color1 == 'желтый') and (color2 == 'красный' or color2 == 'синий' or color2 == 'желтый'):
    if color1=='красный' and color2=='синий':
        print('фиолетовый')
    if color1=='красный' and color2=='желтый':
        print('оранжевый')
    if color1=='синий' and color2=='желтый':
        print('зеленый')
else:
    print('Можно вводить только красный, синий или зеленый')

