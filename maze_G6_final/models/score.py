class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score

    def __str__(self):
        """ This dunder method is for printing instance. Return: string"""
        return f"Score: {self._name} ({self._score})"
    
    def __lt__(self, other_score):                      #! This is to help sorted() in score_manager 
        """ This dunder method is using for comparing score of an instance less than the other instance. 
        
        Arg: other object of Score class

        Raise: TypeError: the if the object is not in the class"""
        if type(other_score) is not type(self):
            raise TypeError("Unsupported type")
        return self._score < other_score._score
    
    def to_dict(self):
        """ This is the method to convert object to a dictionary. Returns: A dictionary represent our object """
        return {"name": self._name, "score": self._score}