def func_counter(func):
    func.counter = 0
    def wrapper(*args):
        func.counter += 1
        func(*args)
    return wrapper






