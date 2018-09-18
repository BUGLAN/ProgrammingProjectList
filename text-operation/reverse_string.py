#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    text-operation.reverse_string
    -----------------------------

    反转字符串
    :copyright: (c) 2018-09-13 by buglan
"""
from typing import List


def reverse_string(string: str) -> str:
    return string[::-1]


def reverse_string2(string: str) -> str:
    """
    string is unmut type
    so cann't use string[i] = ...
    """
    length: int = len(string)
    strings: List[str] = list(string)
    for i in range(length // 2):
        strings[i], strings[length - i - 1] = strings[length - i -
                                                      1], strings[i]
    return "".join(strings)


def test_reverse_string():
    string = "abcde"
    assert "edcba" == reverse_string(string)


def test_reverse_string2():
    string = "abcde"
    assert "edcba" == reverse_string2(string)
