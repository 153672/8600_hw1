import search
import time

__author__ = 'Mart Aarma'

class MagicHexagonProblem(search.Problem):

    def __init__(self):
        self.initial = [0] * 19
        self.initial[0] = 1

    def actions(self, state):
        if self.partialSolutionIsValid(state):
            return ["startNext"]
        else:
            if self.valueIsMaxAvailValue(state, state[state.index(0) - 1]):
                return ["incPrevVal"]
            else:
                return ["incCurrVal"]

    def result(self, state, action):
        index = state.index(0)
        currentIndex = index - 1;
        if action == "startNext":
            state[state.index(0)] = self.findNextElement(state, None)
        elif action == "incCurrVal":
            state[currentIndex] = self.findNextElement(state, state[currentIndex])
        else:
            self.incPrevValue(state, currentIndex)
        return state

    def incPrevValue(self, state, index):
        state[index] = 0
        elem = state[index - 1]
        newValue = self.findNextElement(state, elem)
        if elem == newValue:
            self.incPrevValue(state, index - 1)
        else:
            state[index - 1] = newValue

    def valueIsMaxAvailValue(self, state, value):
        for e in range(1, 20):
            if (e > value) and e not in state:
                return False
        return True

    def findNextElement(self, state, min):
        for e in range(1, 20):
            if (min is None or e > min) and e not in state:
                return e
        return min

    def goal_test(self, state):
        return self.checkSolution(state, True)

    def partialSolutionIsValid(self, state):
        return self.checkSolution(state, False)

    def checkSolution(self, state, completeCheck):

        if completeCheck and state[-1] == 0:
            return False

        #        /a|b|c\
        #       /d|e|f|g\
        #      /h|i|j|k|l\
        #       \m|n|o|p/
        #        \r|s|t/

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

        # 3 17 18 11 9 14 15 13 10 12 16 19 7 1 6 8 4 2 5

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
print(search.breadth_first_tree_search(nq1).solution())
print("--- %s seconds ---" % (time.time() - start_time))
