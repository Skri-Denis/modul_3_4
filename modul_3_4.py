def single_root_words (root_word, *other_words):
    same_words = []
    for i in other_words: # переменная i содержит параметр - other_words
        if (root_word.lower() in i.lower() # если root_word есть в other_word
                or i.lower() in root_word.lower()): # или other_word есть в root_word
            same_words.append(i) # добавить other_word в список
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
