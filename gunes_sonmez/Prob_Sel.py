from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np



if pop_size % 2 == 1:
    bin_number = pop_size - 1  # how many neighbours except the selected individual
else:
    bin_number = pop_size - 2  # if pop size is even, both the selected individual AND the one opposite to it(aka furthest away) will be discarded.

step_number = bin_number // 2  # basically how many steps can reach the furthest neighbour on each direction.
bin_size = 6 / bin_number


x = np.random.normal(0.0, 1.0, 1)
selected_1 =

def prob_selection(x, ):
    if x>= 0:
        dir = 1
    else:
        dir= -1

        i=1
        while i < step_number:
             if  (i*(bin_size)) <= (x*dir):
                 i= i+1
            else:
                y=i
                break

    return y








