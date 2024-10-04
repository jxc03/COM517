Introduction recap of Python programming covering beginner-to-intermediate level Python tasks. Working hrough a series of exercises that cover key Python skills such as loops, functions, data structures, and basic algorithms.

<h1 align="center">
    Week 1 - Python Tasks
</h1>

<p>
    Following tasks completed using Jupyter notebook.
</p>

**T1**<br>
Print 'Hello, World!'.

```python
print('Hello, World!')
```
```
Hello, World!
```

**T2**<br>
Create a list of numbers from 1 to 10 and print the list.

```python
numbers = list( range(1,11) ) 
print(numbers)
```
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**T3**<br>
Create a variable `x` with value 5, then print the square of `x`.

```python
x = 5
print(x ** 2)
```
```
25
```

**T4**<br>
Write a function `add_numbers(a, b)` that returns the sum of two numbers.

```python
def add_numbers(a, b):
    return a + b

print(add_numbers (5,4) )
```
```
9
```

**T5**<br>
Use a `for` loop to iterate through a list of names and print each name.

```python
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)
```
```
Alice
Bob
Charlie
```

**T6**<br>
Write a Python program to find the maximum number in a list of numbers [4, 7, 1, 12, 9].

```python
numbers = [4, 7, 1, 21, 9]
print(max (numbers) )
```
```
21
```

**T7**<br>
Use a `while` loop to print numbers from 1 to 5.

```python
n = 1
while n <= 5: 
    print(n)
    n += 1
```
```
1
2
3
4
5
```

**T8**<br>
Create a function that takes a list of numbers and returns the average of those numbers.

```python
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [15, 25, 35, 45]
print(average (numbers) )
```
```
30.0
```

**T9**<br>
Use a dictionary to store the ages of 3 people (e.g., John: 25, Jane: 30, James: 22) and print the dictionary.

```python
ages = {'John': 35, 'Jane': 40, 'James': 22}
print(ages)
```
```
{'John': 35, 'Jane': 40, 'James': 22}
```

**T10**<br>
Write a Python program to convert a temperature from Celsius to Fahrenheit. Use the formula: `F = C * 9/5 + 32`.

```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)
```
```
86.0
```

**T11**<br>
Write a function `is_even(n)` that returns `True` if a number is even, otherwise returns `False`.

```python
def is_even(n):
    return n % 2 == 00

print(is_even (9) )
print(is_even (2) )
```
```
False
True
```

**T12**<br>
Write a Python program to reverse a string.

```python
string = 'Hello'
reversed_string = string[::-1]
print(reversed_string)
```
```
olleH
```

**T13**<br>
Write a Python program that counts the occurrences of each character in a string.

```python
from collections import Counter

string = 'Hello'
count = Counter(string)
print(count)
```
```
Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
```

**T14**<br>
Write a function that adds all numbers from 1 to a given number.

```python
def add_numbers(n):
    result = 0
    for i in range (1, n + 1):
        result += i
    return result

print(add_numbers (3) )
```
```
6
```

**T15**<br>
Write a function that adds all numbers from 1 to a given number.

```python
def add_numbers(n):
    result = 0
    for i in range (1, n + 1):
        result += i
    return result

print(add_numbers (3) )
```
```
6
```

**T16**<br>
Write a Python program to check if a string is a palindrome (reads the same forward and backward).

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('hero'))
print(is_palindrome('madam'))
```
```
False
True
```

**T17**<br>
Write a Python program to count the number of vowels in a string.

```python
vowels = 'aeiou'
string = 'Hello, how are you'
vowel_count = sum(1 for char in string if char in vowels)
print(vowel_count)
```
```
7
```

**T18**<br>
Write a Python program to merge two dictionaries.

```python
dict1 = {'a': 2, 'b': 3}
dict2 = {'c': 4, 'd': 5}
merged_dict = {**dict1, **dict2}
print(merged_dict)
```
```
{'a': 2, 'b': 3, 'c': 4, 'd': 5}
```

**T19**<br>
Write a function count_even_numbers(n) that counts how many even numbers there are from 1 to n.

```python
def count_even_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    return count

print(count_even_numbers (24) )
```
```
12
```

**T20**<br>
Write a Python program to find the common elements between two sets.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1.intersection(set2)
print(common_elements)
```
```
{4, 5}
```

**T21**<br>
Write a function `is_prime(n)` that returns `True` if a number is prime, otherwise returns `False`.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    
print (is_prime (13) )
print (is_prime (6) )
```
```
True
False
```

**T22**<br>
Write a Python program to flatten a list of lists. E.g., `[[1, 2], [3, 4]]` becomes `[1, 2, 3, 4]`.

```python
list_of_lists = [ [1, 2], [3, 4] ]
flattened_list = [ item for sublist in list_of_lists for item in sublist]
print(flattened_list)
```
```
[1, 2, 3, 4]
```

**T23**<br>
Write a Python program to remove duplicates from a list.

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_numbers = list(set (numbers) )
print(unique_numbers)
```
```
[1, 2, 3, 4, 5, 6]
```

**T24**<br>
Write a Python program to check if two strings are anagrams of each other.

```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams ('listen', 'silent') )
print(are_anagrams ('hello', 'world') )
print(are_anagrams ('man', 'woman') )
```
```
True
False
False
```

**T25**<br>
Write a Python program to find the smallest number in a list.

```python
def find_smallest(numbers):
    return min(numbers)

numbers = [100, 9, 32, 15, 24, 2]

print(find_smallest (numbers) )
```
```
2
```

**T26**<br>
Write a Python program to remove all whitespace from a string.

```python
string = ' Hello        World         '
cleaned_string = string.replace(' ', "")
print(cleaned_string)
```
```
HelloWorld
```

**T26**<br>
Write a Python program to remove all whitespace from a string.

```python
string = ' Hello        World         '
cleaned_string = string.replace(' ', "")
print(cleaned_string)
```
```
HelloWorld
```

**T27**<br>
Write a Python program to find the second largest number in a list.

```python
numbers = [10, 20, 4, 45, 99]
unique_numbers = list(set (numbers) )
unique_numbers.sort()
print(unique_numbers[-2]) 
```
```
45
```

**T28**<br>
Write a Python program to find the length of the longest word in a sentence.

```python
sentence = 'I wonder what is the longest word'
longest_word = max(sentence.split(), key = len)
print(len (longest_word) )
```
```
7
```

**T29**<br>
Write a Python program to generate all the divisors of a given number.

```python
def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(divisors (32) )
```
```
[1, 2, 4, 8, 16, 32]
```

**T30**<br>
Write a Python program to calculate the area of a circle given its radius.

```python
import math
radius = 5
area = math.pi * (radius ** 2)
print(area) 
```
```
78.53981633974483
```

#Add explanation / breakdown of code to every tasks