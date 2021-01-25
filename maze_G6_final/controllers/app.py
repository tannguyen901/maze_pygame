from models.maze import Maze
from .welcome_controller import WelcomeController
from .game_controller import GameController
from .end_game_controller import EndGameController
from models.score_database_manager import DatabaseManager
import pygame

class App:
    """Initiates the game and allows it to keep running until the
    variable turns to false.
    """
    def __init__(self, filename, player):
        """Using the filename and players as args, starts the game
        as filename is the maze and the player is the player.

        Args:
            filename(str): The text file of the maze
            player(str): the player
        """
        self._contents = Maze(filename, player)
        self._welcome = WelcomeController(self._contents)
        self._endgame = EndGameController(self._contents.player.backpack, self._contents)


    def run(self):
        """Starts the welcome screen and the game_controller. Starts
        looping until the 'running' becomes false
        """
        model = self._contents
        model.create_random_items()
        self._welcome.run()
        game_controller = GameController(model)

        running = True

        while running:
            
            try:
                if game_controller._end_game:
                    self._endgame.run()
                    running = False
                else:
                    game_controller.run()

            except SystemExit as e:
                print(e)
                running = False
                continue
        pygame.quit()

        # write score
        score = int(game_controller.time_score)*2 + len(self._contents.player.backpack)*15
        print("Final score is:", score)  
        user_input = input("Enter your name to have your high score showed on our website:")
        scores_db = DatabaseManager("scores.db")
        if score >= 80 and user_input:
            scores_db.add(user_input, score)

