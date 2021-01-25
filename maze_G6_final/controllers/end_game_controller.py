from views.endgame_view import EndGameView

class EndGameController:
    """ This class is used to end the game when the player decides to
    quit
    """
    def __init__(self, backpack, maze):
        """Takes the backpack and maze as auguments to display the items
        that player had collected as well as the maze

        Args:
            backpack(list): A list that stores items
            maze(obj): A maze for the player traverse
        """
        self._maze = maze
        self._view= EndGameView(backpack, maze)
        
    def run(self):
        """Imports the function from EndGameView to display a goodbye
        message
        """
        return self._view.say_goodbye()

        
        
