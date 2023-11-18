import realEvo as evo
import numpy as np

###  General parameters
popsize = 100
genesize = 5
recombProb = 0.5
mutatProb = 0.1
generations = 100

def fitnessFunction(genotype):
    return np.sum(genotype)

###  Microbial test
demeSize = 2
ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, demeSize, generations)
ga.run()
ga.showFitness()
ga.save("microbialresults")

###  Generational test
eliteProp = 0.2
ga = evo.Generational(fitnessFunction, popsize, genesize, recombProb, mutatProb, eliteProp, generations)
ga.run()
ga.showFitness()
ga.save("generationalresults")
