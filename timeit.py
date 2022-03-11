import time

def calculate_time(func):
    def wrapper_func():
        start = time.time()
        end = time.time()
        print('Total time ', str(end - start))
        return func()
    return wrapper_func






