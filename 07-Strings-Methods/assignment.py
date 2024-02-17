def vowel_count(word):
    return word.count("a") + word.count("e") +word.count("i") +word.count("o")+word.count("u")

print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))

def find_my_letter(word, char):
    return word.find(char)

print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))

def fancy_cleanup(word):
    return word.strip().replace("g","z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey     "))
print(fancy_cleanup("       nonsence    "))
print(fancy_cleanup("grade"))