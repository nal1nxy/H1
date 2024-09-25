"""
File: test_my_join.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
Date: 9/24/2024
"""
from sentence import Sentence


def test_my_join_irregular_spaces():
    """
    Test Sentence that has irregular number of spaces between words.
    """
    test_sentence = "This       is a     string      in multiple   lines"
    sentence_object = Sentence(test_sentence)
    expected = "This is a string in multiple lines"
    actual = sentence_object.my_join
    assert actual == expected


def test_my_join_special_characters():
    """
    Test Sentence that has special characters as separate words.
    """
    test_sentence = "This !$ @ str!ng in mu|tip|e l!nes"
    sentence_object = Sentence(test_sentence)
    expected = "This is a string in multiple lines"
    actual = sentence_object.my_join
    assert actual == expected
