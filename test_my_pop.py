"""
File: test_my_pop.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
Date: 9/24/2024
"""
from sentence import Sentence


def test_my_pop_legal_index():
    """
    Test Sentence that returns the word at the index given.
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    index = 4
    expected_word = "writing"
    actual_word = sentence_object.my_pop(index)
    assert actual_word == expected_word


def test_my_pop_illegal_index():
    """
    Test that the method returns None at the illegal index given.
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    index = 11
    expected = None
    actual = sentence_object.my_pop(index)
    assert actual == expected
