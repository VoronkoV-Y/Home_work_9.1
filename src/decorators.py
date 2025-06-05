from functools import wraps
from typing import Any

from black.lines import Callable


def log(filename: str = '') -> Callable:
    '''Декоратор для логирования исходной функции'''
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            name = func.__name__
            try:
                result = func(*args, **kwargs)
                text_log = f"{name} {result} \n"
                #return result
                if filename:
                    with open(filename, 'a') as file:
                        file.write(text_log)
                else:
                    print(text_log)
            except Exception as e:
                text_log = f'{name} error: {type(e).__name__}. Inputs: {args}, {kwargs} \n'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(text_log)
                else:
                    print(text_log)
        return wrapper
    return decorator


#@log(filename="mylog.txt")
# @log()
# def my_function(x, y):
#     return x + y
#
# my_function(15, 10)