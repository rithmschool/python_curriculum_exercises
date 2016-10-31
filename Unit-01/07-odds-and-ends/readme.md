# Odds and Ends

Research the `zip` method, what does it do? Start [here](http://pavdmyt.com/python-zip-fu/)

### `get_next_multiple`

This function should accept a number and return the next number that is divisible by it

```py
genMultipleOfTwo = get_next_multiple(2)
next(genMultipleOfTwo) # 2
next(genMultipleOfTwo) # 4
next(genMultipleOfTwo) # 6
next(genMultipleOfTwo) # 8

genMultipleofThirteen = get_next_multiple(13)

next(genMultipleofThirteen) # 13
next(genMultipleofThirteen) # 26
next(genMultipleofThirteen) # 39
next(genMultipleofThirteen) # 52
```

### `is_prime` 

This function should accept a number and return True or False if the number is a prime number. 

```py
is_prime(11) # True
is_prime(122) # False
```

### `get_next_prime` 

This function should return a generator that yields in the next prime number. The highest it should go should be 1000.

```py
gen = get_next_prime()

next(gen)
```

### `double_result`

This decorator function should return the result of another function multiplied by two

```py
def add(a,b):
    return a+b

add(5,5) # 10

@double_result
def add(a,b):
    return a+b

add(5,5) # 20
```

### `only_even_parameters`

This decorator function should only allow a function to have even parameters or else return the string "Please only use even numbers!"

```py
@only_even_parameters
def add(a,b):
    return a+b

add(5,5) # "Please add even numbers!"
add(4,4) # 8

@only_even_parameters
def multiply(a,b,c,d,e):
    return a*b*c*d*e
```

### `sum_index`

This function should accept a list or tuple and return the sum of each index. As a bonus, make this function able to accept a variable number of arguments.

```py
sum_index([1,2,3,4]) # 6
sum_index((1,2,3,4)) # 
```

### `remove_vowels`

This function should accept a string and return a new string with all vowels removed. You **must** use the `re` module to solve this!

```py

remove_vowels("awesome") # wsm
remove_vowels("MAtt") # Mtt
```

### `collect_email`

This function should accept a string and return everything before the `@`. You **must** use the `re` module to solve this!

```py
collect_email('elie@rithmschool.com') # elie
collect_email('tom@gmail.com') # tom
```

### `collect_domain_name`

This function should accept a string and return everything after the `@`. You **must** use the `re` module to solve this!

```py
collect_domain_name('elie@rithmschool.com') # rithmschool.com
collect_domain_name('tom@gmail.com') # gmail.com
```

### `valid_phone_number`

This function should accept a string and return True or False if it is a valid `US` phone number. You **must** use the `re` module to solve this!

```py
valid_phone_number("1-567-425-1234") # True
valid_phone_number("123-456-7894") # True
valid_phone_number("173-495-1234") # True
valid_phone_number("1-973-495-124") # False
valid_phone_number("173-49-1234") # False
```
