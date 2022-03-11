def func_counter(func):
    counter = 0
    def wrapper_func(*args):
        func_counter.counter += 1
        return func(*args)
    func_counter.counter = 0
    return wrapper_func



