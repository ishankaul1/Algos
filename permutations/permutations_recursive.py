#returns all permutations of a list using recursion

def permute(arr):
    if len(arr) == 1:
        return [arr]

    old_perms = permute(arr[:-1])
    excluded = arr[-1]
    
    new_perms = []

    for perm in old_perms:
        for i in range(len(perm)+1):
            newperm = perm[:i] + [excluded] + perm[i:]
            new_perms.append(newperm)

    return new_perms

def test1():
    arr = [1]
    print(permute(arr))

def test2():
    arr = [1, 2, 3, 4]
    print(permute(arr))



def main():
    test1()
    test2()


main()
