
#Algorithm to bottom-up fill dp table and output maximum profit from fitting a list of items in a knapsack
#Implementation is simple but filling whole dp table can be very expensive, especially when dealing with a large starting capacity
#item = list of [weight, profit] pairs to represent an item
def knapsack_bottomup(capacity, items):
    #rows = # items, columns = capacity
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(items))]
    for item_index in range(len(items)):
        for cur_capacity in range(capacity+1):
            #if cur_capacity < item weight, exclude item
            #else take max(include, exclude)
            if cur_capacity < items[item_index][0]:
                dp[item_index][cur_capacity] = dp[item_index-1][cur_capacity] #works at item index 0 because dp[-1] just pull a 0 from the last item index; would be index out of range in any other language
            else:
                dp[item_index][cur_capacity] = max(dp[item_index-1][cur_capacity], dp[item_index-1][cur_capacity - items[item_index][0]] + items[item_index][1]) #item index 0 will just add item value to 0 if it fits in capacity

    return dp[len(dp)-1][len(dp[0])-1]

#Algorithm to fill dp table top-down to find maximum profit from fitting a list of items in a knapsack
#Saves time by not filling entire dp table - instead only fills as needed when recursively choosing subproblems
def knapsack_topdown(capacity, items):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(items)+1)]

    def topdown_calc(cur_capacity, item_index):
        #if function called on capacity of 0 or a list of 0 items, max value is 0
        if cur_capacity == 0 or item_index == 0:
            return 0
        #if max value of subproblem excluding item has not been calculated, must calculate first before making any decisions
        if dp[item_index-1][cur_capacity] == -1:
            dp[item_index-1][cur_capacity] = topdown_calc(cur_capacity, item_index-1)

        #if weight of current item is greater than the current capacity, item must be excluded by default
        if items[item_index-1][0] > cur_capacity:
            dp[item_index][cur_capacity] = dp[item_index-1][cur_capacity]
        else:
            #optimal value for this subproblem will be the maximum of including the item and excluding the item
            #need to check if value for the subproblem where item is included has been calculated
            if dp[item_index-1][cur_capacity-items[item_index-1][0]] == -1:
                dp[item_index-1][cur_capacity-items[item_index-1][0]] = topdown_calc(cur_capacity - items[item_index-1][0], item_index-1)
            dp[item_index][cur_capacity] = max(dp[item_index-1][cur_capacity], dp[item_index-1][cur_capacity-items[item_index-1][0]] + items[item_index-1][1])
        return dp[item_index][cur_capacity]
        
    opt = topdown_calc(capacity, len(items))
    return opt





def test1():
    print("Test1")
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    capacity = 7
    items = list(zip(weights, profits))
    print("Correct: 22")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test2():
    
    print("Test2")
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    capacity = 5
    items = list(zip(weights, profits))
    print("Correct: 10")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()
def test3():
    print("Test3")
    capacity = 26
    weights = [12, 7, 11, 8, 9]
    profits = [24, 13, 23, 15, 16]
    items = list(zip(weights, profits))
    print("Correct profit: " + str(13 + 23 + 15))
    print("Correct weights: 7, 11, 8")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test4():
    print("Test4")
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    capacity = 165
    items = list(zip(weights, profits))
    print("Correct profit: " + str(92 + 57 + 49 + 68 + 43))
    print("Correct weights: 23, 31, 29, 44, 38")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test5():
    print("Test5")
    capacity = 190
    weights = [56, 59, 80, 64, 75, 17]
    profits = [50, 50, 64, 46, 50 , 5]
    items = list(zip(weights, profits))
    print("Correct profit: " + str(50 + 50 + 50))
    print("Correct weights: 56 + 59 + 75")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test6():
    print("Test6")
    capacity = 50
    weights = [31, 10, 20, 19, 4, 3, 6]
    profits = [70, 20, 39, 37, 7, 5, 10]
    items = list(zip(weights, profits))
    print("Correct profit: " + str(70 + 37))
    print("Correct weights: 31, 19")
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test7():
    print("Test7")
    capacity = 750
    weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    profits = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    items = list(zip(weights, profits))
    correct = [1, 3, 5, 7, 8, 9, 14, 15]

    correct_sum = 0
    correct_weights = "Correct weights: "
    for i in correct: 
        correct_sum += profits[i-1]
        correct_weights += str(weights[i-1]) + ", "
    
    print("Correct profit: " + str(correct_sum))
    print(correct_weights)
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def test8():
    print("Test8")
    capacity = 6404180
    weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]
    profits = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261]
    items = list(zip(weights, profits))
    correct = [1, 2, 4, 5, 6, 10, 11, 13, 16, 22, 23, 24]

    correct_sum = 0
    correct_weights = "Correct weights: "
    for i in correct: 
        correct_sum += profits[i-1]
        correct_weights += str(weights[i-1]) + ", "
    
    print("Correct profit: " + str(correct_sum))
    print(correct_weights)
    print("Bottomup Solution: " + str(knapsack_bottomup(capacity, items)))
    print("Topdown Solution: " + str(knapsack_topdown(capacity, items)))
    print()

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()


main()
