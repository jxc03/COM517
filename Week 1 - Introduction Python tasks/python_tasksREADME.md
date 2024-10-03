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