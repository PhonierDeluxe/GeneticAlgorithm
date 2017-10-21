import random

individuals = 20 #p
crossoverReplaced = individuals/2 #r
mutationRate = 0 #m
population = [] #P
newGeneration = [] #Ps

maxFitness = 0
fitnessThreshold = 0
optimum = 100

def selectIndividual():
    randNum = random.uniform(0,1)
    sum = 0
    index = random.randint(0,individuals)
    index
    while sum < randNum:
        index += 1
        index = index % individuals
        #sum +=

def randomGenes(individuals,optimum):

    genes = [""]*individuals
    for i in range(individuals):
        number = random.randint(0, 256)
        genes[i] = "{0:08b}".format(number)
        print(genes[i])
    return genes

def selection():
    for i in range((1-crossoverReplaced)*individuals):
        pass

if __name__ == '__main__':
    population = randomGenes(individuals,optimum)

    while maxFitness < fitnessThreshold:
        pass