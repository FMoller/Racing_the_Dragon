"""
Collatz conjecture
https://github.com/FMoller/Racing_the_Dragon
"""

__author__ = 'Frederico Moeller'

def r_collatz(n,c_list):
    c_list.append(n)
    if n>1:
        if n%2==0:
            r_collatz(n/2,c_list)
        else:
            r_collatz(3*n+1,c_list)

    
