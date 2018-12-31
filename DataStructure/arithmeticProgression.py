from DataStructure.progression import Progression


class ArithmeticProgression(Progression):
    """
    Inherit from the progression class
    """
    def __init__(self, increment = 1, start = 0):
        super().__init__(start)
        self.increment = increment

    def advance(self):
        """
        This method overrides advance method in the super class
        :return:
        """
        self.current += self.increment

