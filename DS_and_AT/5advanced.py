import sys

#built in python print signature
#print(*objects, sep='',end='\n', file = sys.stdout,flush = False)

print(1,2,3,4,sep="|",end="\n",flush=True)

# dictionary class signature
# def dict(**kwargs)
d  = dict(a=2, b=3, c=4)
d = {'a': 2, 'b': 3, 'c': 4}
def p(**kwargs):
    for x in kwargs.items():
        print(x)


#________________Anonymous Functions(Lambda)_________

a = [1,3,4,5,2,1,5,5,3,1,6,7]

print(sorted(a))

# sort numbers by their reminders when devided by 2
print(sorted(a, key= lambda x : x % 2))


#____________________Partial Fucntions________________


from functools import partial

def greeting(word, person):
    print(f"{word}, {person}")


say_hi = partial(greeting, "Hi")
say_hello= partial(greeting, "Hello")

say_hi("gani")
say_hello("gani")

#_____________________Closures__________________________

def make_incrementer(step):

    counter = 0

    def incrementer():

        nonlocal counter

        counter += step
        return counter
    return incrementer

increment_ten = make_incrementer(10)

print(increment_ten())#10
print(increment_ten())#20

#___________________Decorators_________________________________


import time

def logging_time(func):
    
    def logger():

        start = time.time()

        func()
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")

    return logger

@logging_time
def calculate_sum():
    return sum(range(100000))

calculate_sum()

