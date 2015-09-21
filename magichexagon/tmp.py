import search
import time
import random

__author__ = 'Mart Aarma'

class MagicHexagonProblem(search.Problem):

    def __init__(self):
        #        /a|b|c\
        #       /d|e|f|g\
        #      /h|i|j|k|l\
        #       \m|n|o|p/
        #       8\r|s|t/6
        # 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
        # a,b,c,g,l,p,t,s,r,m,h, d, e, f, k, o, n, i, j

        # 3 17 18 11 9 14 15 13 10 12 16 19 7 1 6 8 4 2 5

        # a,0 = 0,1
        # b,1 = 0,1,2
        # c,2 = 0,1,2,3  <-
        # g,3 = 2,3,4
        # l,4 = 2,3,4,5  <-
        # p,5 = 4,5,6
        # t,6 = 4,5,6,7  <-
        # s,7 = 6,7,8
        # r,8 = 6,7,8,9  <-
        # m,9 = 8,9,10
        # h,10 = 8,9,10,11 <-
        # d,11 = 10,11,12, 0? <-
        # e,12 = 11,12,13
        # f,13 = 12,13,14
        # k,14 = 13,14,15
        # o,15 = 14,15,16
        # n,16 = 15,16,17
        # i,17 = 16,17,18
        # j,18 = 17,18,0

        self.initial = tuple([0] * 19)
        self.index = 0;

    # tagastab v6imalikud v22rtused indeksi jaoks ja otsustab milline on j2rmine indeks
    def actions(self, state):
        #if state[0] == 1 and state[1] == 18 and state[2] == 19 and state[3] == 17:
        print(state)

        if state[0] == 0:
            return [e for e in range(1,20)]

        if self.partialSolutionIsValid(state):
            self.index = state.index(0)
            e = [e for e in range(1,20) if e not in state]
            return e
        else:
            if self.valueIsMaxAvailValue(state, state[self.index]):
                return [0]
            else:
                v = state[self.index];
                e = [e for e in range(1,20) if e > v and e not in state]
                return e

    def result(self, state, action):
        localstate = list(state)
        if action == 0:
            self.index = max(0, self.index - 1)
            localstate[self.index] = 0
        else:
            localstate[self.index] = action

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

        if completeCheck and state[-1] == 0:
            return False

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

        if self.checkRowsOf3(a, b, c, completeCheck):
            if self.checkRowsOf3(c, g, l, completeCheck):
                if self.checkRowsOf3(l, p, t, completeCheck):
                    if self.checkRowsOf3(t, s, r, completeCheck):
                        if self.checkRowsOf3(r, m, h, completeCheck):
                            if self.checkRowsOf3(h, d, a, completeCheck):
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
