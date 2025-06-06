import os
import tempfile
import time

import pytest

from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(10, 15)
    captured = capsys.readouterr()
    assert captured.out == "my_function 25\n"


def test_log_error(capsys):
    @log()
    def faulty_function(x, y):
        return x / y
    faulty_function(1, 0)  # Это вызовет ZeroDivisionError
    captured = capsys.readouterr()
    assert captured.out == "faulty_function error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_with_filename():
    with tempfile.NamedTemporaryFile(dir='.', delete=False) as temp_file:
        temp_file_name = temp_file.name

        @log(filename=temp_file_name)
        def my_function(x, y):
            return x + y

        my_function(10, 15)
        with open(temp_file_name, 'r') as f:
            content = f.read()
            assert content == "my_function 25"

    time.sleep(2)
    os.remove(temp_file_name)


def test_log_with_filename_error():
    with tempfile.NamedTemporaryFile(dir='.', delete=False) as temp_file:
        temp_file_name = temp_file.name

        @log(filename=temp_file_name)
        def my_error_function(x, y):
            return x / y

        my_error_function(10, 0)
        with open(temp_file_name, 'r') as f:
            content = f.read()
            assert content == "my_error_function error: ZeroDivisionError. Inputs: (10, 0), {}"

    time.sleep(2)
    os.remove(temp_file_name)
