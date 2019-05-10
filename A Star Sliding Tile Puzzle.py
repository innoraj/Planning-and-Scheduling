# A Star Sliding Tile Puzzle
# Run on Python 3

import random

class State:

    def __init__(self, nsize):
        """Initialze the n-puzzle problem, with n size defined by user.
        """
        self.nsize = nsize
        self.tsize = pow(self.nsize, 2)
        self.goal = list(range(1, self.tsize))
        self.goal.append(0)

    def prlist(self, st):
        """Print the list in a Matrix Format."""
        for (index, value) in enumerate(st):
            s = ' %s ' % value
            print (s, end="\t" )
            if index in [x for x in range(self.nsize - 1, self.tsize, 
                         self.nsize)]:
                print ()
        print ()

    def movefunc(self, key):
        """Motions at various key positions in the Matrix."""
        values = [1, -1, self.nsize, -self.nsize]
        valid = []
        for x in values:
            if 0 <= key + x < self.tsize:
                if x == 1 and key in range(self.nsize - 1, self.tsize, 
                        self.nsize):
                    continue
                if x == -1 and key in range(0, self.tsize, self.nsize):
                    continue
                valid.append(x)
        return valid

    def expand(self, st):
        """Provide the list of next possible states from current state."""
        pexpands = {}
        for key in range(self.tsize):
            pexpands[key] = self.movefunc(key)
        pos = st.index(0)
        moves = pexpands[pos]
        expstates = []
        for mv in moves:
            nstate = st[:]
            (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos + 
                    mv])
            expstates.append(nstate)
        return expstates

    def one_of_poss(self, st):
        """Choose one of the possible states."""
        exp_sts = self.expand(st)
        rand_st = random.choice(exp_sts)
        return rand_st

    def st_state(self, seed=1000):
        """Determine the Start State of the Problem."""
        start_st = (self.goal)[:]
        for sts in range(seed):
            start_st = self.one_of_poss(start_st)
        return start_st

    def final_st(self, st):
        """Check if the Goal Reached or Not."""
        return st == self.goal

    def manhatan_dis(self, st):
        """Calculate the Manhattan Distances of the particular State.
        """
        mdist = 0
        for node in st:
            if node != 0:
                gdist = abs(self.goal.index(node) - st.index(node))
                (jumps, steps) = (gdist // self.nsize, gdist % self.nsize)
                mdist += jumps + steps
        return mdist

    def misplaced_dis(self, st):
        dist = 0
        for index,val in enumerate(st):
            if val != self.goal[index]:
                dist+=1
        return dist

    def heuristic_next(self, st, heuristic ="manhattan"):
        """This is the Heuristic Function. It determines the next state to follow and uses Mahattan distances method as the heuristics"""
        exp_sts = self.expand(st)
        mdists = []
        if heuristic == "manhattan":
            for st in exp_sts:
                mdists.append(self.manhatan_dis(st))
        elif heuristic == "misplaced":
            for st in exp_sts:
                mdists.append(self.misplaced_dis(st))
        mdists.sort()
        short_path = mdists[0]
        if mdists.count(short_path) > 1:
            if heuristic == "manhattan":
                least_paths = [st for st in exp_sts if self.manhatan_dis(st) == short_path]
            elif heuristic == "misplaced":
                least_paths = [st for st in exp_sts if self.misplaced_dis(st) == short_path]

            return random.choice(least_paths)
        else:
            for st in exp_sts:
                if heuristic== "manhattan" and  self.manhatan_dis(st) == short_path:
                    return st
                elif heuristic == "misplaced" and self.misplaced_dis(st) == short_path:
                    return st

    def solve_it(self, st, heuristic="manhattan"):
        if heuristic =="manhattan":
            while not self.final_st(st):
                st = self.heuristic_next(st)
                self.prlist(st)
        elif heuristic == "misplaced":
            while not self.final_st(st):
                st = self.heuristic_next(st,heuristic="misplaced")
                self.prlist(st)


if __name__ == '__main__':
    print ('Sliding Tile Puzzle')
    print (20*'-')
    print (' choose random size ')
    print ('eg  for 3x3 choose 3 for 5x5 choose 5....so on')
    a=int(input())
    state = State(a)
    print ('Choose a random seed:')
    b=int(input())
    start = state.st_state(5)
    print ("")
    state.prlist(start)
    print ('The Goal State should be:')
    state.prlist(state.goal)
    print ("Please select the Heuristic method: \n1. misplaced\n2. Manhattan ")
    print ("Enter your choice 1 or 2")
    choice = int(input())
    print ('Here it Goes:')
    state.prlist(start)
    if choice == 1:
        state.solve_it(start,heuristic="misplaced")
    else:
        state.solve_it(start, heuristic="manhattan")