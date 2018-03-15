word_list = {}

for word in input().split():
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1

for word in word_list:
    print(word, word_list[word])
