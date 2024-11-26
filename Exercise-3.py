def kesav(*args):
    test = max([len(x) for x in args])
    test1 = [y+[0]*(test-len(y))for y in args]
    #test3 = tuple(test1)
    zipped = zip (*test1)

    zippedlist = list(zipped)
    res =[(sum(z)/len(z)) for z in zippedlist]
    print(res)
kesav([1,2], [1,2,3], [1,2,3,4,5])    

