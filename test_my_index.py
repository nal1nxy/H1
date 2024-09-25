"""
File: test_my_index.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
Date: 9/24/2024
"""
from sentence import Sentence


def test_my_index_a_word():
    """
    Test Sentence that has irregular number of spaces between words.
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    a_word = "Use"
    expected = 0
    actual = sentence_object.my_index(a_word)
    assert actual == expected


def test_my_index_a_word_not_in_sentence():
    """
    Test Sentence that has irregular number of spaces between words.
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    a_word = "U$e"
    expected = None
    actual = sentence_object.my_index(a_word)
    assert actual == expected
