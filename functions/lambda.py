'''
Lambda Functions
They can accept many arguments but only one expression
'''
# this is a normal function
 def add(x, y): 
    return x + y
# Call the function
add(2, 3) # Output: 5

# Redoing the function in the lambda way
add = lambda x,y : x + y
print add(2,3) # Output: 5

'''
Map Functions
'''
def multiply(x):
	return x * 2
map(multiply,[1,2,3,4]) # Output [2, 4, 6, 8]

'''Rewriting the above map function with lambda'''
map(lambda x:x*2, [1,2,3,4]) # Output [2, 4, 6, 8]

'''
Iterating over a dictionary using map and lambda
'''
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]
map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]

'''
Multiple iterables to the map function
'''
list_a = [1, 2, 3]
list_b = [10, 20, 30]
map(lambda x, y: x + y, list_a, list_b) # Output: [11, 22, 33]

# In Python3, map function returns an iterator or map object which gets lazily evaluated
map_output = map(lambda x: x*2, [1, 2, 3, 4])
print(map_output) # Output: map object: <map object at 0x04D6BAB0>
list_map_output = list(map_output)
print(list_map_output) # Output: [2, 4, 6, 8]


'''
Filter functions
'''
# Even number using filter function
a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

# Filter list of dicts
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
filter(lambda x : x['name'] == 'python', dict_a) # Output: [{'name': 'python', 'points': 10}]

'''
Similar to map, filter function in Python3 returns a filter object or the iterator which gets lazily evaluated. Neither we can access the elements of the filter object with index nor we can use len() to find the length of the filter object.
'''
list_a = [1, 2, 3, 4, 5]
filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>
even_num = list(filter_obj) # Converts the filer obj to a list
print(even_num) # Output: [2, 4