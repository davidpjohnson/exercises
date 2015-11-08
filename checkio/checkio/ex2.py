from termcolor import colored, cprint
def index_power(array, n):

#Find Nth power of the element with index N.
    if 0<= len(array) <= 100 and n <= len(array):
        return array[n] ** n
        return None
        print "%d ** %d = %d"  % (array[n], n, array[n] ** n)
        print array[n] ** n 
    elif n >= len(array):
            print "-1"
    else:
        cprint ("\n\nTEST FAILED\n\n", 'red')
if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

