# coding=utf-8

# Input: array with multiple strings
# Expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

from collections import Counter

def rank_words(sentences):
    # All sentences transform into one string and convert to lowercase
    combined_text = ' '.join(sentences).lower()

    # Punctuation removal and split into words
    words = combined_text.replace('.', '').replace(',', '').split()

    # Counting the frequency of each word
    word_counts = Counter(words)

    # Getting the three most common words
    most_common_words = word_counts.most_common(3)

    # The results
    for i, (word, count) in enumerate(most_common_words, 1):
        print(f"{i}. \"{word}\" - {count}")

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

print(rank_words(sentences))
