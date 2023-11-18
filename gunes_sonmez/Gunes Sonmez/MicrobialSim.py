import Microbial as evo
import DemesMicrobial as demeevo
import numpy as np

###  General parameters
popsize = 11
genesize = 5
recombProb = 0.7
mutatProb = 0.1
generations = 50

def fitnessFunction(genotype):
    return np.sum(genotype)


###  Microbial test
spatial = 1
ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, spatial, generations)
ga.run()
ga.showFitness()
ga.save("microbialresults")

demeSize = 2
ga = demeevo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, demeSize , generations)
ga.run()
ga.showFitness()
ga.save("microbial_demes_results")

###  Microbial test
spatial = 0
ga = evo.Microbial(fitnessFunction, popsize, genesize, recombProb, mutatProb, spatial, generations)
ga.run()
ga.showFitness()
ga.save("microbialresults")