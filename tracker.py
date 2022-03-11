def func_counter(func):
    counter
    def wrapper_func(*args):
        counter += 1
        return func(*args)
    counter = 0
    return wrapper_func



