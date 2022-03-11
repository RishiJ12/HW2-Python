import time

def calculate_time(func):
    def wrapper_func():
        start = time.time()
        func()
        end = time.time()
        print('Total Time ', str(end - start))
    return wrapper_func






