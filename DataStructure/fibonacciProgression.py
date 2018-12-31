from DataStructure.progression import Progression


class FibonacciProgression(Progression):

    def __init__(self, first = 0, second = 1):
        """
        Fibonacci progression
        :param first: first term with default value of 0
        :param second: second term with default value of 1
        """
        super().__init__(first)
        self.prev = second - first

    def advance(self):
        self.prev, self.current = self.current, self.prev + self.current