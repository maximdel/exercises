import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    '(((())))',
    '()()()()()()',
    '(())()()',
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"String {string} matches parentheses"


@pytest.mark.parametrize('string', [
    '(((()))',
    ')()()()',
    ')))((()())',
    '((((()))',
])
def test_not_matching_parentheses(string):
    assert not matching_parentheses(string), f"String {string} does not match"