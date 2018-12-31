from DataStructure.arithmeticProgression import ArithmeticProgression
from DataStructure.fibonacciProgression import FibonacciProgression
from DataStructure.geometricProgression import GeometricProgression
from DataStructure.progression import Progression

if __name__ == '__main__':
    print('Default Progression')
    Progression().printProgression(10)
    print('-----------------------------------------------------')

    print('Arithmetic Progression with incremet of 5 --> ')
    ArithmeticProgression(5).printProgression(10)
    print('-----------------------------------------------------')

    print('Arithmethic Progression with start 2 and increment 5 --> ')
    ArithmeticProgression(5,2).printProgression(10)
    print('-----------------------------------------------------')

    print('Geometric Progression with default base --> ')
    GeometricProgression().printProgression(10)
    print('-----------------------------------------------------')

    print('Geometric Progression with base 3 --> ')
    GeometricProgression(3).printProgression(10)
    print('-----------------------------------------------------')

    print('Fibonacci Progression with default start value --> ')
    FibonacciProgression().printProgression(10)
    print('------------------------------------------------------')

    print('Geometric Progression with start values 4 and 6 --> ')
    FibonacciProgression(4,6).printProgression(10)



