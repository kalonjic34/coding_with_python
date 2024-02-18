empty = []
active = [True]

favourite_numbers = [8, 24, 12, 34, 67]

colors = ["red", "green", "blue"]


def is_long(elements):
    return len(elements) > 5

print(is_long())

def first_and_last(strings):
    return strings[0]+ strings[-1]

print(first_and_last(strings=["a", "b", "c"]))
print(first_and_last(strings=["bob", "tom", "rob"]))
print(first_and_last(strings=["a"]))

def product_of_even_indices(numbers):
    return numbers[0] * numbers[2] * numbers[4]

print(product_of_even_indices(numbers=[1,2,3,4,5,6]))
print(product_of_even_indices(numbers=[3,4,3,5,3,6]))

def first_letter_of_last_string(string):
    return string[-1][0]

print(first_letter_of_last_string(string=["cat", "dog", "zebra"]))
print(first_letter_of_last_string(string=["nonsense"]))

def split_in_two(list, number):
    if number % 2 == 0:
        return list[2:]
    else:
        return list[0:2]
    
list=["a","b","c","d","e","f"]
print(split_in_two(list, 3))
print(split_in_two(list, 4))
print(split_in_two(list, 1))
print(split_in_two(list, 10))

def nested_extraction(elements, index):
    return elements[index][index]

elements = [[3,4,5], [7,8,9], [10,11,12]]
print(nested_extraction(elements, 0))
print(nested_extraction(elements, 1))
print(nested_extraction(elements, 2))

print()

def beginning_and_end(elements):
    return elements[0] == elements[-1]

print(beginning_and_end(elements=[1,2,3,4,1]))
print(beginning_and_end(elements=[1,2,3,4,5]))
print(beginning_and_end(elements=["a","b","a"]))
print(beginning_and_end(elements=[15]))

print()

def long_word_in_collection(elements,target):
    return target in elements and len(target) > 4

elements = ["cat", "dog", "rhino"]
print(long_word_in_collection(elements,"rhino"))
print(long_word_in_collection(elements,"cat"))
print(long_word_in_collection(elements,"monkey"))