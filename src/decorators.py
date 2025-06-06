from functools import wraps
from typing import Any

from black.lines import Callable


def log(filename: str = None) -> Callable:
    '''Декоратор для логирования исходной функции'''
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            name = func.__name__
            try:
                result = func(*args, **kwargs)
                text_log = f"{name} {result}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(text_log)
                else:
                    print(text_log)
                return result
            except Exception as e:
                text_log = f'{name} error: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(text_log)
                else:
                    print(text_log)
        return wrapper
    return decorator
