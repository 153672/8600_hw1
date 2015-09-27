import search
import time

__author__ = 'Mart Aarma'


class MagicHexagonProblem(search.Problem):

    def __init__(self, allNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]):

        # idx 0-> /a|b|c\
        #        /d|e|f|g\
        #       /h|i|j|k|l\
        #        \m|n|o|p/
        #         \r|s|t/

        # idx 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
        #     a,b,c,g,l,p,t,s,r,m,h, d, e, f, k, o, n, i, j
        # (18, 11, 9, 14, 15, 13, 10, 12, 16, 19, 3, 17, 1, 6, 8, 4, 2, 7, 5)
        # [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.allNumbers = allNumbers
        self.initial = tuple([0] * 19)

    def actions(self, state):
        if state[0] == 0:
            return self.allNumbers

        idx = state.index(0) - 1
        if self.check_partial_solution(state, idx):
            # see document "Equations for solving Magic hexagon problem.pdf"
            # center value can be calculated if rows of 3 are calculated and correct
            centerValue = 0
            if 10 < idx < 17:
                blue = (state[1] + state[3] + state[5] + state[7] + state[9] + state[11])
                yellow = 114 - blue
                centerValue = 19 - (yellow / 2)

                # if invalid center value is found, this path will not be explored
                if centerValue < 1:
                    return []
                elif centerValue in state:
                    return []

            # also this center value can not be put in any other index but the last, so its excluded from
            # available numbers until last index is at hand.
            return [e for e in self.allNumbers if e != centerValue and e not in state]
        else:
            # paths that violate constraints, will not be explored further
            return []

    def result(self, state, action):
        localstate = list(state)
        localstate[state.index(0)] = action
        return tuple(localstate)

    def h(self, node):
        state = node.state
        s = sum(state)
        h = state[10]

        if h != 0:
            # see document "Equations for solving Magic hexagon problem.pdf"
            # 67 < p < 76, all other permutations for rows of 3 are penalised
            p = state[0] + state[2] + state[4] + state[6] + state[8] + h
            if p > 76:
                p -= 76
            elif p < 67:
                p = 67 - p
            else:
                p = 0
        else:
            p = 0

        return (190 - s) + (p * 150)

    def h1(self, node):
        return (190 - sum(node.state))

    def goal_test(self, state):
        return self.check_solution(state, True)

    def check_partial_solution(self, state, idx):
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

        g = state[3]
        d = state[11]
        e = state[12]
        f = state[13]

        if self.check_rows_of_4(d, e, f, g):
            b = state[1]
            p = state[5]
            k = state[14]
            if self.check_rows_of_4(b, f, k, p):
                s = state[7]
                o = state[15]
                if self.check_rows_of_4(g, k, o, s):
                    m = state[9]
                    n = state[16]
                    if self.check_rows_of_4(m, n, o, p):
                        i = state[17]
                        if self.check_rows_of_4(b, e, i, m):
                            if self.check_rows_of_4(d, i, n, s):
                                c = state[2]
                                r = state[8]
                                j = state[18]
                                if self.check_rows_of_5(c, f, j, n, r):
                                    l = state[4]
                                    h = state[10]
                                    if self.check_rows_of_5(h, i, j, k, l):
                                        a = state[0]
                                        t = state[6]
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


class InstrumentedProblem(search.Problem):
    """Delegates to a problem, and keeps statistics."""

    def __init__(self, problem):
        self.problem = problem
        self.succs = self.goal_tests = self.states = self.heuristic = 0
        self.found = None
        self.start_time = time.time()

    def actions(self, state):
        self.succs += 1
        return self.problem.actions(state)

    def result(self, state, action):
        self.states += 1
        return self.problem.result(state, action)

    def goal_test(self, state):
        self.goal_tests += 1
        result = self.problem.goal_test(state)
        if result:
            self.found = state
        return result

    def h(self, node):
        self.heuristic += 1
        return self.problem.h(node)

    def path_cost(self, c, state1, action, state2):
        return self.problem.path_cost(c, state1, action, state2)

    def value(self, state):
        return self.problem.value(state)

    def __getattr__(self, attr):
        return getattr(self.problem, attr)

    def set_end_time(self, end_time):
        self.end_time = end_time
    def __repr__(self):
        return '<%4d/%4d/%4d/%4d/%s/time: %s s>' % (self.succs, self.goal_tests,
                                     self.states, self.heuristic, str(self.found)[:67], (self.end_time - self.start_time))

def compare_searchers(problems, header,
                      searchers=[search.depth_first_tree_search, search.depth_limited_search, search.depth_first_graph_search,
                                 search.recursive_best_first_search, search.breadth_first_tree_search, search.iterative_deepening_search]):

    def do(searcher, problem):
        p = InstrumentedProblem(problem)
        searcher(p)
        p.set_end_time(time.time())
        return p
    table = [[search.name(s)] + [do(s, p) for p in problems] for s in searchers]
    search.print_table(table, header)

reversedNumbers = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

mhp = MagicHexagonProblem()
start_time = time.time()
print("----- Start")
#search.compare_searchers([mhp], ["Searcher","Result"])
print(search.iterative_deepening_search(mhp).solution())
#print(search.astar_search(mhp, mhp.h1).solution())
print("--- Total %s seconds ---" % (time.time() - start_time))
