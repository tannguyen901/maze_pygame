from views.game_view import GameView
import pygame
from pygame.locals import K_RIGHT,K_LEFT,K_UP,K_DOWN,K_q

class GameController:
    """Checks and updates the user inputs from the keyboard and game.
    """
    def __init__(self, maze):
        """Takes maze as an argument and changes the end_game to false
        which indicates that the game is running while printing 'exit game
        controller'

        Args:
            Maze(Obj): A layout of the maze
        """
        self._maze = maze
        self._view = GameView(self._maze)
        self._end_game = False

    @property
    def end_game(self):
        return self._end_game

    @property
    def time_score(self):
        return self._view.counter

    def get_user_input(self):
        """ ALL IT DOES IS RETURN WAXDq"""
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if (keys[K_RIGHT]):
            return "d"

        if (keys[K_LEFT]):
            return "a"

        if (keys[K_UP]):
            return "w"

        if (keys[K_DOWN]):
            return "x"

        if (keys[K_q]):
            return "q"


    def run(self):
        """Uses a loop to check for player input. When a player inputs a 
        working command, the game will check if the player has landed on
        a empty space. If the space is empty, the player will move to that
        space. If the player ever presses 'q', the loop will immediately end
        and the game will end.

        """
        # allow user to hold the keys
        pygame.key.set_repeat(200,200)

        p_idx = self._maze.find_player_idx()

        [row_idx, col_idx] = p_idx
        # user_input = input("Wa123nna go to right ('d') /left ('a')/up ('w') /down ('x'): or 'q' to quit:")
        user_input= self.get_user_input()
        # while (user_input != 'q') and not self._maze.is_exit(row_idx,col_idx+1):
        while (user_input != 'q') and self._end_game != True and self._view.counter > 0:
            self.game_has_ended()   # check if the game has ended yet or not
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self._end_game = True
                self.check_user_input(user_input, row_idx, col_idx)
            if self._end_game == True:
                break

            # pygame.time.delay(500)

            self._view.display_maze_game()
            self._end_game = self._view.end_game

            p_idx = self._maze.find_player_idx()
            [row_idx, col_idx] = p_idx
            user_input= self.get_user_input()
            # user_input = input("Wan123na go to right ('d') /left ('a')/up ('w') /down ('x'): or 'q' to quit:")

        if user_input == 'q'  or self._view.counter <= 0:
            self._end_game = True

        # if self._maze.is_exit(row_idx,col_idx+1):
        #     self._maze.maze[row_idx][col_idx] = ' '
        #     self._maze.maze[row_idx][col_idx+1] = 'P'
        #     self._end_game = True
        
        self.game_has_ended()
        return p_idx 

    def check_user_input(self, user_input, row_idx, col_idx):
        """Takes the arguments user_input, row_idx, col_idx to control
        the input of the player.

        Args:
            user_input(str): The player's movement by pressing arrow keys that return to 'd', 'a', 'w', or 'x'
            row_idx(int): The current row of the player
            col_idx(int) the current column of the player
        """
        if user_input == 'd':
            if self._maze.check_vacancy_or_exit(row_idx,col_idx+1):
                self._maze.maze[row_idx][col_idx] = ' '
                self._maze.maze[row_idx][col_idx+1] = 'P'
            self._maze.check_item(row_idx, col_idx+1)
        elif user_input == 'a':
            if self._maze.check_vacancy_or_exit(row_idx,col_idx-1):
                self._maze.maze[row_idx][col_idx] = ' '
                self._maze.maze[row_idx][col_idx-1] = 'P'
            self._maze.check_item(row_idx, col_idx-1)
        elif user_input == 'w':
            if self._maze.check_vacancy_or_exit(row_idx-1,col_idx):
                self._maze.maze[row_idx][col_idx] = ' '
                self._maze.maze[row_idx-1][col_idx] = 'P'
            self._maze.check_item(row_idx-1, col_idx)
        elif user_input == 'x':
            if self._maze.check_vacancy_or_exit(row_idx+1,col_idx):
                self._maze.maze[row_idx][col_idx] = ' '
                self._maze.maze[row_idx+1][col_idx] = 'P'
            self._maze.check_item(row_idx+1, col_idx)

    def game_has_ended(self):
        """Checks game if 'E' exists still, if no 'E' end game"""
        no_e_remains = True
        for row in self._maze.maze:
            for element in row:
                if element == "E":
                    no_e_remains = False

        if no_e_remains:
            self._end_game = True