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


def r_collatz_2(n,c_list):
    c_list.append(n)
    if n>1:
        if n%2==1:
            n = 3*n+1
            c_list.append(n)
        r_collatz(n/2,c_list)

def i_collatz(n,c_list):
    while(n>1):
        c_list.append(n)
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    c_list.append(n)

    
        
        

    
