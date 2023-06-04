# ¿Es un anagrama? #

def is_anagram(str_1, str_2):
    if str_1.lower() == str_2.lower():
        return False
    return sorted(str_1.lower()) == sorted(str_2.lower())
# SORTED: es un metodo de ordenamiento | solo string


print(is_anagram("123", "123"))
