from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """ Version of collections.Sequence abstract base class."""

    @abstractmethod
    def __getitem__(self, j):
        """
        returns element at index j
        :param j:
        :return:
        """

    def contains(self, val):
        """
        :return True if val is found in the sequence
        """

        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """
        returns leftmost index at which val is found.
        raised valueError otherwise
        :return:
        """
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('Value not in sequence')

    def count(self, val):
        """
        returns the number of elements corresponding to the given value
        :param val:
        :return:
        """
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
