def long_word(text):
    return len(text) > 7

print(long_word("Python"))
print(long_word("Magnificent"))

def first_longer_than_second(first_word, second_word):
    return len(first_word) > len(second_word)

print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("steven", "seagal"))

def same_letter_and_first_letter(word):
    return word[0] == word[-1]

print(same_letter_and_first_letter("runner"))
print(same_letter_and_first_letter("Runner"))
print(same_letter_and_first_letter("clock"))
print(same_letter_and_first_letter("q"))

def three_number_sum(number):
    return int(number[0]) + int(number[1]) +int(number[2])

print(three_number_sum("567"))
print(three_number_sum("123"))
print(three_number_sum("444"))


def first_three_characters(word):
    return word[:3]

print(first_three_characters("dynasty"))
print(first_three_characters("empire"))

def last_five_characters(word):
    return word[-5:]

print(last_five_characters("dynasty"))
print(last_five_characters("empire"))


def is_palindrome(word):
    return word[:] == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))