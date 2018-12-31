from DataStructure.progression import Progression


class GeometricProgression(Progression):

    def __init__(self, base = 2, start = 1):
        """
        Creates a new geometric progression
        :param base: fixed constant multiplied to each term
        :param start: first term of the progression
        """
        super().__init__(start)
        self.base = base

    def advance(self):
        """
        Method override super class
        :return:
        """
        self.current *= self.base