# Functions

### Part I 

Write the following functions

###`difference` 

- this function takes in two parameters and returns the difference of the two

```py
difference(2,2) # 0
difference(0,2) # -2
```

###`product` 

- this function takes in two parameters and returns the product of the two

```py
product(2,2) # 4
product(0,2) # 0
```

###`printDay` 

- this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return undefined

```py
printDay(4) # "Wednesday"
printDay(41) # undefined
```

###`lastElement` 

- this function takes in one parameter (a list) and returns the last value in the list. It should return `undefined` if the list is empty.

```py
lastElement([1,2,3,4]) # 4
lastElement([]) # undefined
```

###`numberCompare` 

- this function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater". If the second number is greater than the first, the function returns "Second is greater". Otherwise the function returns "Numbers are equal"

```py
numberCompare(1,1) # "Numbers are equal"
numberCompare(1,2) # "First is greater"
numberCompare(2,1) # "Second is greater"
```

###`singleLetterCount` 

- this function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.

```py
singleLetterCount('amazing','A') # 2
singleLetterCount('amazing','A') # 2
```

###`multipleLetterCount` 

- this function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.

```py
multipleLetterCount("hello") # {h:1, e: 1, l: 2, o:1}
multipleLetterCount("person") # {p:1, e: 1, r: 1, s:1, o:1, n:1}
```

###`listManipulation` 

- this function should take in three parameters (a list, command, location and value). 
    - If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
    - If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
    - If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
    - If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list

```py
listManipulation([1,2,3], "remove", "end") # 3
listManipulation([1,2,3], "remove", "beginning") # 1
listManipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
listManipulation([1,2,3], "add", "end", 30) # [1,2,3,30]
```

###`isPalindrome` 

- A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns `true` or `false` if it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that `isPalindrome('a man a plan a canal Panama')` returns `true`

```py
isPalindrome('testing') # false
isPalindrome('tacocat') # true
isPalindrome('hannah') # true
isPalindrome('robert') # false
```

### `frequency`

This function accepts a list and a searchTerm (this will always be a primitive value) and returns the number of times the searchTerm appears in the list.

```py
frequency([1,2,3,4,4,4], 4) # 4
frequency([true, false, true, true], false) # 1
```

### `flipCase`

This function accepts a string and a letter and reverses the case of all occurances of the letter in the string.

```py
flipCase("Hardy har har", "h") # "hardy Har Har"
```

### `multiplyEvenNumbers`

This function accepts a list of numbers and returns the product of all even numbers in the list.

```py
multiplyEvenNumbers([2,3,4,5,6]) # 48
```

### `mode`

This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.

```py
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
```

### `capitalize`

This function accepts a string and returns the same string with the first letter capitalized.

```py
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
```

### `compact`

This function accepts a list and returns a list of values that are truthy values.

```py
compact([0,1,2,"",[], false, {}, None, "All done"]) # [1,2, "All done"]
```

### `partition`

This function accepts a list and a callback function (which you can assume returns true or false). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is `true`, the element should go into one list if it's `false`, the element should go into another list. When it's finished, `partition` should return both lists inside of one larger list.

```py
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
```

### `intersection`

This function should accept a two dimensional list and return a list with the values that are the same in each list.

```py
intersection([1,2,3], [2,3,4]) # [2,3]
```

### `once`

This function accepts a function and returns a new function that can only be invoked once. If the function is invoked more than once, it should return `undefined`.

```py
def add(a,b):
    return a+b
}

var oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # undefined
oneAddition(12,200) # undefined
```
