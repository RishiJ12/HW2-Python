import time

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()
    print('Total Time ', str(end - start))




