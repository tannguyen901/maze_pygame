from views.welcome_view import WelcomeView

class WelcomeController:
    """This class is used as a display the starting screen of the game
    """
    def __init__(self, maze):
        """Takes maze as an argument to assign a variable

        Args:
            maze: The maze
        """
        self._view = WelcomeView(maze)

    def run(self):
        """Displays the starting screen and output when starting the game

        """ 
        return self._view.display_welcome()

