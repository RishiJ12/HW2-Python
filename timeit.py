import time

def calculate_time(func):
    def wrapper_func():
        start = time.time()
        func()
        end = time.time()
        print('Total time ', str(end - start))
    return wrapper_func






