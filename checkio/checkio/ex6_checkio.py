

def checkio(words):

            succ = 0

                for word in words.split():

                                succ = (succ + 1)*word.isalpha()

                                        if succ == 3: return True

                                            else: return False


