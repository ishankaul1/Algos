#longest common (contiguous) substring between two strings

def LCS(str1, str2):
    maxSoFar = 0 #max length of a common substring so far
    table = [[0 for i in range(len(str2))]for j in range(len(str1))] # length of current substring
    #print(table)
    for i in range(len(str1)):
        #for character in first string
        for j in range(len(str2)):
            
        #iterate through characters in second string
            if (j != 0 and i != 0):
                table[i][j] = table[i-1][j-1]
            if str1[i] == str2[j]:
                table[i][j] += 1
            else:
                table[i][j] = 0
            if table[i][j] > maxSoFar:
                maxSoFar = table[i][j]

            #print(str1[i], str2[j], table[i][j], table[i-1][j-1])
            #print(table)
            
            

    return maxSoFar

def test0():
    a = "abc"
    b = "bc"
    print("Correct: 2")
    print("Solution: " + str(LCS(a, b)))
    print()

def test1():
    a = "abbacde"
    b = "bbazcda"
    print("Correct: 3")
    print("Solution: " + str(LCS(a, b)))
    print()

def test2():
    a = "abcdefg"
    b = "hijklmn"
    print("Correct: 0")
    print("Solution: " + str(LCS(a, b)))
    print()

def test3():
    a = "abcdefg"
    b = "hijklma"
    print("Correct: 1")
    print("Solution: " + str(LCS(a, b)))
    print()

def test4():
    a = "abc"
    b = "dbc"
    print("Correct: 2")
    print("Solution: " + str(LCS(a, b)))
    print()

def test5():
    a = "abcd"
    b = "xcdy"
    print("Correct: 2")
    print("Solution: " + str(LCS(a, b)))
    print()

def test6():
    a = "abcde"
    b = "abcde"
    print("Correct: 5")
    print("Solution: " + str(LCS(a, b)))
    print()

def test7():
    a = "abcdeffffffffffxyz"
    b = "xyzxxxxxxabcdexx"
    print("Correct: 5")
    print("Solution: " + str(LCS(a, b)))
    print()


def main():
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
main()
