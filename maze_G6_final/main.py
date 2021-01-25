from controllers.app import App
import pygame

if __name__ == "__main__":
    pygame.init()
    app = App('maze3.txt','P')
    app.run()