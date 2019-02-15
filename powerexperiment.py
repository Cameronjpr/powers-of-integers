#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:21:11 2019

@author: cameron.robson
"""
def numberGrammar(numberGrammarToken):
    if numberGrammarToken == 2:
        return "The 2nd power of "
    elif numberGrammarToken == 3:
        return "The 3rd power of "
    elif numberGrammarToken >= 4:
        return ("The " + str(numberGrammarToken) + "th power of ")
    
def listPowersOfIntsUpTo(int):
    listOfPowersToReturn = list()
    for num in range(int):
        if num < 2:
            num = 2
        else:
            print("\nbase is " + str(num))
            index = 2
            while index < 6:
                ng = numberGrammar(index)
                print(str(ng) + str(num) + " is " + str((num ** index)))
                listOfPowersToReturn.append(num ** index)
                index += 1
    return listOfPowersToReturn


listPowersOfIntsUpTo(101)


