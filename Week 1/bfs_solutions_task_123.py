
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []   # the input pattern
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

adj = [(-1,0),(0,1),(1,0),(0,-1)]   # relative positions around a position

def valid(r,c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)   # the board pattern
        self.g = 0                  # the number of moves so far
        self.parent = None          # the parent state

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

def successor(s):  # generates list of successor states of s
    # Replace the "pass" line with appropriate code
    successor_list = []
    hr, hc = hole_index(s)
    for d in adj:
        # Compute the tile position i,j to be swapped with the hole
        i = hr + d[0]
        j = hc + d[1]
        pass
        if valid(i,j):
            x = copy.deepcopy(s)
            # Swap x's tile at position i,j with the hole
            x.p[i][j], x.p[hr][hc] = x.p[hr][hc], x.p[i][j]
            # Record one addition move
            x.parent = s # x come from s and then swap
            x.g += 1
            # Add x to successor list
            successor_list.append(x)
    return successor_list

def bfs(s):
    global count       # increments each time a state is enqueued

    # Complete the code below this line
    Q = []
    while not is_goal(s):
        for x in successor(s):
            count += 1
            Q.append(x)
        s = Q[0]
        del Q[0]
    return s # return goal state where s is goal

def print_path(s, v):  # s is the initial state, v is the current state
    global count
    if v == s:
        print(s.p)
    elif v.parent is None:
        print("no path found")
    else:
        print_path(s,v.parent)
        print(f"Move {v.g}: ", v.p)

count = 0
initial = state(p)
v = bfs(initial)
print(f"{v.g} moves, {count} states stored")
print("Initial:", end=" ")   # prints the number of moves and total number of states generated
print_path(initial, v)
