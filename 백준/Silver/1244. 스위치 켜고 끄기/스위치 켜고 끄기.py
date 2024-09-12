import sys

def solution():
    input = sys.stdin.readline
    # 남학생 - 받은 수의 배수 상태 변경
    # 여학생 - 받은 수 기준 좌우 대칭인 스위치들 상태 변경
    n = int(input())
    switch = list(map(int, input().split(' ')))
    student_num = int(input())

    for _ in range(student_num):
        gender, num = map(int, input().split(' '))
        if gender == 1:
            # 남학생
            for i in range(n):
                if (i+1) % num == 0:
                    if switch[i] == 0:
                        switch[i] = 1
                    elif switch[i] == 1:
                        switch[i] = 0
        elif gender == 2:
            # 여학생
            left = num-1 - 1
            right = num-1 + 1
            if switch[num-1] == 1:
                switch[num-1] = 0
            else:
                switch[num-1] = 1
            while left >= 0 and right < n:
                if switch[left] != switch[right]:
                    break
                if switch[left] == 1:
                    switch[left] = 0
                else:
                    switch[left] = 1
                if switch[right] == 1:
                    switch[right] = 0
                else:
                    switch[right] = 1
                left -= 1
                right += 1
    for i in range(n//20+1):
        if 20*(i+1) > n:
            print(' '.join(map(str, switch[20 * i:n])))
        else:
            print(' '.join(map(str, switch[20*i:20*(i+1)])))


if __name__ == '__main__':
    solution()
