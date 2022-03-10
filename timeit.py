import time

def calculate_time(func):
    func()
    x = time.time()
    print('Total time ' + str(x))



def test():
    print('')

calculate_time(test)    

