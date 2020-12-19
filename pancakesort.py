#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import random
from simpleai.search.viewers import ConsoleViewer
from simpleai.search import SearchProblem, astar,uniform_cost
pancakesInitialState = []
GOAL = []
ActionList = []
my_viewer = ConsoleViewer()




NumberPancake = input("Enter number of pancakes")
NmbrPnck = int(NumberPancake)
OrderYN = input("Do you want to enter ordering? Y/N")
if OrderYN == 'Y':
    OrderYN = input("Enter order, separate by spaces:")
if OrderYN == 'N':
    for x in range(NmbrPnck):
        pancakesInitialState.append(x)
random.shuffle(pancakesInitialState)

initState = map(str, pancakesInitialState)

class PancakeProblem(SearchProblem):
    def actions(self, state):
        NodeList = []
        StateList = []
        for x in state:
            StateList.append(x)

        for x in range(len(StateList)-1):
            List = []

            for y in range(len(StateList)):
                List.append(StateList[y])

            reversedList = []

            for y in range (x,len(List)):
                reversedList.append(List[y])
            reversedList.reverse()

            for y in range(x,len(List)):
                List.pop()

            for y in range(0,len(reversedList)):
                List.append((reversedList[y]))

            NodeList.append(''.join(str(e) for e in List))

        return NodeList

    def result(self, state, action):
        ActionList = action.split(", ")
        randomSelection = random.randint(0, len(ActionList)-1)
        return ActionList[randomSelection]
    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        return max(state)


problem = PancakeProblem(initial_state='43125')
result = uniform_cost(problem)

print(result.state)
print(result.path())
