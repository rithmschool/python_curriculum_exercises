import math
from functools import wraps
import re

def get_next_multiple(num, count=2):
    # prevent StopIteration
    while True:
        new_count = count
        new_num = 0
        while new_count > 0:
            new_num = new_num + num
            new_count = new_count-1
        count = count+1
        yield (new_num, count)

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    sqr = int(math.sqrt(num)) + 1

    for divisor in range(3, sqr, 2):
        if num % divisor == 0:
            return False
    return True

def get_next_prime(num):
    for val in range(num+1,1000):
        if(is_prime(val)):
            yield val


def double_result(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        return fn(*args, **kwargs) * 2
    return inner

def only_even_parameters(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if arg % 2 != 0]):
            return "Please add even numbers"
        return fn(*args, **kwargs)
    return inner

def sum_index(collection):
    total = 0
    for idx,val in enumerate(collection):
        total = total + idx

    return total

def remove_vowels(string):
    return re.sub("[aeiou]","",string)

def collect_email(email):
    return re.findall(r".*@", email)[0][:-1]

def collect_domain_name(domain):
    return re.findall(r"\..*", domain)[0][1:]

def valid_phone_number(number):
    return bool(re.match(r"(1-|^)\d{3}-\d{3}-\d{4}",number))


