def checkio(array):
    # sum even-index elements and multiply by last index
    if len(array) >= 1:
        new_array = array[0::2]
        for i in range(len(new_array) + 1):
            n = sum(new_array)
            a = len(array) -1
        print n * array[a]
        
    else: 
        return 0

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__': 
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"

