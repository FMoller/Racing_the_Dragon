"""
Collatz conjecture
https://github.com/FMoller/Racing_the_Dragon
"""

__author__ = 'Frederico Moeller'

import time
import numpy as np

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

def i_collatz2(n,c_list):
    while(n>1):
        c_list.append(n)
        if n%2==1:
            n=3*n+1
            c_list.append(n)
        n=n/2
    c_list.append(n)

test_val = np.array([744, 340, 480, 679, 227, 996, 984, 753, 931, 679, 325, 939, 153,
       529, 535, 914, 804, 746, 453,  58, 668, 406, 217, 254, 830, 530,
       867, 983, 149, 306, 852, 398, 229, 736,   9, 406, 184, 377, 322,
       367, 960, 583, 355, 534, 980, 906, 474, 921, 895, 504, 586, 281,
        32, 371, 866, 172, 478, 906, 844, 140])

rcltz = []
rcltz2 = []
icltz = []
icltz2 = []

for i in test_val:
    c_list = []
    st_time = time.perf_counter()
    rcltz.append(r_collatz(i,c_list))
    ed_time = time.perf_counter()
    rcltz.append(ed_time - st_time)
    
    
    
        

    
