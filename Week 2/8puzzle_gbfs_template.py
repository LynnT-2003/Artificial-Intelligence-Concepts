
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

from simplePriorityQueue import Simple_Priority_Queue

adj = [(-1,0),(0,1),(1,0),(0,-1)]

def heuristic(p):   # Take pattern p, then return its heuristic value
    # options are number of misplaced tiles or total manhatton distance
    # Complete the code below this line
    pass

def valid(r,c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.h = manhatton(p)
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
            x.h = manhatton(x.p)
            succ.append(x)
    return succ

def gbfs(s):  # Greedy Best-first Search
    global count

    # Complete the code below this line
    pass

def print_path(s, v):  # s is the initial state, v is the current state
    pass

count = 0
initial = state(p)
v = gbfs(initial)
print(v.g, count)
print_path(initial, v)
