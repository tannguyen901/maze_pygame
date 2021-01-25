import random
from .player import Player
import pygame

class Maze:
    """This class is used to read the maze textfile and create it into a maze.
    IT is also used to create the items needed for the player to collect
    as well as placing them in a random location in the maze. Additionally,
    this class is used to check and indicate whether the player is able to exit
    and beat the game when they have all five items in their backpack.
    
    Attributes:
            _maze(nested list): The maze structure
            player(str): The player
    """
    def __init__(self, filename, player):
        """Uses filename and player as an arguement. Filename is used to
        read and create the maze. The player variable to is assigned.

        Args:
            filename(str): The maze as a textfile
            player(str): The player
        """
        with open(filename,'r') as f:
            contents = f.read().split("\n")
            self._maze = [[_ for _ in line] for line in contents]

        self.player = Player(player)

    @property
    def maze(self):
        """Getter for the private attribute maze. Returns: a nested list (the maze)"""
        return self._maze

    @maze.setter
    def maze(self, new_maze):
        """Setter for maze property and create public view to allow user change to various maze structures.
        Return: A Nested List - A new maze structure if user choose diff maze text files input"""
        self._maze = new_maze
    
    def check_vacancy_or_exit(self, row_num, col_num):
        """ This method to check if the position in the nested list with correspoding row index and column index.
        
        Args:
            row_number (int): the row index of a position
            col_num (int): the column index of a position

        Return: Boolean: True if the tested position is a space ' ', otherwise return Fasle
        """
        if self._maze[row_num][col_num] in {' '}:
            return True
        elif self._maze[row_num][col_num] in {'E'} and len(self.player.backpack) >= 3:
            return True
        else:
            return False

    def find_random_spot(self):
        """This method is to find 4 random spots in the nest list
        Returns: a tuple nested in a list [(x1,y1)(x2,y2),(x3,y3),(x4,y4)]
        """
        empty_spaces = []
        for i,line in enumerate(self._maze):
            for j, element in enumerate(line):
                """This nested For loop run and take element position
                which is an empty space in the nested list to put into an empty list 
                with form of each position index is a tuple (x,y)
                """
                if element == ' ':
                    empty_spaces.append(tuple([i,j]))
        gift_items = random.sample(empty_spaces, k = 5) #choose random 5 tuples in the list of empty spaces
        return gift_items
    
    def create_random_items(self):
        """This method is to put 4 gift objects/items into the maze with their random positions are stored in the tuple list
        created using find_random_spot method in the Maze class.
        """
        items = ['axe','bow','pickaxe','shovel','sword']
        for item in self.find_random_spot():
            row_idx = item[0]
            col_idx = item[1]
            self._maze[row_idx][col_idx] = items.pop()
    
        return self._maze

    def find_player_idx(self):
        """This method is to find the player index
        Return: A tuple nested in a list [(row_index,column_index)]"""
        for x, row in enumerate(self._maze):
            for y, col in enumerate(row):
                if row[y] == self.player.player:
                    return [x, y]
        raise RuntimeError("Find a better error...  but cannot find player index")

    def check_item(self, row_num, col_num):
        """Using row_num and col_num as arguemnts, checks if the player
        is touching the item. If the item is touch the player, the player
        will pick up the item.

        Args:
            row_num(int): The x-coordinate
            col_num(int): The y-coordinate
        Return:
            backpack(list): Stores items

        """
        if self._maze[row_num][col_num] not in [' ','P','E','x']:
            p_idx = self.find_player_idx()
            [pr_idx, pc_idx] =p_idx
            self._maze[pr_idx][pc_idx] =' '
            self.player.pickup_item(self._maze[row_num][col_num])
            self._maze[row_num][col_num] = 'P'
        return self.player.backpack
    
    def is_exit(self, row_num, col_num):
        """Using row_num and col_num as arguments, if the coordinates
        are equal to 'E' in the maze then return True. Otherwise, return
        False.

        Args:
            row_num(int): The x-coordinate
            col_num(int): The y-coordinate

        Return:
            if equal to 'E': True
            if not: False
        """
        if self._maze[row_num][col_num] == 'E':
            return True
        else:
            return False
    

    


