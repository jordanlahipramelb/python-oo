import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Machine for generating random words from a dictionary file

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'"""

    def __init__(self, file_path):
        """Read dictionary and reports # items read."""

        # dictionary file path
        dict_file = open(file_path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parses each word in list of words."""

        return [word.strip() for word in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special class that extends from WordFinder. This class will parse blank lines and comments."""

    def parse(self, dict_file):
        return [
            word.strip()
            for word in dict_file
            if word.strip() and not word.startswith("#")
        ]
