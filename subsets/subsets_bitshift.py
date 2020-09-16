
def get_subsets(arr):
    bitlen = len(arr)
    subsets = []
    for num in range(2 ** bitlen):
        subset = []
        if num & 1:
            subset.append(arr[0])
        for i in range(1, bitlen):
            num = num >> 1
            if num & 1:
                subset.append(arr[i])
        subsets.append(subset)

    return subsets




def test1():
    print("test1")
    arr = [1, 2, 3]
    print(get_subsets(arr))
    print()

def test2():
    print("test2")
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(get_subsets(arr))
    print()

def test3():
    print("test3")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_subsets(arr))
    print()

def main():
    test1()
    test2()
    test3()

main()
