import pygame
import os

class MazeView:
    def __init__(self, maze):
        """ the images of the maze game are loaded here """
        self._maze = maze
        length_of_window = len(self._maze.maze[0])*32 + 150
        width_of_window = len(self._maze.maze)*32 + 200
        self._display_surf = pygame.display.set_mode((length_of_window,width_of_window), pygame.HWSURFACE)
        blue = (0, 0, 128)

        self._display_surf.fill(blue)

        self._block_img = pygame.image.load(os.path.join("images","block.png")).convert()
        theme_pics = pygame.image.load(os.path.join("images","theme.jpg")).convert()   #background
        self._theme_img = pygame.transform.scale(theme_pics, (32,32))

        player_img = pygame.image.load(os.path.join("images","player.png")).convert()
        self._player_img = pygame.transform.scale(player_img, (32,32))

        axe_img = pygame.image.load(os.path.join("images","axe.png")).convert()
        self._axe = pygame.transform.scale(axe_img, (32,32))

        bow_img = pygame.image.load(os.path.join("images","bow.png")).convert()
        self._bow = pygame.transform.scale(bow_img, (32,32))

        pickaxe_img = pygame.image.load(os.path.join("images","pickaxe.png")).convert()
        self._pickaxe = pygame.transform.scale(pickaxe_img, (32,32))

        shovel_img = pygame.image.load(os.path.join("images","shield.png")).convert()
        self._shovel  = pygame.transform.scale(shovel_img, (32,32))

        sword_img = pygame.image.load(os.path.join("images","sword.png")).convert()
        self._sword = pygame.transform.scale(sword_img, (32,32))

        exit_door = pygame.image.load(os.path.join("images","door.png")).convert()
        self._exit_door = pygame.transform.scale(exit_door, (32,32))
        self.end_game = False

        self._font = pygame.font.Font(None, 40)
        self._red = pygame.Color('red')
        self._clock = pygame.time.Clock()
        self._timer = 30  # Decrease this to count down.
        self._dt = 0  # Delta time (time since last tick).

    @property
    def counter(self):
        return int(self._timer)

    def display_maze(self):
        """ Template pattern: main text - show the maze structure
        Returns:
            str: the maze structure and everything inside it
        """
        text = "="*15 + "MAZE" + "="*15 + '\n'
        for row in self._maze.maze:
            line = ''
            for element in row:
                line += element 
            line += '\n'
            text += line
        self.image_to_pygame()
        self.timer()
        self.show_score()
        return text

    def get_position(self, x,y):
        return (x*32+64,y*32+64)

    def timer(self):
        """ used to display the timer on the pygame.
        """
        self._timer -= self._dt
        if self._timer <= 0:
            self.end_game = True

        x = len(self._maze.maze[0])*32 - 150
        y = len(self._maze.maze)*32 + 100
        # draws text on new surface
        txt = self._font.render(str(round(self._timer, 2)), True, self._red)
        #draws txt on pygame
        self._display_surf.blit(txt, (x+140, y+30))
        #displays screen

        img = self._font.render('Time remaining', True, self._red)
        self._display_surf.blit(img, (x, y))

        pygame.display.flip()
        
        self._dt = self._clock.tick(30) / 1000  # / 1000 to convert to seconds.

    def show_score(self, score= 0):
        if self.end_game == True:
            print("this is time: ", self._timer)

    def image_to_pygame(self):
        """ blits the images onto the corresponding elements on the maze.txt file."""
        pygame.event.pump()
        self._display_surf.fill((0,0,0))
        for y,row in enumerate(self._maze.maze):
            for x,element in enumerate(row):
                if element == 'x':
                    self._display_surf.blit(self._block_img, self.get_position(x,y))
                if element == ' ':
                    self._display_surf.blit(self._theme_img, self.get_position(x,y))
                if element == "P":
                    self._display_surf.blit(self._player_img, self.get_position(x,y))
                if element == "axe":
                    self._display_surf.blit(self._axe, self.get_position(x,y))
                if element == "bow":
                    self._display_surf.blit(self._bow, self.get_position(x,y))
                if element == "pickaxe":
                    self._display_surf.blit(self._pickaxe, self.get_position(x,y))
                if element == "shovel":
                    self._display_surf.blit(self._shovel, self.get_position(x,y))
                if element == "sword":
                    self._display_surf.blit(self._sword, self.get_position(x,y))
                if element == "E":
                    self._display_surf.blit(self._exit_door, self.get_position(x,y))
        pygame.display.update()
