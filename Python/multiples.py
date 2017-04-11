#printOdds
def printOdds():
    for count in range (1, 1000):
        if count % 2 != 0:
            print count
printOdds()

#printMultiples
def printMultiples():
    for count in range (5, 1000005):
        if count % 5 == 0:
            print count
printMultiples()
