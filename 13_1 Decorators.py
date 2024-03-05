import functools
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


def start_end_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat



@start_end_decorator
def print_name():
    print('Alex')


@start_end_decorator2
def add5(x):
    return x + 5

@repeat(num_times=4)
def greet(name):
    print(f'hello {name}')

def dubug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repl = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repl + kwargs_repr)
        print(f"Calling {func.__name__} ({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned({result!r})")
        return result
    return wrapper

@dubug
@start_end_decorator2
def say_hello(name):
    greeting = f'hello {name}'
    print(greeting)
    return greeting



print_name()
# ----------------------------
result = add5(10)
print(result)
# ----------------------------

print(help(add5))
print(add5.__name__)
# ---------------------------

greet('Alex')
#----------------------------

say_hello('Alex')