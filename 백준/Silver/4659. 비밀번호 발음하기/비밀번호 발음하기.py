import sys


def solution():
    input = sys.stdin.readline
    alpa = ['a', 'e', 'i', 'o', 'u']

    def condition1(str1):
        for s in alpa:
            if s in str1:
                return True
        return False

    def condition2(str2):
        word = [0]*len(str2)
        for i in range(len(str2)):
            if str2[i] in alpa:
                word[i] = 1
            if i >= 2:
                if word[i-2] == word[i-1] and word[i-1] == word[i]:
                    return False
        return True

    def condition3(str3):
        for i in range(len(str3)-1):
            if str3[i] == str3[i+1] and str3[i] != 'e' and str3[i] != 'o':
                return False
        return True

    while True:
        str = input().strip()
        if str == 'end':
            return
        if condition1(str) and condition2(str) and condition3(str):
            print('<'+str+'> is acceptable.')
        else:
            print('<'+str+'> is not acceptable.')


if __name__ == '__main__':
    solution()
