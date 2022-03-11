def doubler(func):
    def wrapper_func():
        func()
        func()

    return wrapper_func







