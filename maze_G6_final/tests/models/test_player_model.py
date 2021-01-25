import pytest
from models.player import Player
import pytest

@pytest.fixture
def john():
    """ This is a sample Player object that is valid"""
    return Player("John")

def test_constructor_player_name(john):
    """1001- Tests constructor name attribute"""
    assert john.player == 'John'

def test_constructor_backpack(john):
    """1002 - Tests constructor backpack attribute"""
    john.backpack = [1,2,3]
    assert john.backpack == [1,2,3]

def test_constructor_backpack_is_list(john):
    """1003 - Tests if constructor backpack is a list"""
    john.backpack == list()

def test_pickup_item(john):
    """2001 - Tests if items picked up gets appended to backpack"""
    john.backpack = ['shield', 'sword', 'hammer']
    john.pickup_item('sword')
    assert john.backpack == ['shield', 'sword', 'hammer', 'sword']