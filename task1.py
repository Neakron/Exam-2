# Задача 1
def number(card):
    return (card)
card = input("Введите номер вашей карты: ")
print('Последние 4 цифры вашей краты: ', '*' * 12 + card[-4:])