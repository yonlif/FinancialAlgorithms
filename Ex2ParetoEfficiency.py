"""
Find a fair division which is pareto efficient and envy-free, using cvxpy.
"""

import cvxpy
from cvxpy import log
from random import randrange

# Resources
m = 4
# People
n = 3

print(f"{n} people and {m} types of resources.")

# Define the resource value matrix
# valueMatrix = [[randrange(100) for _ in range(m)] for _ in range(n)]
valueMatrix = [[19, 0, 0, 81], [0, 20, 0, 80], [0, 0, 40, 60]]

print("\nValue matrix:")
print('\n'.join([', '.join([str(item) for item in row]) for row in valueMatrix]))

# Create a matrix with variables which will be the precent each agent gets
varMatrix = [[cvxpy.Variable() for _ in range(m)] for _ in range(n)]

# Create constrains
sumConstraints = [(sum(item for item in row) == 1) for row in zip(*varMatrix)]
upperBoundConstraints = [item <= 1 for row in varMatrix for item in row]
lowerBoundConstraints = [0 <= item for row in varMatrix for item in row]
boundConstraints = lowerBoundConstraints + upperBoundConstraints
constraints = boundConstraints + sumConstraints

# Up-going function
f = lambda x: log(x)

# Create the expression we will try to maximize
objectiveExpression = sum(f(sum(value * var for value, var in zip(valueRow, varRow)))
                          for valueRow, varRow in zip(valueMatrix, varMatrix))

# Define the problem and solve it
prob = cvxpy.Problem(
    objective   =  cvxpy.Maximize(objectiveExpression),
    constraints = constraints)
prob.solve()

# Print result
print("\nSolution:")
print("Status:", prob.status)
print("Optimal value:", prob.value)

for agentIdx, agent in enumerate(varMatrix):
    print(f"Agent #{agentIdx + 1} gets: " +
          ', '.join([f"{var.value:.5f} of resource #{idx + 1}" for idx, var in enumerate(agent)]) + ".")
