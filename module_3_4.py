def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word = root_word.lower()

    # Пустой список для хранения подходящих слов
    same_words = []

    # Проходим по каждому слову в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Если корневое слово содержится в слове или наоборот
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


# Примеры вызовов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на консоль
print(result1) 
print(result2)