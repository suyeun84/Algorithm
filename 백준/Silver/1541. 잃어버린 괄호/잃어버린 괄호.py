import sys


def solution():
    input = sys.stdin.readline
    sent = list(map(str, input().strip().split('-')))
    answer = 0
    flag = True
    for i in sent:
        temp = str(i).strip().split('+')
        sum = 0
        for num in temp:
            sum += int(num)
        if flag:
            answer += sum
            flag = False
        else:
            answer -= sum
    print(answer)


if __name__ == '__main__':
    solution()
