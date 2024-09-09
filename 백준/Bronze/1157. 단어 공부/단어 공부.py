from collections import Counter


def solution():
    str = Counter(input().upper())
    top = str.most_common(2)
    if len(top) == 1 or top[0][1] != top[1][1]:
        print(top[0][0])
    else:
        print("?")


if __name__ == '__main__':
    solution()
