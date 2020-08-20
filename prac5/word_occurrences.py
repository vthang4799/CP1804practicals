def main():
    count_word = {}
    input_text = input("Text: ")
    words = input_text.split()
    for word in words:
        frequency = count_word.get(word, 0)
        count_word[word] = frequency + 1
    words = list(count_word.keys())
    words.sort()
    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, count_word[word]))


if __name__ == '__main__':
    main()