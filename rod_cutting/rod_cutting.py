#problem: given a rod length L, and array containing all lengths smaller than L, and the price of a rod of that length. Determine the optimal profit from cutting this rod into smaller pieces.
import math

def rod_cut(rodlen, prices):
    dp = [0, prices[0][1]] #base case - rod length 0 gives 0 profit, rod length 1 = value of 1

    for i in range(2, rodlen+1):
        #for each length of rod to calculate
        opt_price = 0
        for j in range(1, math.floor(i/2)+1): #iterate up to 1/2 current length
            price = dp[j] + dp[i-j] #opt at this length is = opt(cut) - opt(length - cut)
            if price > opt_price:
                opt_price = price #update opt price for a rod of this length if it's greater than any calculated so far
            #print(i, j, price)
        if i < rodlen:
            if opt_price < prices[i-1][1]: #take into account that the max profit could be from making no cuts
                opt_price = prices[i-1][1] 
        dp.append(opt_price)

    return dp[-1]


def test1():
    rodlen = 5
    prices = [(1, 2), (2, 5), (3, 7), (4, 8)]
    print("Correct: 12")
    print("Solution: " + str(rod_cut(rodlen, prices)))
    print()

def test2():
    rodlen = 8
    prices = [(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17)]
    print("Correct: 22")
    print("solution: " + str(rod_cut(rodlen, prices)))
    print()

def test3():
    rodlen = 8
    prices = [(1, 3), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17)]
    print("Correct: 24")
    print("solution: " + str(rod_cut(rodlen, prices)))
    print()

def main():
    test1()
    test2()
    test3()

main()





