from views.maze_view import MazeView


class WelcomeView(MazeView):
    """ This class is to welcome and maze structure at the beginning of the game. It inherits from MazeView Class

    Attributes:
        supper that inherits from MazeView Class"""
    def __init__(self, maze):
        """ Setup the attribute for Welcomeview
        
        Args:
            maze (obj): supper that inherits from MazeView Class
        """
        super().__init__(maze)

    def display_welcome(self):
        """ Template pattern: Welcome question text
        Returns:
            str: the question text to start the game
        """

        text = """
        Welcome Maze Runer!!! This is the game you are craving for.\n
        You can move to right ('d') /left ('a')/up ('w') /down ('x') 
        or enter 'q' to quit:
        """
        print(text)
        self.display_maze()

