def cointoss():
    ups = 0
    downs = 0
    for var in range(1, 5001):
        import random
        random_num = round(random.random())
        if random_num == 0:
            headtail = "It's a head!"
            ups = ups + 1
        else: 
            headtail= "It's a tail!"
            downs= downs + 1
        print "Attempt #", var,":", "Throwing a coin...", headtail, "Got", ups, "head(s) so far and", downs, "tail(s) so far"
    print "Ending the program, thank you!"
cointoss()


# import random
# import math
#
# print 'Starting the program'
#
# head_count = 0
# tail_count = 0
# for i in range(1,5001):
#     rand = round(random.random())
#     if rand == 0:
#         face = 'tail'
#         tail_count += 1
#     else:
#         face = 'head'
#         head_count += 1
#     print "Attempt #"+str(i)+": Throwing a coin...It's a "+face+"!...Got "+str(head_count)+" head(s) and "+str(tail_count)+" tail(s) so far"
#
# print 'Ending the program, thank you!'
