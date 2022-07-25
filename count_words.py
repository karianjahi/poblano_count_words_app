"""
This module counts the no. of words in a sentence
"""


class WordCounter:
    """
    This is the class that contains the attributes
    and methods for word counting
    """

    def __init__(self, text):
        """
        Class constructor
        :param text: <str>  text is a string
        :return <None>
        """
        assert isinstance(text, str), "must be a string"
        self.text = text

    def __repr__(self):
        """
        Representative method
        """
        return f"Text to count: {self.text}"

    def count_words(self):
        """
        This is the method that actually counts the words
        :return: <int>
        """
        return len(self.text.split(" "))


if __name__ == "__main__":
    TEXT = "I am studying data science"
    INST = WordCounter(TEXT)
    print(INST.count_words())
