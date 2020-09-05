#Python3 implementation of the Maximum Product Subarray problem: find maximum product of a contiguous subarray in the array.

#My own original linear time algorithm - takes advantage of properties of integer multiplication (will not work if array includes floating point numbers -1 < x < 1)
#Faster than 100% of Python3 online submissions for Maximum product subarray on LeetCode, and uses less memory than 96% :)

def maxProduct(arr):
    if (len(arr) == 1):
        return arr[0]
    if 0 in arr:
        arr = splitByZero(arr) #if there are zeros in array, split into arrays without zeros (since multiplication by 0 = 0)
        products = []

        for array_split in arr:
            products.append(maxProductNoZeros(array_split)) #get all max products of arrays between the zeros

        products.append(0) #get the max of all products and zero (in case all products are negative)
        return(max(products))
    else:
        return maxProductNoZeros(arr)

def splitByZero(arr):
    ret = [] #2d array; elements of original array 'split' by 0 elements
    row = [] #array to hold current row during iteration; restarts when we hit a 0
    for elem in arr:
        if elem == 0:
            #elem = 0 -> append current row to 2d array and empty it
            if len(row) > 0:
                ret.append(row)
                row = []
        else:
            row.append(elem)
    if len(row) > 0:
        #can't forget the last row :)
        ret.append(row)
    return ret

def maxProductNoZeros(arr):
    if len(arr) ==1:
        return arr[0]

    #Count negative numbers in the array. If we have an even number of negatives, we can definitively return the product of the whole array
    #If we have an odd count of negative numbers, we need to drop either the first or last. So we can do both separately and see which one gives us a larger product.
    countNeg = 0

    for elem in arr:
        if elem < 0:
            countNeg += 1

    if (countNeg % 2) == 0:
        #return product of the whole array
        prod = 1
        for elem in arr:
            prod *= elem
        return prod

    elimFirstProd = 1 #product that comes from eliminating the first negative and everything before from the rest of the array
    i = 0
    while arr[i] > 0 and i < len(arr):
        i += 1
    while i < len(arr)-1:
        i += 1
        elimFirstProd *= arr[i]

    elimLastProd = 1 #product from eliminating the last negative and everything after from the rest of the array
    i = len(arr)-1
    while arr[i] > 0 and i >= 0:
        i -= 1
    while i > 0:
        i -= 1
        elimLastProd *= arr[i]

    return max(elimFirstProd, elimLastProd)

def test1():
    arr = [-2, 0, -4, 0, -8, 0, -1]
    print("Correct: 0")
    print("Solution: " + str(maxProduct(arr)))

def test2():
    arr = [-3, 5, 8, 10, 4, -2, 1]
    print("Correct: 9600")
    print("Solution: " + str(maxProduct(arr)))

def test3():
    arr = [-3, 5, 8, -4, 1, -3, 15]
    print("Correct: 7200")
    print("Solution: " + str(maxProduct(arr)))
def test4():
    arr = [2, 3, -2, 4]
    print("Correct: 6")
    print("Solution: " + str(maxProduct(arr)))
def test5():
    arr = [2, 0, 3, -2, 4 ,-2]
    print("Correct: 48")
    print("Solution: " + str(maxProduct(arr)))
def test6():
    arr = [-2, 0]
    print("Correct: 0")
    print("Solution: " + str(maxProduct(arr)))

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
main()




