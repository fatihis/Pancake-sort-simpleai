#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import random
import time
from simpleai.search import SearchProblem, breadth_first, depth_first, limited_depth_first, uniform_cost, \
    iterative_limited_depth_first, astar, greedy
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer


my_viewer = BaseViewer()
GOAL = ''
initialString = ''
NumberPancake = input("Enter number of pancakes")
NmbrPnck = int(NumberPancake)

OrderYN = input("Do you want to enter ordering? Y/N")
if OrderYN == 'Y':
    Order = input("Enter order")
    print(Order)
    for x in range(0, NmbrPnck):
        initialString = initialString + str(x)
    shuffledString = Order
if OrderYN == 'N':
    for x in range(0, NmbrPnck):
        initialString = initialString + str(x)
    shuffledString = ''.join(random.sample(initialString, len(initialString)))

start_time = time.time()
GOAL = initialString
print("goal: ", GOAL)
randomArray = []
counter = 0
MaxNumber = NmbrPnck - 1
print(MaxNumber)
expandedNumberOfNodes = 0
while counter < len(GOAL):
    randomArray.append(counter)
    counter = counter + 1


class SortPancake(SearchProblem):
    def actions(self, state):
        if state != GOAL:
            print(randomArray)
            return randomArray
        else:
            return []

    def result(self, state, action):
        res_first = state[0:action]
        res_second = state[action:len(state)]
        res_second_reversed = res_second[::-1]
        state = res_second_reversed + res_first
        print(state)

        return state

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        l: int = len(state) - 1
        lStr = str(l)
        initState = state
        while 0 < l:
            if initState.find(lStr) != l:
                return lStr
            l = l - 1
            lStr = str(l)
        return lStr


problem = SortPancake(initial_state=shuffledString)
result = breadth_first(problem, viewer=WebViewer())
print(result.state)
print(result.path())
print("--- %s seconds ---" % (time.time() - start_time))

"""

resultIterativeLimitedDepth = iterative_limited_depth_first(problem,NmbrPnck)
resultLimitedDepth = limited_depth_first(problem,NmbrPnck)
resultUniformCost = uniform_cost(problem)
print(resultBreadth.state)
print(resultBreadth.path())

print("---------------------------------------------------------------------------")
print(resultBreadth.state)
print("Breadth Path:",resultBreadth.path())

print(resultUniformCost.state)
print(resultUniformCost.path())
print("---------------------------------------------------------------------------")

print(resultIterativeLimitedDepth.state)
print(resultIterativeLimitedDepth.path())
print("---------------------------------------------------------------------------")

print(resultLimitedDepth.state)
print(resultLimitedDepth.path())
print("---------------------------------------------------------------------------")

print(resultUniformCost.state)
print(resultUniformCost.path())
print("---------------------------------------------------------------------------")"""
