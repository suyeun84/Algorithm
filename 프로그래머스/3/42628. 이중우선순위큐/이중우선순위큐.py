import heapq
def solution(operations):
    heap = []
    for operation in operations:
        op = operation.split(" ")
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D":
            if len(heap) == 0:
                continue
            if int(op[1]) == 1: #최댓값 삭제
                heap.remove(max(heap))
            elif int(op[1]) == -1: #최솟값 삭제
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0, 0]
    return [max(heap), heapq.heappop(heap)]