import sys

def solution():
    input = sys.stdin.readline
    # 남학생 - 받은 수의 배수 상태 변경
    # 여학생 - 받은 수 기준 좌우 대칭인 스위치들 상태 변경
    n = int(input())
    switch = list(map(int, input().split(' ')))
    student_num = int(input())
    
    def change(idx):
        nonlocal switch
        if switch[idx] == 0:
            switch[idx] = 1
        elif switch[idx] == 1:
            switch[idx] = 0

    for _ in range(student_num):
        gender, num = map(int, input().split(' '))
        if gender == 1:
            # 남학생
            for i in range(n):
                if (i+1) % num == 0:
                    change(i)
        elif gender == 2:
            # 여학생
            left = num-1 - 1
            right = num-1 + 1
            change(num-1)
            while left >= 0 and right < n:
                if switch[left] != switch[right]:
                    break
                change(left)
                change(right)
                left -= 1
                right += 1
    for i in range(n//20+1):
        if 20*(i+1) > n:
            print(' '.join(map(str, switch[20 * i:n])))
        else:
            print(' '.join(map(str, switch[20*i:20*(i+1)])))


if __name__ == '__main__':
    solution()
