import pytest
from app import summ


def test_summ():
    assert summ(2, 3) == 5
    assert summ(-1, 1) == 0
