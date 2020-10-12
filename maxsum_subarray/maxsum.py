import math

#Python3 implementation of Maximum Sum Subarray problem: find maximum sum of a subarray in a given array
#Includes optimal Kadane's algorithm solution, as well as suboptimal (O(nlogn)) and optimal (O(n)) divide and conquer solutions.



#O(n) implementation of maximum sum subarray using Kadane's algorithm (Dynamic programming)
#Keeps track of max in the 'current' subarray (local max). 
#'Restarts' the local subarray if the new element is larger than the current local max sum 
def maxSub_Kadanes(array):
    local_max = array[0]
    global_max = array[0]

    for i in range(1, len(array)):
        local_max = max(array[i], array[i] + local_max) #if array[i] is chosen, we have in effect 'restarted' the current subarray
        if local_max > global_max:
            global_max = local_max

    return global_max


#O(nlogn) implementation of maximum subarray using divide and conquer approach
#Splits array into left and right subarrays and solves
#Then uses O(n) iterative approach to find maximum crossing subarray sum and combines

def maxSub_DC_slow(array):

    #base case - array len 1
    if len(array) == 1:
        return array[0]

    #divide into 2 halves and solve each recursively
    mid = math.floor(len(array)/2)
    L = array[:mid]
    R = array[mid:]

    leftMaxSum = maxSub_DC_slow(L)
    rightMaxSum = maxSub_DC_slow(R)
    crossMaxSum = maxCrossSum(L, R)

    #return solution
    return max(leftMaxSum, rightMaxSum, crossMaxSum)

#O(n) iterative crossing sum calculation
def maxCrossSum(L, R):

    #find max subarray from the right of the left subarray
    leftMaxSum = float('-inf')
    leftSum = 0
    
    for num in reversed(L):
        leftSum += num
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum
    

    #find max subarray from the left of the right subarray
    rightMaxSum = float('-inf')
    rightSum = 0
    
    for num in R:
        rightSum += num
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
    
    return rightMaxSum + leftMaxSum




#O(n) implementation of maximum subarray using divide and conquer aproach
#Recursive function returns extra information (total array sum, max prefix, max suffix) to allow for computation of the cross sum in constant time

def maxSub_DC_fast(array):
    return maxSub_DC_fast_helper(array)[0]

def maxSub_DC_fast_helper(array):
    #base case - array length 1
    if len(array) == 1:
        return array[0], array[0], array[0], array[0] #maxsum, totalsum, maxprefix, maxsuffix all = the value of the one element

    #divide into two subarrays and solve
    mid = math.floor(len(array)/2)
    L = array[:mid]
    R = array[mid:]
    LmaxSum, LtotalSum, LmaxPrefix, LmaxSuffix = maxSub_DC_fast_helper(L)
    RmaxSum, RtotalSum, RmaxPrefix, RmaxSuffix = maxSub_DC_fast_helper(R)

    #combine step - use extra information from both halves to compute all values for the combined array
    maxSum = max(LmaxSum, RmaxSum, LmaxSuffix + RmaxPrefix) #computation of cross array sum reduced to one addition due to extra information
    totalSum = LtotalSum + RtotalSum #total sum is easy to compute from left and right subarrays. Useful when computing maxprefix and maxsuffix
    maxPrefix = max(LmaxPrefix, LtotalSum + RmaxPrefix) #max prefix (max subarray sum starting from the left) is either the max prefix of the left subarray, or the total sum of the left subarray + max prefix of the right subarray
    maxSuffix = max(RmaxSuffix, RtotalSum + LmaxSuffix) #max suffix (max subarray sum starting from the right) is either the max suffix of the right subarray, or the total sum of the right subarray + max suffix of the left subarray

    return maxSum, totalSum, maxPrefix, maxSuffix


#Some test cases of different arrays. I tested these on LeetCode as well.

def test1():
    array = [-1, 5, 8, -12, 3, 4, -10, 4, 4, -6,-2, -8, 1]
    print("Correct = 13")
    print("Kadane's algorithm: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()


def test2():
    array = [-1, -1, -1, -2, -1]
    print("Correct = -1")
    print("Kadane's algorithm: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()

def test3():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Correct = " + str(int(8 * 9 / 2)))
    print("Kadane's algorithm: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()


def test4():
    array = [-8, -10, 1, -4]
    print("Correct = 1")
    print("Kadane's algorithm: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()

def test5():
    array = [-1]
    print("Correct = -1")
    print("Kadane's algorithm: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()

def test6():
    array = [54, -100, 12, 18, -44, 37, -500, 200, 42, 3, -100, -1000, 220]
    print("Correct = 245")
    print("Kadane's implementation: " + str(maxSub_Kadanes(array)))
    print("Divide and Conquer (slow): " + str(maxSub_DC_slow(array)))
    print("Divide and Conquer (fast): " + str(maxSub_DC_fast(array)))
    print()

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

main()
