def checkio(*args):
    low_num = 1000
    high_num = -1000
    empty_list = len(args)
    if empty_list == 0:
        low_num = 0
        high_num = 0 
    for i in args:
        if i > high_num:
            high_num = i
        if i <= low_num:
            low_num= i
    
    print high_num - low_num
