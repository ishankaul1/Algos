#Returns all subsets of a list using recursion

def get_subsets(arr):
    subsets = [[]]
    if not arr:
        return subsets
    subsets_excluding_last = get_subsets(arr[:-1])
    subsets_including_last = []

    for subset in subsets_excluding_last:
        subsets_including_last.append(subset + [arr[-1]])
    return subsets_excluding_last + subsets_including_last




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
