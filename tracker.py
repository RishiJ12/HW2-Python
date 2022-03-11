def func_counter(func):
    counter = 0
    def wrapper_func(*args):
        counter += 1
        func(*args)
    return wrapper_func



