def count_words(text):
    text = text.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")
    words = text.split(' ')
    length = len(words)-1
    dict = {}
    for word in words:
        try:
            dict[word] += 1
        except KeyError:
            dict[word] = 1
    print(dict)
    print( "총 단어 수:", length)


count_words(input("문장을 입력하세요: "))
