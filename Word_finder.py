import itertools

def load_words(file_path):
    with open(file_path) as f:
        valid_words = set(word.strip().lower() for word in f)
    return valid_words

def find_words(letters, word_list, min_len=3, max_len=None):
    letters = letters.lower()
    found_words = set()

    if max_len is None:
        max_len = len(letters)

    for i in range(min_len, max_len+1):
        for perm in itertools.permutations(letters, i):
            word = ''.join(perm)
            if word in word_list:
                found_words.add(word)

    return sorted(found_words, key=lambda x: (-len(x), x))


if __name__ == "__main__":
    word_list = load_words("C:/Users/PC/Desktop/DSA/words_alpha.txt")
    letters = input("Enter letters: ")

    try:
        min_len = int(input("Enter minimum word length: "))
    except ValueError:
        print("Invalid input. Using default minimum length = 3.")
        min_len = 3

    try:
        max_len_input = input("Enter maximum word length (or press Enter to use all): ")
        max_len = int(max_len_input) if max_len_input else None
    except ValueError:
        print("Invalid input. Using maximum length = length of letters.")
        max_len = None

    results = find_words(letters, word_list, min_len, max_len)

    print(f"\nFound {len(results)} words (length between {min_len} and {max_len or len(letters)}): ")
    for word in results:
        print(word)