import time

def calculate_time(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        total_time = time.time()
        # first item in the args, ie `args[0]` is `self`
        print(f' Total time {total_time:.4s}')
        return result
    return timeit_wrapper






