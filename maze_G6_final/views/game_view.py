import pygame
from views.maze_view import MazeView


class GameView(MazeView):
    """ This class is to show the maze structure during the game. It inherits from MazeView Class

    Attributes:
        supper that inherits from MazeView Class"""
    def __init__(self, maze):
        """ Setup the attribute for GameView
        
        Args:
            maze (obj): supper that inherits from MazeView Class
        """
        super().__init__(maze)
        self.end_game = False
        
    def display_maze_game(self):
        """ Template pattern: display maze structure during the game

        Returns:
        str: a maze show current structure of the maze during the game
        """
        self.display_maze()




        
