import random

bestFitnessGeneration = []
averageFitnessGeneration = []
worstFitnessGeneration = []

populationSize = 4
totalQtyAssessments = 20
currentQtyAssessments = 0
percentageMutation = 3

population = []
nextPopulation = []
fitness = [0] * populationSize
fitnessNextPopulation = [0] * (populationSize + 1)
indexBetterSolution = 0
indexWorstSolution = 0

backpackSize = 190
punishment = 15
profitObjects = [50, 50, 64, 46, 50, 5]
weightObjects = [56, 59, 80, 64, 75, 17]
solutionSize = len(profitObjects)


def objectiveFunction(solution):
  fitness = 0
  weight = 0
  for i in range(len(solution)):
    fitness = fitness + (solution[i] * profitObjects[i])
    weight = weight + (solution[i] * weightObjects[i])

  if (weight > backpackSize):
    fitness = fitness - punishment

  return fitness

for i in range (populationSize):
  population.append([0] * solutionSize)
  nextPopulation.append([0] * solutionSize)

nextPopulation.append([0] * solutionSize)

def evaluateSolution(index):
  fitness[index] = objectiveFunction(population[index])

def evaluatePopulation():
  for i in range(populationSize):
    evaluateSolution(i)

def identifyBestSolution():
  indexBetterSolution = 0
  for i in range(populationSize):
    if fitness[indexBetterSolution] < fitness[i]:
        indexBetterSolution = i
  return indexBetterSolution

def elitism():
  indexBetterSolution = identifyBestSolution()
  nextPopulation[populationSize] = population[indexBetterSolution]
  fitnessNextPopulation[populationSize] = fitness[indexBetterSolution]

def mutation(index):
  for i in range(solutionSize):
    if random.randint(0, 100) <= percentageMutation:
      if population[index][i] == 0:
        nextPopulation[index][i] = 1
      else:
        nextPopulation[index][i] = 0
    else:
      nextPopulation[index][i] = population[index][i]

def identifyWorstSolutionNextPopulation():
  indexWorstSolution = 0
  for i in range(populationSize+1):
    if fitnessNextPopulation[indexWorstSolution] > fitnessNextPopulation[i]:
      indexWorstSolution = i
  return indexWorstSolution

def generateInitSolution():
  for i in range(populationSize):
    for j in range(solutionSize):
      population[i][j] = random.randint(0, 1)

def identifyWorstSolutionCurrentPopulation():
  indexWorstSolution = 0
  for i in range(populationSize):
    if fitness[indexWorstSolution] > fitness[i]:
      indexWorstSolution = i
  return indexWorstSolution

def generateNextPopulation():
  worst = identifyWorstSolutionNextPopulation()
  del nextPopulation[worst]
  del fitnessNextPopulation[worst]

  population = nextPopulation
  fitness = fitnessNextPopulation

  nextPopulation.append(nextPopulation[0])
  fitnessNextPopulation.append(fitnessNextPopulation[0])

def stopCriterionReached(currentQtyAssessments):
  return currentQtyAssessments >= totalQtyAssessments

def reportConvergenceGeneration():
  bestFitnessGeneration.append(fitness[identifyBestSolution()])
  worstFitnessGeneration.append(fitness[identifyWorstSolutionCurrentPopulation()])
  average = 0
  for i in fitness:
    average = average+i
  averageFitnessGeneration.append(average/len(fitness))

def runAlgoritm():
  generateInitSolution()
  evaluatePopulation()
  currentQtyAssessments = populationSize
  reportConvergenceGeneration()
  count = 0
  while not stopCriterionReached(currentQtyAssessments):
    elitism()
    for i in range(populationSize):
      mutation(i)
      fitnessNextPopulation[i] = objectiveFunction(nextPopulation[i])
      currentQtyAssessments = currentQtyAssessments + 1
    generateNextPopulation()
    reportConvergenceGeneration()
    count = count + 1

  print("Melhor indivíduo:")
  bestEnd = identifyBestSolution()
  print(population[bestEnd])
  print("Fitness =", fitness[bestEnd])
  print("")

# RODANDO 30 VEZES O ALGORITMO
do = 30
while do >= 0:
  runAlgoritm()
  do = do - 1