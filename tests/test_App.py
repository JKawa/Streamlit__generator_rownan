import pytest
from App import *

def test_random_number():
    actual=random_number(1,9)
    assert isinstance(actual,int)

def test_random_symbol():
    actual =random_symbol()
    assert actual in ['+', '-']
    
def test_random_symbol_p():
    actual=random_symbol_p()
    assert actual in ['', '-']
    
def test_random_from_list():
    actual=random_from_list(["xyz"])
    assert actual=="xyz"