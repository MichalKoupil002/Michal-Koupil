# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:00:04 2021

@author: misak
"""


import time
import random


your_name = input("Welcome to rock, paper, scissors! Enter Your name:")
time.sleep(1)
print("welcome" + your_name)
time.sleep(1)




rps = input("what's it gonna be? rock, paper or scissors?")    


def main(rps):
        
        list1 = ['rock', 'paper', 'scissors']
        contra = random.choice(list1)
        sitA = contra == list1[0]
        sitB = contra == list1[1]
        sitC = contra == list1[2]
        sitD = rps == list1[0]
        sitE = rps == list1[1]
        sitF = rps == list1[2]


        if rps == contra:
            print("it's a tie")
            
 
        elif sitA & sitE == True:
            print('paper folds rock, you win!')
        
        elif sitA & sitF == True:
            print('rock breaks scissors, you lose')
    
        elif sitB & sitD == True:
            print('paper folds rock, you lose!')
        
        elif sitB & sitF == True:
            print('scissors cut paper, you win!')
    
        elif sitC & sitD == True:
            print('rock breaks scissors, you win!')
    
        elif sitC & sitE == True:
            print('scissors cut paper, you lose!')


main(rps)
        
        

          
        
        