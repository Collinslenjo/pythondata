'''
List comprehensions are used for creating new list from another iterables.
'''

# normal function to get the square of a list
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
  squares.append(n**2)
print(squares) # Output: [1, 4, 9, 16]

# when redone in list comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares) # Output: [1, 4, 9, 16]

# example 2
# normal way to Find common numbers from two list using for loop.
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
  for b in list_b:
    if a == b:
      common_num.append(a)
print(common_num) # Output [2, 3, 4]

# list comprehension way of doing it
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]