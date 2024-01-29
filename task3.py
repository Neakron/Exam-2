#Задача 3
class Func:  #Для абстракации
    def zvonok(self):
        print('Этот телефон может звонить!')

    def sleep(self):
        print('Я не могу работать 8 часов.')

class Phone(Func):   #Главный класс
    def __init__(self, name, system, color):
        super().__init__()
        self._name = name
        self._system = system
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def system(self):
        return self._system

    @property
    def color(self):
        return self._color

    @system.setter
    def system(self, new_system):
        self._system = new_system

phone1 = Phone('Xiaomi', 'Android 13.0', 'Black')
phone1.new_system = 'Android 12.0'

print('Инкапсуляция: \n')
print(phone1._name)
print(phone1._system)
print(phone1._color)
print(phone1.new_system)
print('-'*80, '\nАбстракция: \n')  #Абстракция для Phone
phone1.zvonok()

class WorkPhone(Phone):  #Класс наследствие
    def __init__ (self, name, system, color, access, time):
        super().__init__(name, system, color)
        self._access = access
        self._time = time

    @property
    def access(self):
        return self._access

    @property
    def time(self):
        return self._time

work_phone = WorkPhone('Xiaomi', 'Android 13.0', 'Black', 'с доступом в Интерент', '8 часов')
print('-'*80, '\nНаследование: \n')
print(work_phone._name)
print(work_phone._system)
print(work_phone._color)
print(work_phone._access)
print(work_phone._time)

print('-'*80, '\nАбстракция: \n') #Абстракция для WorkPhone
work_phone.zvonok()

class Planshet():  # Для полиморфизма
    def sleep(self):
        print('Разряжаюсь так же быстро, как заканчиваются твои деньги.')

def razryad(technic):
    technic.sleep()
planshet = Planshet()

print('-'*80, '\nПолиморфизм: \n')
razryad(phone1)   #основной телефон
razryad(work_phone)  #рабочий телефон
razryad(planshet)  #планшет