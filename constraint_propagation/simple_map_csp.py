#!/usr/bin/env python3

initial = [ "?", "?", "?", "?" ]

DOMAIN = [ "red", "green" ]

def isValid(state):
    valid = True
    if ( state[0] != "?" ) and ( state[1] != "?" ) and ( state[0] == state[1] ):
        valid = False
    elif ( state[1] != "?" ) and ( state[2] != "?" ) and ( state[1] == state[2] ):
        valid = False
    elif ( state[2] != "?" ) and ( state[3] != "?" ) and ( state[2] == state[3] ):
        valid = False
    elif ( state[3] != "?" ) and ( state[0] != "?" ) and ( state[3] == state[0] ):
        valid = False
    elif ( state[0] != "?" ) and ( state[2] != "?" ) and ( state[0] == state[2] ):
        valid = False
    return valid

def isSolution( state ):
    sol = True
    for s in state:
        if (s == "?" ):
            sol = False
            break
    if ( sol ):
        sol = isValid(state)
    return sol

def genChildren( state ):
    children = []
    for i in range(len(state)):
        if ( state[i] == "?" ):
            for d in DOMAIN:
                ns = state[0:i] + [d] + state[i+1:]
                children = children + [ns]
    return children
    
def search(initial):
    queue = [ (initial, [] ) ]
    solution = None
    numNodes = 1
    while(len(queue) > 0):
        state,hist = queue.pop()
        depth = len(hist)
        ind = "   " * depth
        print(ind, end="")
        print('Current state:', state)
        if ( isSolution(state) ):
            solution = state
            break
        children = genChildren(state)
        for c in children:
            if ( c not in hist ):
#                queue= queue + [ (c, hist + [state]) ]
                queue= [ (c, hist + [state]) ] + queue
                numNodes = numNodes + 1
    return (solution, numNodes)
        
    
    
#print(isValid(initial))
#print(isValid( ["red", "?", "green", "?"] ))
#print(isSolution( ["red", "green", "red", "green"] ))
#print(genChildren(["?", "red", "?", "green"]))
#print(genChildren(initial))
print(search(initial))

        