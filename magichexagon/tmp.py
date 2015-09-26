import search
import time

__author__ = 'Mart Aarma'


class MagicHexagonProblem(search.Problem):
    def __init__(self):

        # idx 0-> /a|b|c\
        #        /d|e|f|g\
        #       /h|i|j|k|l\
        #        \m|n|o|p/
        #         \r|s|t/

        # idx 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
        #     a,b,c,g,l,p,t,s,r,m,h, d, e, f, k, o, n, i, j
        # (18, 11, 9, 14, 15, 13, 10, 12, 16, 19, 3, 17, 1, 6, 8, 4, 2, 7, 5)

        self.allNumbers = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.initial = tuple([0] * 19)

    def actions(self, state):
        if state[0] == 0:
            return self.allNumbers

        if self.check_partial_solution(state):
            return [e for e in self.allNumbers if e not in state]
        else:
            return []

    def result(self, state, action):
        localstate = list(state)
        localstate[state.index(0)] = action
        return tuple(localstate)

    def goal_test(self, state):
        return self.check_solution(state, True)

    def check_partial_solution(self, state):
        idx = state.index(0) - 1

        if idx in (2, 4, 6, 8, 10):
            return state[idx - 2] + state[idx - 1] + state[idx] == 38
        elif idx == 11:
            return state[8] + state[9] + state[10] == 38 and state[10] + state[11] + state[0] == 38
        else:
            if idx > 11:
                return self.check_solution(state, False)
            else:
                return True

    def check_solution(self, state, goalCheck):

        if goalCheck and state[-1] == 0:
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

        if self.check_rows_of_4(d, e, f, g):
            if self.check_rows_of_4(g, k, o, s):
                if self.check_rows_of_4(b, f, k, p):
                    if self.check_rows_of_4(m, n, o, p):
                        if self.check_rows_of_4(b, e, i, m):
                            if self.check_rows_of_4(d, i, n, s):
                                if self.check_rows_of_5(c, f, j, n, r):
                                    if self.check_rows_of_5(h, i, j, k, l):
                                        if self.check_rows_of_5(a, e, j, o, t):
                                            return True

        return False

    def check_rows_of_4(self, a, b, c, d):
        if b == 0 or c == 0 or a == 0 or d == 0:
            return True
        return a + b + c + d == 38

    def check_rows_of_5(self, b, c, d, a, e):
        if a == 0 or b == 0 or c == 0 or d == 0 or e == 0:
            return True
        return a + b + c + d + e == 38


nq1 = MagicHexagonProblem();
start_time = time.time()
print(search.depth_first_graph_search(nq1).solution())
print("--- %s seconds ---" % (time.time() - start_time))
