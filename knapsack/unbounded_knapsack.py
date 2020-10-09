#Problem: Given a total weigh capacity of a knapsack, and weight/value pairs of items available, output the maximum possible value of items that can be fit in the knapsack


def knapsack_topdown(items, max_capacity):
    # represent max possible value for each capacity less than max capacity, including 0
    dp = [-1 for _ in range(max_capacity+1)]
    
    def calc_opt(cur_capacity): #cur_capacity is the how much weight is left in the knapsack
        #base case - current capacity is 0
        if cur_capacity == 0:
            dp[cur_capacity] = 0
        else:
            #get value that comes from picking each choice of item
            opt_val = 0
            for item_index in range(len(items)):
                if cur_capacity - items[item_index][0] >= 0: #if current item can fit
                    if dp[cur_capacity - items[item_index][0]] == -1: #if subproblem we will use to calculate opt value of choosing this item has not been calculated yet, calculate it recursively 
                        calc_opt(cur_capacity - items[item_index][0])
                    item_val = dp[cur_capacity - items[item_index][0]] + items[item_index][1] #opt value possible when choosing this item with the current capacity left in the knapsack
                    opt_val = max(item_val, opt_val)
                #if item didn't fit ignore it
            #if no items fit then opt val was just 0
            dp[cur_capacity] = opt_val

    calc_opt(max_capacity)
    #print(dp)
    return dp[max_capacity]

def knapsack_bottomup(items, max_capacity):
    #same dp table as topdown, non-recursive memoization
    dp = [0 for _ in range(max_capacity+1)]

    for cur_capacity in range(max_capacity+1):
        #get value that comes from picking each choice of item
        opt_val = 0
        for item_index in range(len(items)):
            #if item can fit
            if cur_capacity - items[item_index][0] >= 0:
                #item fits - use answer to prev subproblem (which has been calculated)
                item_val = dp[cur_capacity - items[item_index][0]] + items[item_index][1]
                opt_val = max(item_val, opt_val)
            #if item doesn't fit ignore
        #if none of the items fit then thex capacity was just 0 anyways (optval's starting value)
        dp[cur_capacity] = opt_val

    return dp[max_capacity]




#value with smallest weight has highest profit to weight ratio
def test1():
    weights = [1, 2, 3, 4]
    profits = [4, 3, 2, 1]
    items = list(zip(weights, profits))
    max_capacity = 4
    correct = 16
    testknaps(items, max_capacity, correct)


#one best value that doesn't fit all the way, then needs to fit another
def test2():
    weights = [1, 2, 3, 4]
    profits = [1, 4, 9, 2]
    items = list(zip(weights, profits))
    max_capacity = 8
    correct = 9 + 9 + 4
    testknaps(items, max_capacity, correct)

#item with largest weight can be picked once and provides best answer
def test3():
    weights = [1, 2, 3, 4, 5, 6, 7, 8]
    profits = [1, 2, 3, 4, 5, 6, 7, 21]
    items = list(zip(weights, profits))
    max_capacity = 8
    correct = 21
    testknaps(items, max_capacity, correct)

#item with second largest weight plus another item is best choice, even though largest weight has best value
    
def test4():
    weights = [1, 2, 3, 4, 5, 6, 7, 8]
    profits = [2, 2, 3, 4, 5, 6, 99, 100]
    items = list(zip(weights, profits))
    max_capacity = 8
    correct = 99 + 2
    testknaps(items, max_capacity, correct)

#3, 3, 1, 1
def test5():
    weights = [1, 2, 3, 4, 5, 6, 7, 8]
    profits = [2, 3, 50, 4, 5, 6, 99, 100]
    items = list(zip(weights, profits))
    max_capacity = 8
    correct = 104
    testknaps(items, max_capacity, correct)


def testknaps(items, max_capacity, correct):    
    print("Correct: " + str(correct))
    print("Knapsack Top-down: " + str(knapsack_topdown(items, max_capacity)))
    print("Knapsack Bottom-up: " + str(knapsack_bottomup(items, max_capacity)))
    print()

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
main()
