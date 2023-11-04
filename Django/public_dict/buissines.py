def read_words():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    words3 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
        words3.append([word1, word2])
    print(words3)
    return words3


def write_words(word1: str, word2: str):
    with open("file.txt", "a") as file:
        file.write(word1 + "-" + word2 + "\n")