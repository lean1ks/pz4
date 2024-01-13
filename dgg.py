#variant 4
from pulp import *
problem1 = LpProblem("LP Problem", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
problem1 += x1 + 2*x2
problem1 += - x1 - 2*x2 -4 <= 0
problem1 += x1 + 2*x2 - 6 <= 0
problem1 += x1 - 2*x2 -4 <= 0 <= 0
problem1.solve()
print("Maximum: ", value(problem1.objective))
print("Opt x ")
for v in problem1.variables():
    print(v.name, "=", value(v))