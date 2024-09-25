"""
File: test_my_index.py
Initial developers: COMP 801 instructors
Developer: Nalin Yetukuri
Date: 9/24/2024
"""
from sentence import Sentence


def test_my_index_a_word():
    """
    a_word is a word that is present in the sentence.
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    a_word = "Use"
    expected = 0
    actual = sentence_object.my_index(a_word)
    assert actual == expected


def test_my_index_a_word_not_in_sentence():
    """
    a_word is a word that is not present in the test sentence. 
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    a_word = "U$e"
    expected = None
    actual = sentence_object.my_index(a_word)
    assert actual == expected


def test_my_index_case_sensitivity():
    """
    a_word is a word that is present in the sentence,
    but it is given with a different case
    """
    test_sentence = "Use this area for writing code or taking notes."
    sentence_object = Sentence(test_sentence)
    a_word = "use"  
    expected = None  
    actual = sentence_object.my_index(a_word)
    assert actual == expected
