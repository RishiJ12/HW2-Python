counter = 0
def func_counter(func):
    global counter
    def wrapper_func(*args):
        counter += 1
        func(*args)
    counter = 0
    return wrapper_func



