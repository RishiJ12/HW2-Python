def func_counter(func):
    def wrapper_func(*args):
        wrapper_func += 1
        return func(*args)
    wrapper_func.counter = 0
    return wrapper_func



