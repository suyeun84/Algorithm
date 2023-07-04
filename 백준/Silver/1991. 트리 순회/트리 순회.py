import sys
input = sys.stdin.readline

n = int(input())
#dictionary
graph = {}

for _ in range(n):
    curr, left, right = input().strip().split()
    graph[curr] = [left, right]

def preorder(curr):
    print(curr, end="")
    for node in graph[curr]:
        if node != ".":
            preorder(node)

def inorder(curr):
    if graph[curr][0] != ".":
        inorder(graph[curr][0])
    print(curr, end="")
    if graph[curr][1] != ".":
        inorder(graph[curr][1])
    

def postorder(curr):
    for node in graph[curr]:
        if node != ".":
            postorder(node)
    print(curr, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")