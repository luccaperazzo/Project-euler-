import inflect
import re

def count(strings):
    non_symbol_count = 0

    for string in strings:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string.replace(' ', '').replace('-', ''))
        non_symbol_count += len(cleaned_string)

    return non_symbol_count



def convert(numbers):
    p = inflect.engine()
    words_list = [p.number_to_words(number) for number in numbers]
    return words_list

lista = []
for i in range(1,1001):
    lista.append(i)
words_list = convert(lista)
lol = count(words_list)
print(lol)
print(words_list)