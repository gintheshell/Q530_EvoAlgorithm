from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
mean = 0
sd = 1
x = norm.cdf(0, mean, sd) - norm.cdf(-3, mean, sd)

print(x)

pop_size = 11
bin_number = pop_size-1
step_number = bin_number//2
bin_size = 6/bin_number
prob_list = np.zeros(bin_number)
step_prob = np.zeros(step_number)
print(prob_list)



i=0
while i < bin_number:
    prob_list[i] = norm.cdf(-3+((i+1)*bin_size), mean, sd) - norm.cdf(-3+(i*bin_size) ,mean, sd)
    i = i + 1


print(prob_list)

i = 0

while i < step_number:
    step_prob[step_number-i-1] = prob_list[i]
    i = i+1

print(step_prob)

step_list = np.array(range(1, step_number+1))


labels = list(range(1,len(step_prob)+1))
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x , step_prob, width)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Probability')
ax.set_xlabel('Neighbour')
ax.set_title('Probability of selecting Neighbour')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)


fig.tight_layout()

plt.show()