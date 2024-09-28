"""
File: client.py
Initial developers: COMP 801 instructors
Developer:
Date:
"""
from sentence import Sentence


def main():
    """
    Check functionality of `Sentence` class.
    """
    s_obj = Sentence('just chekcing')
    s_obj.my_split()
    print(s_obj.sentence)
    print(s_obj.words)

    s_obj = Sentence('just chekcing')
    joined_words = s_obj.my_join()
    print(s_obj.sentence)
    print(s_obj.words)
    print(joined_words)

    s_obj = Sentence('just chekcing')
    a_word = "just"
    indexed_word = s_obj.my_index(a_word)
    print(s_obj.sentence)
    print(s_obj.words)
    print(indexed_word)


main()
