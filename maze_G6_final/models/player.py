class Player:
    """ This class represents the player and backpack features which
    allows items collected by the player to be stored in a list
    """
    def __init__(self, player:str):
        """Initialized player and backpack to be used as a public
        variable.

        args:
            player(str): a string
        """
        self.player = player
        self.backpack = []

    def pickup_item(self, item):
        """ Appends the item retrieved by the player and appends it into
        the backpack. 
        
        Returns:
            backpack(list): updates the list.
        """
        self.backpack.append(item)
        return self.backpack
