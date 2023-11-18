import discEvo as evo
import numpy as np
import NK
import matplotlib.pyplot as plt

###  General parameters
popsize = 100
genesize = 15
recombProb = 0.5
mutatProb = 1/genesize
generations = 100

n = genesize
k = 7

def fitnessFunction(genotype):
    return nklandscape.fitness(genotype)

###  Experiment
demelist = [2,100]
repetitions = 100
avg = np.zeros((2,repetitions,generations))
best = np.zeros((2,repetitions,generations))

for rep in range(repetitions):
    i = 0
    nklandscape = NK.Landscape(n,k)
    for demesize in demelist:
        ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, demesize, generations)
        ga.run()
        avg[i][rep] = ga.avgHistory
        best[i][rep] = ga.bestHistory
        i +=  1

plt.plot(np.mean(avg[0],axis=0),'#1f77b4',label="Local")
plt.plot(np.mean(avg[1],axis=0),'#ff7f0e',label="Global")
plt.plot(np.mean(best[0],axis=0),'#1f77b4')
plt.plot(np.mean(best[1],axis=0),'#ff7f0e')
plt.xlabel("Generations")
plt.ylabel("Fitness (best and avg)")
plt.legend()
plt.show()
