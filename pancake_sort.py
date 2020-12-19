#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import random
from simpleai.search import SearchProblem, depth_first



int_list = []
goal_list = []
tuple(int_list)
counter = 0
NumberPancake = input("Enter number of pancakes")
NmbrPnck = int(NumberPancake)
OrderYN = input("Do you want to enter ordering? Y/N")
if OrderYN == 'Y':
    OrderYN = input("Enter order, separate by spaces:")
if OrderYN == 'N':
    for x in range(NmbrPnck):
        int_list.append(x)
random.shuffle(int_list)

randomizedString = ''

randomizedString.join(int_list)
print('liste bu', int_list)


for x in range(NmbrPnck):
    goal_list.append(x)
GOAL = tuple(goal_list)
temppMax = max(int_list)


def flip(liste, element):
    lst = list(liste)
    cut_index = lst.index(element)
    cut_index = cut_index + 1
    l2 = lst[:cut_index]
    l3 = lst[cut_index:]
    l2.reverse()
    for x in l3: l2.append(x)
    print(l2, "l2son")
    liste = tuple(l2)


print(GOAL, 'goal')


class PancakeProblem(SearchProblem):
    def actions(self, state):
        init_array = state
        if temppMax == init_array.index(temppMax) - 1:
            --temppMax
        elif temppMax != init_array.index(temppMax) - 1:
            if init_array.index(temppMax) != 0: flip(init_array, temppMax)
            if init_array.index(temppMax) == 0:
                flip(init_array, temppMax)
                --temppMax
        return init_array

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        return 2


problem = PancakeProblem(initial_state=tuple(int_list))
result = depth_first(problem)
print(result.state)
print(result.path())
