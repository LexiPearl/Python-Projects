#print integers 1-255
def printInts():
    for count in range (1, 256):
        print count
print(Ints)

#print odds 1-255
def printOdds():
    for count in range (1, 256):
        if count % 2 != 0:
            print count
odds()

#print ints & sum 0-255
def printSum():
    sum= 0
    for x in range (0, 256):
        sum = sum+ x
        print x, sum
        print "The number is", x, "The sum is", sum
printSum()

#interate & print array
def printarray(arr):
    for val in arr:
        print val
printarray([1,2,3,4,5])

#find and print max
def findmax(arr):
    print max(arr)
findmax([1,2,3,4,5])

#find and print max
def findmax(arr):
    max=arr[0]
    for x in range (0, len(arr)):
        if arr[x] >max:
        max=arr[x]
findmax([1,2,3,4,5])

#getandprintaverage
def getandprint(arr):
    print float(sum(arr))/len(arr)
getandprint([1,2,3,4,5.0])

#arraywithodds
def getarraywithoods():
    arr=[]
    for count in range (1,256,2):
        return arr
arraywithodds()

#squarethevalues
def squarethevalues(arr):
    for count in range(0,len(arr)):
        arr[count]= arr[count]*arr[count]
    return arr
print squarethevalues[1,2,3,4,5]

#greaterthany
def greaterthany(arr,y):
        newCount=0
        for count in arr:
            if count > y:
                newCount+=1
        print newCount
print greaterthany ([1,2,3,4,5],2)

#zerooutnegativenumbers
def zeroOut(arr):
    for idx, val in enumerate(arr):
        if val < 0:
            arr[idx]=0
    return arr
print zeroOut([-1, -2, -3, 4, 5])

#maxminaverage
def maxMinAve(arr):
    max=arr[0]
    min= arr[0]
    total= 0
    for val in arr:
        if max< val:
            max=val
        if min>val:
            min=val;
        total+=val
    print max, min, float(total)/len(arr)
maxMinAve([1,2,3,4,5])

#shiftarray
def shiftArr(arr):
    arr.pop(0)
    arr.append(0)
    return arr
print shiftArr[1,2,3,4,5]

#shiftarray
def shiftArr(arr):
    for idx, val in enumerate(arr):
        if idx < len(arr)-1:
        arr[idx]= arr[idx+1]
    arr[len(arr)-1]=0
    arr.append(0)
    return arr
print shiftArr[1,2,3,4,5]

#swapstring (for array negative values)
def swapstring(arr):
    for x in range (0, len(arr)):
        if arr[x]<0:
            arr[x]="Dojo"
    print arr
swapstring([-1, -2,-3,4,5])
