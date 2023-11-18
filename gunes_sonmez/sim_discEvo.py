import discEvo as evo
import numpy as np
import NK
import matplotlib.pyplot as plt

###  General parameters
popsize = 500
genesize = 15
recombProb = 0.5
mutatProb = 0.1
generations = 100

# def fitnessFunction(genotype):
#     return np.sum(genotype)

n = genesize
k = 7
nklandscape = NK.Landscape(n,k)

def fitnessFunction(genotype):
    return nklandscape.fitness(genotype)

###  Microbial test
demeSize = 100
ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, demeSize, generations)
ga.run()
ga.showFitness()
#ga.save("microbialresults")
plt.imshow(ga.fitHistory)
plt.colorbar()
plt.show()

demeSize = 2
ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, demeSize, generations)
ga.run()
ga.showFitness()
#ga.save("microbialresults")
plt.imshow(ga.fitHistory)
plt.colorbar()
plt.show()


###  Generational test
# eliteProp = 0.2
# ga = evo.Generational(fitnessFunction, popsize, genesize, recombProb, mutatProb, eliteProp, generations)
# ga.run()
# ga.showFitness()
#ga.save("generationalresults")
