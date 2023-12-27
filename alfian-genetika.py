import random

OPTIMAL     = "Kalijaga Muda Alfian Informatika 2022 Kecerdasan Buatan Kelas B"
DNA_SIZE    = len(OPTIMAL)
POP_SIZE    = 150
GENERATIONS = 20000

def weighted_choice(items):

    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
        if n < weight:
            return item
        n = n - weight
    return item

def random_char():
    return chr(int(random.randrange(32 , 126, 1)))

def random_population():
    pop = []
    for i in range(POP_SIZE):
        dna = ""
        for c in range(DNA_SIZE):
            dna += random_char()
        pop.append(dna)
    return pop

def fitness(dna):
    fitness = 0
    for c in range(DNA_SIZE):
        fitness += abs(ord(dna[c]) - ord(OPTIMAL[c]))
    return fitness

def mutate(dna):
    dna_out = ""
    mutation_chance = 100
    for c in range(DNA_SIZE):
        if int(random.random()*mutation_chance) == 1:
            dna_out += random_char()
        else:
            dna_out += dna[c]
    return dna_out

def crossover(dna1, dna2):
    pos = int(random.random()*DNA_SIZE)
    return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])

population = random_population()

for generation in range(GENERATIONS):
    print("Generation #%s" % generation)
    weighted_population = []

    for individual in population:
        fitness_val = fitness(individual)

        if fitness_val == 0:
            pair = (individual, 1.0)
        else:
            pair = (individual, 1.0/fitness_val)

        weighted_population.append(pair)

    population = []

    for _ in range(int(POP_SIZE/2)):
        ind1 = weighted_choice(weighted_population)
        ind2 = weighted_choice(weighted_population)

        ind1, ind2 = crossover(ind1, ind2)

        population.append(mutate(ind1))
        population.append(mutate(ind2))

    fittest_string = population[0]
    minimum_fitness = fitness(population[0])

    for individual in population:
        ind_fitness = fitness(individual)
        if ind_fitness <= minimum_fitness:
            fittest_string = individual
            minimum_fitness = ind_fitness

    print("Fittest String: %s with Fitness value: %s" % (fittest_string, minimum_fitness))
    if minimum_fitness == 0:break