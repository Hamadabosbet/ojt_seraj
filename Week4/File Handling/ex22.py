from collections import Counter
import re


def get_most_frequent_words(text, num_words):
    text = re.sub(r'[!?"\'.,;:()\[\]*]', '', text)
    words = text.upper().split()

    word_counts = Counter(words)
    most_common_words = word_counts.most_common(num_words)

    return most_common_words

if __name__ == "__main__":
    with open("2701-0.txt", 'r',encoding='utf-8') as file:
        moby_dick = file.read()
    most_frequent_words = get_most_frequent_words(moby_dick, 100)

    for rank, (word, count) in enumerate(most_frequent_words, start=1):

        print(f"{rank}. {word}: {count} ")