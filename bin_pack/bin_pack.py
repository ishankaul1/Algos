import heapq

#Problem: Given a list of items and sizes of bins, return (approximately) the least number of bins of an inputted size needed to fit all the items.

#find the first bin in which the items fit
def first_fit(items, bin_size):
    bins = [bin_size]

    for item in items:
        foundBin = False
        for bin_index in range(len(bins)):
            if (bins[bin_index] - item) >= 0:
                #bin found - add item to bin
                bins[bin_index] -= item
                foundBin = True
                break
        if not foundBin:
            bins.append(bin_size - item)

    return len(bins)



#find the largest bin in which the items fit
def best_fit(items, bin_size):
    bins = [bin_size * -1] #popping heapq gives us the min of the heap in constant time - keep values negative so we have the largest value instead
    heapq.heapify(bins)

    for item in items:
        #print(bins)
        largest = bins[0] * -1
        
        if largest - item >= 0:
            #item fits in largest - push largest-item to heap
            heapq.heappushpop(bins, -1 * (largest - item))
        else:
            #item does not fit in largest - push largest back into heap, and a new bin where item fits
            heapq.heappush(bins, -1 * (bin_size - item))
    return len(bins)



#order objects descending, then find the first bin in which the objects fit
def first_fit_decr(items, bin_size):
    items = sorted(items, reverse=True)
    return first_fit(items, bin_size)


#order objects descending, then find largest bin in which the objects fit
def best_fit_decr(items, bin_size):
    items = sorted(items, reverse=True)
    return best_fit(items, bin_size)

def test1():
    items = [1, 1, 1, 1]
    bin_size = 1
    print("Opt: 4")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()


def test2():
    items = [1, 1, 1, 1]
    bin_size = 2
    print("Opt: 2")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()


def test3():
    items = [1, 1, 1, 1]
    bin_size = 3
    print("Opt: 2")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()


def test4():
    items = [5,6,3,7,5,4]
    bin_size = 10
    print("Opt: 3")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()


def test5():
    items = [49, 41, 34, 33, 29, 26, 26, 22, 20, 19]
    bin_size = 100
    print("Opt: 4")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()

def test6():
    items = [70, 60, 50, 33, 33, 33, 11, 7, 3]
    bin_size = 100
    print("Opt: 4")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()

def test7():
    items = [442, 252, 252, 252, 252, 252, 252, 252, 127, 127, 127, 127, 127, 106, 106, 106, 106, 85, 84, 46, 37, 37, 12, 12, 12, 10, 10, 10, 10, 10, 10, 9, 9]
    bin_size = 524
    print("Opt: 7")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
    print()


def test8():
    items = [49, 41, 34, 33, 29, 26, 26, 22, 20, 19]
    bin_size = 100
    print("Opt: 4")
    print("FF: " + str(first_fit(items, bin_size)))
    print("BF: " + str(best_fit(items, bin_size)))
    print("FFD: " + str(first_fit_decr(items, bin_size)))
    print("BFD: " + str(best_fit_decr(items, bin_size)))
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
