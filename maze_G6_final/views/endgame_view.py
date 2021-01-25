
from views.maze_view import MazeView


class EndGameView(MazeView):
    """ This class is to show the game over. It inherits from MazeView Class

    Attributes:
        _backpack (list): the list of items that play collect on the way
        supper that inherits from MazeView Class
    """
    def __init__(self, backpack:list, maze):
        """ Setup the private attribute for EndGamrView
        
        Args:
            backpack (list): the list of items that play collect on the way
            maze (obj): supper that inherits from MazeView Class
        """
        self._backpack = backpack
        super().__init__(maze)
    
    def say_goodbye(self):
        """ Template pattern: display end game text. Show the items in backpack
        
        Returns:
            str: a goodbye string and which gift of 4 items the player collected
        """
        self.display_maze()
        goodbye = "Thank you for playing with us.\n"
        show_backpack = f"You have {len(self._backpack)} in your backpack: {','.join(self._backpack)}"
        print(goodbye + show_backpack)
        
