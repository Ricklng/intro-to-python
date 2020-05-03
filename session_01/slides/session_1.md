# [fit] IHF: Code
## Python — Session 1

---

# [fit] What is programming?

---

# [fit] What is Python?

---

# [fit] What's it used for?

---

# [fit] Who uses it?

---

# Hello, World!

---

# Hello, World!

```python
print("Hello, World!")
```

---

# Text Editor

---

# [fit] repl.it

---

# Naming Python Files

```
what_the_script_does.py
```
---

# Naming Python Files

```
hello_world.py
number_guess.py
tic_tac_toe.py
calculate_totals.py
send_emails.py
```

---

# Naming Python Files

- Lowercase
- Underscore instead of spaces
- No punctuation

---

# Writing Python

- You are not writing an essay...

---

# Hello, world!
Code — hello.py:

```python
print("Hello, Saf")
```

To Run:

```
$ python hello.py
```

---

# Variables

---

# Variables

```python
<variable_name> = <value>
```

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Variables

- Any mix of letters, numbers and some special characters
- Must start with a letter
- Keep lowercase
- Use underscore where there are spaces

---

# Data Types

---

# Strings

---

# Strings

Characters surrounded by quotes

```python
name = "Alice"
address = "123 Station Road"
favourite_food = "Pizza"
```

---

# Escaping

---

# Escaping

```
\n = New line
\t = Tab
\" = Double Quote
```

---
# Escaping

```python
favourite_food = "Pizza from \"Dough N' Sauce\""
shopping_list = "Apples\nBread\nMilk\nEggs"
```

---

# [fit]Coding Time
## Section A

---

1. Write code that prints ‘Hello world’
2. Print the numbers 1 to 5 on a single line
3. Write a script where ‘Hello’ and ‘World’ are printed on two separate lines
4. Write a script that prints a list of names, tabbed on separate lines, e.g.

```bash
My List of Names:
    Alice
    Bob
    Charlie
```

---
# Integer

---

# Integer

A whole number

```python
age = 17
days_in_january = 31
bottles_sitting_on_the_wall = 99
```

----

# Float

----

# Float

A decimal number

```python
price = 12.99
percent = 34.57
pi = 3.1415
```

---

# Boolean

---

# Boolean

True or False

```python
has_paid = True
vip = False
```

---

# None

---

# None

Absence of a value

```python
last_film_seen = None
items_in_basket = None
```

---

# Numerical Operators

---

# Numerical Operators

| Operator | Action | Example |
| --- | --- | --- |
| + | Addition | `1 + 2` |
| - | Subtraction | `3 - 1` |
| * | Multiplication | `3 * 7` |
| / | Division | `9 / 3` |
| ** | Exponent | `4 ** 2` |
| % | Modulus (remainder) | `10 % 3` |

---

# Numerical Operators

```python
print(1 + 2)
print(5 - 3)
print(3 * 7)
print(49 / 7)
print(4 ** 2)
print(10 % 3)
```

---

# Numerical Operators

[.code-highlight: 1-2]
[.code-highlight: 3]
```python
x = 3
y = 6
area = x * y
```

---

# Concatenation

---

# Concatenation

[.code-highlight: 1-2]
[.code-highlight: 3]
[.code-highlight: 1,5]
[.code-highlight: 1-3,6]
```python
first_name = "Bob"
last_name = "Jones"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Order of Operations

---

# Order of Operations

| | | |
| --- |--- | --- |
| Highest | () | Brackets |
| | ** | Exponent |
| | * | Multiplication |
| | / | Division |
| | + | Addition |
| Lowest | - | Subtraction |

---

# Order of Operations

[.code-highlight: 1]
[.code-highlight: 3]
```python
sum = 4 + 5 * 2

correct_sum = (4 + 5) * 2
```

---

# [fit]Coding Time
## Section B

---

## Section B
1. Write code that prints the value of 2 + 2
2. Write code that prints the value of 5.7 subtracted from 3.4
3. Write code that prints the value of 8 multiplied by 7
4. Write code that prints the value of 144 divided by 12
5. Write code that prints the value of the remainder of 67 divided by 12
6. Write code that finds the value of 20 from `4 - 2 * 6 / 3 * 5`. Hint: you might need brackets

---

### Further Help

### go to sli.do #ihfcode