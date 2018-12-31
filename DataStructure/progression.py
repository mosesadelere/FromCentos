class Progression:
    """
    This will produce a generic progression.
    """
    def __init__(self, start=0):
        # initialize the current state of the first value
        self.current = start

    def advance(self):
        """
        Updating the current value to a new value.
        If current value is set to None, finite progression ends.
        :return:
        """
        self.current += 1

    def __next__(self):
        """
        Return the next element, or raised StopIteration error
        :return: Answer
        """
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current #records current value toreturn
            self.advance()
            return answer

    def __iter__(self):
        """This returns itself by convention"""
        return self

    def printProgression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))