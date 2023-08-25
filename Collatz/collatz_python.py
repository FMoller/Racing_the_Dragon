"""
Collatz conjecture
https://github.com/FMoller/Racing_the_Dragon
"""

__author__ = 'Frederico Moeller'

import time
import numpy as np
import pandas as pd
import sys
from timeit import default_timer as timer
import datetime

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

def i_collatz_2(n,c_list):
    while(n>1):
        c_list.append(n)
        if n%2==1:
            n=3*n+1
            c_list.append(n)
        n=n/2
    c_list.append(n)

"""
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
 """

def main():
    """
    arg1 = csv file with the data
    arg2 = function type:
        1 - r_collatz_2
        2 - i_collatz
        3 - i_collatz_2
        default - r_collatz
    arg3 = log_dir
    arg4 = output_times
    """
    args = sys.argv
    #print(args)
    if (len(args)>2):
        print(args)
        bcmk = pd.read_csv(args[1],header = None)
        q_rows = len(bcmk)
        bcmk_times = []
        bcmk_sol = dict()
        start = timer()
        end = timer()
        log_text = str(datetime.datetime.now()) + '\n' + str(args) + '\n\n'
        out_times = 'python,' + datetime.datetime.now().strftime('%Y.%m.%d')+','+str(timer())+','+args[2]
        for i in range(q_rows):   
            row = bcmk.loc[i,:]
            total_row_time = 0
            for j in range(len(row)):
                collatz_list = []
                if int(args[2]) == 1:
                    start = timer()
                    r_collatz_2(row[j],collatz_list)
                    end = timer()
                    total_row_time += (end-start)
                elif int(args[2]) == 1:
                    start = timer()
                    i_collatz(row[j],collatz_list)
                    end = timer()
                    total_row_time += (end-start)
                elif int(args[2]) == 1:
                    start = timer()
                    i_collatz_2(row[j],collatz_list)
                    end = timer()
                    total_row_time += (end-start)
                else:
                    start = timer()
                    r_collatz(row[j],collatz_list)
                    end = timer()
                    total_row_time += (end-start)
                bcmk_sol[row[j]] = collatz_list
            bcmk_times.append(total_row_time)
        log_text += 'bcmk_times: \n' + str(bcmk_times) + '\n\n'
        log_text += 'results: \b' + str(bcmk_sol)
        fname = args[3] + 'python_collatz_'+str(int(time.time()))+'.txt'
        f = open(fname,'a')
        f.write(log_text)
        f.close()
        for i in bcmk_times:
            out_times += ',' + str(i)
        out_times += '\n'
        gname = args[4] + args[1][:args[1].find('.')]+'_times.csv'
        g = open(gname,'a')
        g.write(out_times)
        g.close()
                    
    else:
        pass
    #print(bcmk_sol)
    #print(bcmk_times)


if __name__ == "__main__":
        main()
    
    
        

    
