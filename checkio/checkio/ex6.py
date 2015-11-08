def checkio(words):
    n = 0 
    for word in words.split():
        try:
            if int(word)>= 0:
                n = 0
        except ValueError:

            n = n + 1
            if n == 3:
                print ("True")
