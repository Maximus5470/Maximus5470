import pytest
from sq import sq

def testp():
    assert sq(2)==4
    assert sq(3)==9
def testn():
    assert sq(-2)==4
    assert sq(-3)==9