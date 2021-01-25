import pytest
from models.score import Score
from ..fixture import good_score, bad_score

def test_init_invalid_name_score():
    """ 1001- Test if type of score name is a valid- a string"""
    with pytest.raises(ValueError):
        Score(100,55)
    with pytest.raises(ValueError):
        Score('',55)
    with pytest.raises(ValueError):
        Score('valid','55')

def test_str(good_score):
    """ 2001- Test if dunder __str__ method works"""
    assert str(good_score) == "Score: Good (100)"
    # assert print(good_score) == "Score: Good (100)"

def test_invalid_score_lt(good_score):
    """ 3001- Test if dunder __lt__ receiver an instance of the Class """
    with pytest.raises(TypeError):
        good_score < 1001

def test_lt(good_score,bad_score):
    """ 3002- Test if dunder __lt__ compare 2 instances of the Class properly"""
    assert bad_score < good_score 
    assert not good_score < bad_score

def test_to_dict(good_score):
    """ 4001- Test to_dict() method if it return a dict from of the score"""
    assert good_score.to_dict() == {"name": "Good", "score": 100}



