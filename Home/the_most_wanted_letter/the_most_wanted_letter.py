def checkio(text):
    text = text.lower()
    letter_li = [i for i in text if i.isalpha()]

    letter_set = set(letter_li)

    max_frequency = max([letter_li.count(i) for i in letter_set])

    max_letter_set = [i for i in letter_set if letter_li.count(i) == max_frequency]

    max_letter_set.sort()

    print(max_letter_set)

    return max_letter_set[0]


print(checkio('Hello World'))
