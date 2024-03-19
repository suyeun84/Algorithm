def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    b_idx = 0
    for a_idx in range(len(A)):
        if A[a_idx] < B[b_idx]:
            answer += 1
            b_idx += 1
    
    return answer