"""
File: test_my_split.py
Developer: Nalin Yetukuri
Date: 9/24/2024
"""

from sentence import Sentence


def test_my_split_multi_line():
    """
    Test Sentence that has multiple lines.
    """
    test_sentence = """This is a string
    in multiple lines"""
    sentence_object = Sentence(test_sentence)
    expected = ['This', 'is', 'a', 'string', 'in', 'multiple', 'lines']
    sentence_object.my_split()
    actual = sentence_object.words
    assert actual == expected


def test_my_split_chars():
    """
    Test sentence that has special characters with extra space in the end.
    """
    test_sentence = "special octets for 802.1Q?). "
    sentence_object = Sentence(test_sentence)
    expected = ['special', 'octets', 'for', '802.1Q?).']
    sentence_object.my_split()
    actual = sentence_object.words
    assert actual == expected
