#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    text-operation.count_vowel
    --------------------------

    统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
    :copyright: (c) 2018-09-15 by buglan
"""
keys = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def count_vowel(string: str) -> dict:
    for s in string:
        if s in keys:
            keys[s] += 1
    return keys


def test_count_vowel():
    string = 'aeiiousdfsdfsdf'
    assert count_vowel(string) == {'a': 1, 'e': 1, 'i': 2, 'o': 1, 'u': 1}
