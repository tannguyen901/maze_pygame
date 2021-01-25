import pytest
from models.maze import Maze
from models.score import Score

@pytest.fixture
def maze_object():
    """ This is a sample Maze object that is valid"""
    return Maze("tests/test1.txt", "P")

@pytest.fixture()
def good_score():
    """This is a sample of a valid score"""
    return Score('Good', 100)

@pytest.fixture()
def bad_score():
    """This is another sample of a valid score"""
    return Score('Bad',0)