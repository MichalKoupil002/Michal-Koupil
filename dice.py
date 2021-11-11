# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:14:43 2021

@author: misak
"""
import random

class Dice():
    def roll(self):
        x = random.randint(1,6)
        return(x)
    
d = Dice()
d.roll()

        
    