import pytest
from app import summ


def test_add():
    assert summ(2, 3) == 5
    assert summ(-1, 1) == 0
