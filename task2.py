# Задача 2
import time
def decorator(func):
    def wrapper():
        start = time.time()
        time.sleep(1)
        end = time.time()
        print('Надел костюм Железного-Человека за {} секунд.'.format(end-start))
        func()
        print('Снова надел костюм Железного-Человека за {} секунд.'.format(end-start))
    return wrapper

@decorator
def new():
    import time
    start = time.time()
    time.sleep(1)
    end = time.time()
    print('Снял костюм за {} секунд.'.format(end-start))

new()