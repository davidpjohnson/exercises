def find_message(text):
    message = str() 
    for i in text:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
           #print i
            message = str(message) + "%s" % i
    print "%s" % message

