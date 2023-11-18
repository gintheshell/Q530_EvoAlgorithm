import numpy as np
import matplotlib.pyplot as plt
""""
def probSel (a, popsize):
        if self.popsize % 2 == 1:
            bin_number = self.popsize - 1  # how many neighbours except the selected individual
        else:
            bin_number = self.popsize - 2  # if pop size is even, both the selected individual AND the one opposite to it(aka furthest away) will be discarded.

        step_number = bin_number // 2  # basically how many steps can reach the furthest neighbour on each direction.
        bin_size = 6 / bin_number

        # select the other individual probabilistically

        x = np.random.normal(0.0, 1.0, 1)

        if x >= 0:
            dir = 1
        else:
            dir = -1

        i = 1
        while i < step_number:
            if (i * (bin_size)) <= (x * dir):
                i = i + 1
            else:
                step = i
                break

        b = (a + step) % popsize

        return b

"""

class Microbial():

    def __init__(self, fitnessFunction, popsize, genesize, recombProb, mutatProb, spatial, generations):
        self.fitnessFunction = fitnessFunction
        self.popsize = popsize
        self.genesize = genesize
        self.recombProb = recombProb
        self.mutatProb = mutatProb
        self.spatial = spatial
        self.generations = generations
        self.tournaments = generations*popsize
        self.pop = np.random.rand(popsize,genesize)*2 - 1
        self.fitness = np.zeros(popsize)
        self.avgHistory = np.zeros(generations)
        self.bestHistory = np.zeros(generations)
        self.gen = 0


    def showFitness(self):
        plt.plot(self.bestHistory)
        plt.plot(self.avgHistory)
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.title("Best and average fitness")
        plt.show()

    def fitStats(self):
        bestind = self.pop[np.argmax(self.fitness)]
        bestfit = np.max(self.fitness)
        avgfit = np.mean(self.fitness)
        self.avgHistory[self.gen]=avgfit
        self.bestHistory[self.gen]=bestfit
        return avgfit, bestfit, bestind

    def save(self,filename):
        af,bf,bi = self.fitStats()
        np.savez(filename, avghist=self.avgHistory, besthist=self.bestHistory, bestind=bi)

    def run(self):
        # Calculate all fitness once
        for i in range(self.popsize):
            self.fitness[i] = self.fitnessFunction(self.pop[i])
        # Evolutionary loop
        for g in range(self.generations):
            self.gen = g
            # Report statistics every generatiprint((y*dir))on
            self.fitStats()
            for i in range(self.popsize):

                # Step 1: Pick 2 individuals
                a = np.random.randint(0,self.popsize-1)

                if self.spatial == 0:
                    b = np.random.randint(self.popsize)
                    while (a == b):  # Make sure they are two different individuals
                        b = np.random.randint(self.popsize)
                else:
                    if self.popsize % 2 == 1:
                        bin_number = self.popsize - 1  # how many neighbours except the selected individual
                    else:
                        bin_number = self.popsize - 2  # if pop size is even, both the selected individual AND the one opposite to it(aka furthest away) will be discarded.

                    step_number = bin_number // 2  # basically how many steps can reach the furthest neighbour in each direction.
                    bin_size = 6 / bin_number   # normal function (m=0,sd=1) approximates to 0 around -3,+3 , so the area under the curve
                                                # between the curve in that range =1 (total prob.). Hence my range is = 6.
                                                #I need to divide that range to bin number to get equal sized bins.
                                                #changing dist. function, will change the range.

                    # select the other individual probabilistically

                    x = np.random.normal(0.0, 1.0, 1)

                    if x >= 0:  #clockwise or counter clockwise
                        dir = 1
                    else:
                        dir = -1

                    i = 1
                    while i < step_number:
                        if (i * (bin_size)) <= (x * dir):
                            i = i + 1
                        else:
                            step = i
                            break

                    b = (a + step) % self.popsize




                # Step 2: Compare their fitness
                if (self.fitness[a] > self.fitness[b]):
                    winner = a
                    loser = b
                else:
                    winner = b
                    loser = a

                # Step 3: Transfect loser with winner --- Could be made more efficient using Numpy
                for l in range(self.genesize):
                    if (np.random.random() < self.recombProb):
                        self.pop[loser][l] = self.pop[winner][l]

                # Step 4: Mutate loser and make sure new organism stays within bounds
                self.pop[loser] += np.random.normal(0.0,self.mutatProb,size=self.genesize)
                self.pop[loser] = np.clip(self.pop[loser],-1,1)
                # Save fitness
                self.fitness[loser] = self.fitnessFunction(self.pop[loser])
