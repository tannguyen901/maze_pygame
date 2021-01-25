import pytest
from models.maze import Maze
import pytest
from ..fixture import maze_object

def test_maze_constructor_opening_filename_contains_maze_template(maze_object):
    """1001 - Tests constructor of maze"""
    with open("tests/test1.txt",'r') as f:     #This run from root dir
        contents = f.read().split("\n")
        maze = [[_ for _ in line] for line in contents]

    assert maze_object.maze == maze

def test_maze_setter_changing_mazes(maze_object):
    """1002 - Tests constructor player if equal to 'P'"""
    maze_object = Maze("tests/test2.txt", "P")
    with open("tests/test2.txt",'r') as f:
        contents = f.read().split("\n")
        maze = [[_ for _ in line] for line in contents]
    maze_object.maze = maze
    assert maze_object.maze == maze

def test_constructor_player(maze_object):
    """2001 - Tests whether maze setter can change mazes"""
    assert maze_object.player.player == "P"

def test_check_vacancy_if_vacant_return_false(maze_object):
    """3001- Test If location is not vacant on map, return False"""
    assert False == maze_object.check_vacancy_or_exit(0,0)

def test_check_vacancy_if_vacant_return_true(maze_object):
    """3002- If location is vacant on map, return True"""
    assert True == maze_object.check_vacancy_or_exit(2,1)

def test_check_vacancy_if_exitdoor_return_true(maze_object):
    """3003- If the exit door just open when user collect at least 3 items, return True"""
    maze_object.player.backpack = ['A','B','C']
    assert True == maze_object.check_vacancy_or_exit(2,35)

def test_check_vacancy_if_exitdoor_return_false(maze_object):
    """3003- If the exit door just open when user collect at least 3 items, return False"""
    maze_object.player.backpack = ['A','B']
    assert False == maze_object.check_vacancy_or_exit(2,35)

def test_find_4_random_spots_are_empty(maze_object):
    """4001 - If random spots are empty, return True"""
    random_spots = maze_object.find_random_spot()
    for element in random_spots:
        assert True == maze_object.check_vacancy_or_exit(element[0], element[1])
    
def test_create_random_items(maze_object):
    """5001 - Test to see if random items are generated"""
    maze_object.create_random_items()

def test_find_player_idx(maze_object):
    """"6001 -Tests to find player index is on map"""
    maze_object.find_player_idx() == [1,1]

def test_find_player_runtime_error():
    """60002- Tests to see if player index can be found, raises Runtime Error when cannot"""
    maze_object = Maze("tests/test3.txt", "P")
    with pytest.raises(RuntimeError):
        maze_object.find_player_idx()

def test_check_item_if_item_in_backpack(maze_object):
    """7001- Test if a thing collected in the backpack is a gift item"""
    [item_a] = maze_object.check_item(3,1)
    assert item_a not in [' ','P','E','x']

def test_is_exit(maze_object):
    """8001- Test if player reach exit door, return True"""
    assert maze_object.is_exit(2,35) == True

def test_not_is_exit(maze_object):
    """8002 - Test if player does not reach exit door, return False"""
    assert maze_object.is_exit(2,34) == False

