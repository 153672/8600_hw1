__author__ = 'Mart Aarma'

import search

class MagicHexagonProblem(search.Problem):
    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of None means that the c-th column has not been
    filled in yet.  We fill in columns left to right.
    >>> depth_first_tree_search(MagicHexagonProblem(8))
    <Node [7, 3, 0, 2, 5, 1, 6, 4]>
    """
    def __init__(self):
        self.N = 19
        self.initial = [0] * self.N
        self.initial[0] = 1

    def actions(self, state):
        index = state.index(0)
        currentValue = state[index - 1]
        if self.partialSolutionIsValid(state):
            return ["startNext"]
        else:
            if self.valueIsMaxAvailValue(state, currentValue):
                return ["incPrevVal"]
            else:
                return ["incCurrVal"]

    def result(self, state, action):
        print(state)
        index = state.index(0)
        currentIndex = index - 1;
        if action == "startNext":
            state[index] = self.findNextElement(state, None)
        elif action == "incCurrVal":
            state[currentIndex] =  self.findNextElement(state, state[currentIndex])
        else:
            state[index - 2] = self.getMinElement(state)
            state[currentIndex] = self.getMinElement(state)
        print(state)
        print("\n----------")
        return state


    def valueIsMaxAvailValue(self, state, value):
         for e in range(self.N + 1):
             if e not in state and (e > value):
                 return False
         return True

    def getMinElement(self, state):
         for e in range(self.N + 1):
             if e not in state:
                 return e
         return -1

    def findNextElement(self, state, min):
         for e in range(self.N + 1):
             if e not in state and (min is None or e > min):
                 return e
         return min

    def goal_test(self, state):
        if state[-1] == 0:
            return self.checkSolution(state, True)
        return self.checkSolution(state, False)

    def partialSolutionIsValid(self, state):
        return self.checkSolution(state, False)

    def checkSolution(self, state, completeCheck):
#        /a|b|c\
#       /d|e|f|g\
#      /h|i|j|k|l\
#       \m|n|o|p/
#        \r|s|t/

        a=state[0];
        b=state[1];
        c=state[2];
        g=state[3];
        l=state[4];
        p=state[5];
        t=state[6];
        s=state[7];
        r=state[8];
        m=state[9];
        h=state[10];
        d=state[11];
        e=state[12];
        f=state[13];
        k=state[14];
        o=state[15];
        n=state[16];
        i=state[17];
        j=state[18];

        if completeCheck and state[-1] == 0:
            return False

        if self.checkVariables3(a,b,c,completeCheck):
            if self.checkVariables4(d,e,f,g,completeCheck):
                if self.checkVariables5(h,i,j,k,l,completeCheck):
                    if self.checkVariables4(m,n,o,p,completeCheck):
                        if self.checkVariables3(r,s,t,completeCheck):
                            if self.checkVariables3(a,d,h,completeCheck):
                                if self.checkVariables4(b,e,i,m,completeCheck):
                                    if self.checkVariables5(c,f,j,n,r,completeCheck):
                                        if self.checkVariables4(g,k,o,s,completeCheck):
                                            if self.checkVariables3(l,p,t,completeCheck):
                                                if self.checkVariables3(c,g,l,completeCheck):
                                                    if self.checkVariables4(b,f,k,p,completeCheck):
                                                        if self.checkVariables5(a,e,j,o,t,completeCheck):
                                                            if self.checkVariables4(d,i,n,s,completeCheck):
                                                                if self.checkVariables3(h , m , r,completeCheck):
                                                                    print("true: ", state)
                                                                    return True;
        print("false: ", state)
        return False

    def checkVariables3(self, a,b,c, completeCheck):
        if (a == 0 or b == 0 or c == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c == 38:
            return True
        return False;

    def checkVariables4(self,a,b,c,d, completeCheck):
        if (a == 0 or b == 0 or c == 0 or d == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c + d == 38:
            return True
        return False;

    def checkVariables5(self,a,b,c,d,e, completeCheck):
        if (a == 0 or b == 0 or c == 0 or d == 0 or e == 0):
            if completeCheck:
                return False
            else:
                return True

        if a + b + c + d + e == 38:
            return True
        return False;
                                                                








nq = search.NQueensProblem(8);
nq1 = MagicHexagonProblem();
print(search.breadth_first_tree_search(nq1).solution())




# 22. sept on esitamise aeg. 09.09.15 on moodlis yleval kus gruppi sind pandi. tulemused esitada githubi