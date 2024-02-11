import sys


class TextWord:
    def __init__(self, filename):

        self.filename = filename

    def appropriate_words(self, word):

        mathing_words = []

        try:

            with open(self.filename, "r", encoding="ANSI") as file:
                for line in file:
                    words = line.split()
                    for w in words:
                        if len(w) == len(word) and w == word:
                            mathing_words.append(w)

        except IOError:
            print(f"Error reading file << {self.filename} >> not found. ")
            sys.exit(1)

        return mathing_words

    def word_count(self, word):
        mathing_words = self.appropriate_words(word)

        return len(mathing_words)

    def word_output(self, word):
        matching_words = self.appropriate_words(word)
        count = len(matching_words)
        print(
            f"Word < {word} > lengths < {len(word)} > occurs < {count} > time in the file < {self.filename} >:"
        )
        if count > 0:
            for match in matching_words:
                print(match)


def main():

    try:

        filename = input("Enther to path to the file: ")
        word = input("Enther earch words: ")

        counter = TextWord(filename)
        counter.word_output(word)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
