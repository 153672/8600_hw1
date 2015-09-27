import search
import time
import random

__author__ = 'Mart Aarma'

class MagicHexagonProblem(search.Problem):

    def __init__(self):

        # idx 0-> /a|b|c\
        #        /d|e|f|g\
         #      /h|i|j|k|l\
        #        \m|n|o|p/
        #         \r|s|t/

        # idx 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
        #     a,b,c,g,l,p,t,s,r,m,h, d, e, f, k, o, n, i, j

        # Before going further to inner circle the outer rows of 3 must be correct

        self.initial = tuple([0] * 19)
        self.idx = 0;
        self.c = 0

    # tagastab v6imalikud v22rtused indeksi jaoks ja otsustab milline on j2rmine indeks
    def actions(self, state):

        if state[0] == 0:
            return [e for e in reversed(range(1,20))]

        if self.partialSolutionIsValid(state):
            e = [e for e in reversed(range(1,20)) if e not in state]
            return e
        else:
            if state[-1] == 0:
                idx = state.index(0) - 1
            else:
                idx = 18

            if idx in (3,5,7,9,11) and not self.checkRowOf3(state, idx):
                return []

            v = state[idx];
            e = [e for e in reversed(range(1,20)) if e > v and e not in state]
            return e

    def result(self, state, action):
        localstate = list(state)
        if action == 0:
            print("!!!!!!!!!!!!!")
            localstate[state.index(0) - 1] = 0
        else:
            localstate[state.index(0)] = action

        #print("result:", localstate)
        return tuple(localstate)

    def valueIsMaxAvailValue(self, state, value):
         for e in range(1, 20):
             if e not in state and (e > value):
                 return False
         return True

    def findNextBiggerValue(self, state, min):
        for e in range(min, 20):
            if e not in state:
                return e
        return min

    def goal_test(self, state):
        return self.checkSolution(state, True)

    def partialSolutionIsValid(self, state):
        return self.checkSolution(state, False)

    def checkSolution(self, state, completeCheck):

        state = [18, 17, 3, 19, 16, 12, 10, 13, 15, 14, 9, 11, 1, 7, 2, 4, 8, 6, 5]

        a = state[0]
        b = state[1]
        c = state[2]
        g = state[3]
        l = state[4]
        p = state[5]
        t = state[6]
        s = state[7]
        r = state[8]
        m = state[9]
        h = state[10]
        d = state[11]
        e = state[12]
        f = state[13]
        k = state[14]
        o = state[15]
        n = state[16]
        i = state[17]
        j = state[18]

        completeCheck = False
        rows3Complete = False;

        if not completeCheck:
            if self.checkRowsOf3(a, b, c, completeCheck):
                if self.checkRowsOf3(c, g, l, completeCheck):
                    if self.checkRowsOf3(l, p, t, completeCheck):
                        if self.checkRowsOf3(t, s, r, completeCheck):
                            if self.checkRowsOf3(r, m, h, completeCheck):
                                if self.checkRowsOf3(h, d, a, completeCheck):
                                    rows3Complete = True

        if completeCheck or rows3Complete:
            if self.checkRowsOf4(d, e, f, g, completeCheck):
                if self.checkRowsOf4(g, k, o, s, completeCheck):
                    if self.checkRowsOf4(b, f, k, p, completeCheck):
                        if self.checkRowsOf4(m, n, o, p, completeCheck):
                            if self.checkRowsOf4(b, e, i, m, completeCheck):
                                if self.checkRowsOf4(d, i, n, s, completeCheck):
                                    if self.checkRowsOf5(c, f, j, n, r, completeCheck):
                                        if self.checkRowsOf5(h, i, j, k, l, completeCheck):
                                            if self.checkRowsOf5(a, e, j, o, t, completeCheck):
                                                return True

        return False

    def checkRowOf3(self, state, index):
        if state[index-3] + state[index - 2] + state[index-1] == 38:
            return True
        return False

    def checkRowsOf3(self, a, b, c, completeCheck):
        if (a == 0 or b == 0 or c == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c == 38:
            return True
        return False

    def checkRowsOf4(self, a, b, c, d, completeCheck):
        if (a == 0 or b == 0 or c == 0 or d == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c + d == 38:
            return True
        return False

    def checkRowsOf5(self, a, b, c, d, e, completeCheck):
        if (a == 0 or b == 0 or c == 0 or d == 0 or e == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c + d + e == 38:
            return True
        return False


nq1 = MagicHexagonProblem();
start_time = time.time()
print(search.depth_first_graph_search(nq1).solution())
print("--- %s seconds ---" % (time.time() - start_time))
