# def even_or_odd(number):
#     if number % 2 == 0:
#         return "even"
#     return "odd"

# print(even_or_odd(2))
# print(even_or_odd(0))
# print(even_or_odd(13))
# print(even_or_odd(9))

# print()

# def truthy_or_falsy(value):
#     if bool(value):
#         return f"The value {value} is truthy"
#     return f"The value {value} is falsy"

# print(truthy_or_falsy(0))
# print(truthy_or_falsy(5))
# print(truthy_or_falsy("Hello"))
# print(truthy_or_falsy(""))

# def negative_energy(number):
#     if number > 0:
#         return number
#     elif number < 0:
#         return -1 * number
#     else:
#         return number
    
# print(negative_energy(5))
# print(negative_energy(10))
# print(negative_energy(-5))
# print(negative_energy(-8))
# print(negative_energy(0))

def divisable_by_three_and_four(number):
    if number % 3 == 0 and number % 4 ==0:
        return True
    return False

    
print(divisable_by_three_and_four(3))
print(divisable_by_three_and_four(4))
print(divisable_by_three_and_four(12))
print(divisable_by_three_and_four(18))
print(divisable_by_three_and_four(24))

print()

def string_theory(word):
    if len(word) > 3 and word[0] == "S":
        return True
    else: False


print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))