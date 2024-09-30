import sys

def solution():
    input = sys.stdin.readline
    # N: 벨트에 놓인 접시 수, d: 초밥 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
    N, d, k, c = map(int, input().split())
    belt = []
    answer = 0
    dic = {}
    for _ in range(N):
        belt.append(int(input()))
    if c in dic:
        answer = max(answer, len(dic))
    else:
        answer = max(answer, len(dic)+1)

    for i in range(k):
        if belt[i] not in dic:
            dic[belt[i]] = 1
        else:
            dic[belt[i]] += 1
    # 다음거 넣어주는 곳
    for i in range(k, N+k):
        if i >= N:
            i = i % N
        if belt[i] not in dic:
            dic[belt[i]] = 1
        else:
            dic[belt[i]] += 1
        # 마지막 초밥 빼주기
        if dic[belt[i-k]] == 1:
            del dic[belt[i-k]]
        else:
            dic[belt[i-k]] -= 1

        if c in dic:
            answer = max(answer, len(dic))
        else:
            answer = max(answer, len(dic)+1)

    print(answer)


if __name__ == '__main__':
    solution()
