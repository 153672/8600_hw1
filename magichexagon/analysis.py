__author__ = 'Mart Aarma'

import search
import time
import inspect
import math


class InstrumentedProblem(search.Problem):
    """Delegates to a problem, and keeps statistics."""

    def __init__(self, problem):
        self.problem = problem
        self.succs = self.goal_tests = self.states = self.minh = self.maxh = self.unsuccs = 0
        self.found = None
        self.start_time = time.time()

    def actions(self, state):
        a = self.problem.actions(state)
        l = len(a)
        if l == 0:
            self.unsuccs += 1
        else:
            self.succs += l

        return a

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
        h = self.problem.h(node)
        if h <= 190:
            self.minh += 1
        else:
            self.maxh += 1
        return h

    def path_cost(self, c, state1, action, state2):
        return self.problem.path_cost(c, state1, action, state2)

    def value(self, state):
        return self.problem.value(state)

    def __getattr__(self, attr):
        return getattr(self.problem, attr)

    def set_end_time(self, end_time):
        self.end_time = end_time

    def __repr__(self):
        return '<a:%4d / ua:%4d / g:%4d / h:%d:%d (%2.4f%%) / s: %s / t: %s s>' % (self.succs, self.unsuccs, self.goal_tests,
                                                                 self.minh, self.maxh, (self.minh / (max(1, self.maxh) * 1.0)), str(self.found)[:67],
                                                                 (self.end_time - self.start_time))


def compare_searchers(problems):

    searchers=[search.depth_first_tree_search,
               search.depth_limited_search,
               search.depth_first_graph_search,
               search.breadth_first_tree_search,
               search.recursive_best_first_search]


    print("----- Start comparison")
    print("a = total nr. of successful actions")
    print("ua =          of unsuccessful actions (when action() returns [])")
    print("g =           of goal tests")
    print("hmin:hmax = nr. good states vs. bad states ")
    print("s = solution")
    print("t = solving time \n\n")

    def do(searcher, problem):
        p = InstrumentedProblem(problem)
        argspec = inspect.getargspec(searcher)
        if len(argspec.args) == 1:
            searcher(p)
        else:
            searcher(p, p.h)

        p.set_end_time(time.time())
        return p

    table = [[search.name(s)] + [do(s, problems[0])] for s in searchers]
    search.print_table(table, ["Searcher", "Result"])
    print("")
    table = [[search.name(s)] + [do(s, problems[1])] for s in searchers]
    search.print_table(table, ["Searcher", "Result with reverse number selection list"])
