
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

adj = [(-1,0),(0,1),(1,0),(0,-1)]

def valid(r,c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.parent = None

def is_goal(s):
    if s.p == goal:
        return True
    else:
        return False

def hole_index(s):
    for i in range(3):
        for j in range(3):
            if s.p[i][j] == 0:
                return i,j

def successor(s):
    succ = []
    hr, hc = hole_index(s)
    for d in adj:
        i = hr + d[0]
        j = hc + d[1]
        if valid(i,j):
            x = copy.deepcopy(s)
            x.p[hr][hc], x.p[i][j] = x.p[i][j], x.p[hr][hc]
            x.parent = s
            x.g += 1
            succ.append(x)
    return succ

def DFS(s, maxDepth):  # depth is limited to be <= maxDepth
    global count       # increments when state s is depth-first searched
    
    if s.g > maxDepth:
        return None
    elif is_goal(s):
        return s
    else:
        count += 1
        # Complete the depth-first mechanism below this line
        

def IDS(s):
    # Complete the code below this line
    pass

def print_path(s, v):  # s is the initial state, v is the current state
    pass

count = 0
initial = state(p)
v = IDS(initial)
print(v.g, count)
print_path(initial, v)
