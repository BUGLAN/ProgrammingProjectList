#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    text-operation.plalindrome
    --------------------------

    判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”
    :copyright: (c) 2018-09-15 by buglan
"""
from typing import List, Optional, Any


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Stack:
    def __init__(self, maxcount: Optional[int] = None) -> None:
        self.items: List = []
        self.maxcount = maxcount
        if self.maxcount is not None and self.maxcount <= 0:
            raise Exception("self.maxcount cann't <= 0")

    def __len__(self) -> int:
        return len(self.items)

    def push(self, value: Any) -> None:
        if self.maxcount is not None and len(self) >= self.maxcount:
            raise FullError(f"len(self) >= {self.maxcount}")
        self.items.append(value)

    def pop(self) -> Any:
        if len(self) <= 0:
            raise EmptyError("len(self) <= 0")
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peak(self) -> Any:
        if len(self) <= 0:
            raise EmptyError("len(self) <= 0")
        return self.items[-1]


def is_plalindrome(string: str) -> bool:
    length: int = len(string)
    stack: 'Stack' = Stack(length // 2)
    for i in range(length // 2):
        stack.push(string[i])
    s: str = ""
    for i in range(length // 2):
        s += stack.pop()
    if len(string) // 2 == 0 and s == string[length // 2:]:
        return True
    elif s == string[length // 2 + 1:]:
        return True
    return False


def test_is_plalindrome():
    string = 'racecar'
    assert is_plalindrome(string)
    string = '妈妈爱我,我爱妈妈'
    assert is_plalindrome(string)
    string = 'aabb'
    assert not is_plalindrome(string)
    string = 'abba'
    assert not is_plalindrome(string)
