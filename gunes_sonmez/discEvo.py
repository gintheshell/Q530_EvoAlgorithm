import numpy as np
import matplotlib.pyplot as plt

class Microbial():

    def __init__(self, fitnessFunction, popsize, genesize, recombProb, mutatProb, demeSize, generations):
        self.fitnessFunction = fitnessFunction
        self.popsize = popsize
        self.genesize = genesize
        self.recombProb = recombProb
        self.mutatProb = mutatProb
        self.demeSize = int(demeSize/2)
        self.generations = generations
        self.tournaments = generations*popsize
        self.pop = np.random.randint(2, size=(popsize,genesize))
        self.fitness = np.zeros(popsize)
        self.avgHistory = np.zeros(generations)
        self.bestHistory = np.zeros(generations)
        self.fitHistory = np.zeros((generations,popsize))
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
        self.fitHistory[self.gen]=self.fitness
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
            # Report statistics every generation
            self.fitStats()
            for i in range(self.popsize):
                # Step 1: Pick 2 individuals
                a = np.random.randint(0,self.popsize-1)
                b = np.random.randint(a-self.demeSize,a+self.demeSize-1)%self.popsize   ### Restrict to demes
                while (a==b):   # Make sure they are two different individuals
                    b = np.random.randint(a-self.demeSize,a+self.demeSize-1)%self.popsize   ### Restrict to demes
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
                for l in range(self.genesize):
                    if (np.random.random() < self.mutatProb):
                        self.pop[loser][l] = np.random.randint(2)
                # Save fitness
                self.fitness[loser] = self.fitnessFunction(self.pop[loser])

class Generational():

    def __init__(self, fitnessFunction, popsize, genesize, recombProb, mutatProb, eliteprop, generations):
        self.fitnessFunction = fitnessFunction
        self.popsize = popsize
        self.genesize = genesize
        self.recombProb = recombProb
        self.mutatProb = mutatProb
        self.elite = int(eliteprop*popsize)
        self.generations = generations
        self.pop = np.random.randint(2, size=(popsize,genesize))
        self.fitness = np.zeros(popsize)
        self.rank = np.zeros(popsize,dtype=int)
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

            # Report statistics every generation
            self.gen = g
            self.fitStats()

            # Rank individuals by fitness
            tempfitness = self.fitness.copy()
            for i in range(self.popsize):
                self.rank[i]=int(np.argmax(tempfitness))
                tempfitness[self.rank[i]]=0.0

            # Start new generation
            new_pop = np.zeros((self.popsize,self.genesize))
            new_fitness = np.zeros(self.popsize)

            # Fill out the elite first
            for i in range(self.elite):
                new_pop[i] = self.pop[self.rank[i]]
                new_fitness[i] = self.fitness[self.rank[i]]

            # Fill out remainder of the population through reproduction of most fit parents
            for i in range(self.elite,self.popsize):
                # Pick parents based on rank probability
                a = self.rank[int(np.random.triangular(0, 0, self.popsize))]
                b = self.rank[int(np.random.triangular(0, 0, self.popsize))]
                while (a==b):           # Make sure they are two different individuals
                    b = self.rank[int(np.random.triangular(0, 0, self.popsize))]

                # Recombine parents to produce child
                for k in range(self.genesize):
                    if np.random.random() < self.recombProb:
                        new_pop[i][k] = self.pop[a][k]
                    else:
                        new_pop[i][k] = self.pop[b][k]

                # Mutate child and make sure they stay within bounds
                for k in range(self.genesize):
                    if (np.random.random() < self.mutatProb):
                        self.pop[i][k] = np.random.randint(2)

                # Recalculate their fitness
                new_fitness[i] = self.fitnessFunction(new_pop[i])

            # Finally replace old population with the new one
            self.pop = new_pop.copy()
            self.fitness = new_fitness.copy()
