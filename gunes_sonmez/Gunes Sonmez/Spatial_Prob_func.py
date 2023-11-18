from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def Spatial_Prob(pop_size):

    #values of the normal distribution I will use for probabilities
    mean = 0
    sd = 1

    if pop_size % 2 == 1:
        bin_number = pop_size-1 #how many neighbours except the selected individual
    else:
        bin_number = pop_size-2 # if pop size is even, both the selected individual AND the one opposite to it(aka furthest away) will be discarded.

    step_number = bin_number//2 #basically how many steps can reach the furthest neighbour on each direction.
    bin_size = 6/bin_number #this part is a bit suboptimal and tricky. basically I will use a normal distribution and a
                            #cumulative probability density function (CDF). In the circular spatial distribution,
                            #selected individual can move clockwise or counterclockwise, until reaching the farthest neighbour.
                            #neighbours and distances are symmetrical in both semicircles (clockwise/counterclockwise).
                            #I wanted to create a probabilistic function, in which the prob. of contact with neighbours
                            #decreases in respect to the distance from selected individual. And the sum of all contact prob.= 1.
                            #I used a CDF and created bins of equal size for each neighbour. These bins are representative
                            #of the probability of the agent contacting with the individual in that bin.
                            #since m=0,sd=1 normal distb. approximates to 0 around -3,+3 (I rounded it up), that is
                            #my range for values. Imagine -3/+3 is the farthest point from our selected individual.
                            # To create equal bins in that range, I divided the range with bin_number.


    prob_list = np.zeros(bin_number)  #will contain contact probs. of each bin/neighbour
    step_prob = np.zeros(step_number) #will contain contact probs. of each bin/neighbour, but in one semicircle
    #print(prob_list)

    #this part calculates the cumulative prob. of the bins, using the norm.cdf function. The difference of a starting
    #and ending point of a bin, is the cumulative prob. of that bin's range.
    i = 0
    while i < bin_number:
        prob_list[i] = norm.cdf(-3+((i+1)*bin_size), mean, sd) - norm.cdf(-3+(i*bin_size) ,mean, sd)
        i = i + 1

    #print(prob_list)


    #just converting it to semi-circle to make things easier.
    i = 0
    while i < step_number:
        step_prob[step_number-i-1] = prob_list[i]
        i = i+1

    #print(step_prob)

    return step_prob, prob_list


def Spatial_Prob_Plot (pop_size):

    #plot showing prob. of each bin in one semicircle. as you move away from the starting point,
    #chance of contact gets less and less.
    #the sum of probs = 0.5 since it's one semicircle

    #y_axis = Spatial_Prob(pop_size)[0]
    #x_axis = list(range(1, len(y_axis)+1))

    y_axis = Spatial_Prob(pop_size)[1]
    x_axis = list(range(1, len(y_axis) + 1))


    x_pos = np.arange(len(x_axis))

    # Create bars
    plt.bar(x_pos, y_axis)

    # Create names on the x-axis
    plt.xticks(x_pos, x_axis)

    plt.xlabel("Step")
    plt.ylabel("Probability")

    for i, v in enumerate(x_axis):
        plt.text(x_pos[i] - 0.25, v + 0.01, str(v))

    # Show graphic
    plt.show()

Spatial_Prob_Plot(101)