import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/4195

def find(f):
    if f == parent[f]:
        return f
    else:
        root = find(parent[f])
        parent[f] = root
        return parent[f]
    
def union(f1, f2):
    root1 = find(f1)
    root2 = find(f2)

    if root1!=root2:
        parent[root2] = root1
        network[root1] += network[root2]

T = int(input())

answer = []
for _ in range(T):
    F = int(input())
    global parent, network
    parent = dict()
    network = dict()
    for f in range(F):
        f1, f2 = input().rstrip().split()
        if f1 not in network:
            parent[f1] = f1
            network[f1] = 1
        if f2 not in network:
            parent[f2] = f2
            network[f2] = 1
        
        union(f1, f2)
        answer.append(str(network[find(f1)]))
print('\n'.join(answer))