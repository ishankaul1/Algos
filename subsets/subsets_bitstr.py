#Given: array of integers
#Return: 2D list of all subsets of this array

#iterates from 0-2*len(array). creates subsets according to the positions of the 1-bits of each number in the iteration (all combinations of indices are covered)
def get_subsets_bitstr(arr):
    numbits = len(arr)
    subsets = []
    for i in range(0, (2 ** numbits)):
        cur_subset = []
        bitstr = ('{:0' + str(numbits) + 'b}').format(i)
        for bit in range(len(bitstr)):
            if bitstr[bit] == '1':
                cur_subset.append(arr[bit])

        subsets.append(cur_subset)

    return subsets

def test1():
    print("test1")
    arr = [1, 2, 3]
    print(get_subsets_bitstr(arr))
    print()

def test2():
    print("test2")
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(get_subsets_bitstr(arr))
    print()

def test3():
    print("test3")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_subsets_bitstr(arr))
    print()

def main():
    test1()
    test2()
    test3()

main()
