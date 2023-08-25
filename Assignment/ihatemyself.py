import random

n = int(input())
weights = list(map(int, input().split()))

# Function to calculate the difference in weight between two piles
def weight_difference(pile1, pile2):
    return abs(sum(pile1) - sum(pile2))

# Function to initialize a random chromosome (representing a potential solution)
def random_chromosome(num_stones):
    return random.choices([0, 1], k=num_stones)

# Function to perform crossover between two parent chromosomes
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation on a chromosome
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

# Function to evaluate the fitness of a chromosome
def fitness(chromosome, stone_weights):
    pile1 = [stone_weights[i] for i in range(len(chromosome)) if chromosome[i] == 1]
    pile2 = [stone_weights[i] for i in range(len(chromosome)) if chromosome[i] == 0]
    return weight_difference(pile1, pile2)

# Genetic Algorithm implementation
def genetic_algorithm(stone_weights, population_size=100, generations=1000, mutation_rate=0.01):
    num_stones = n
    population = [random_chromosome(num_stones) for _ in range(population_size)]

    for _ in range(generations):
        # Evaluate the fitness of each chromosome
        fitness_values = [fitness(chromosome, stone_weights) for chromosome in population]
        min_fitness = min(fitness_values)

        # Check for early stopping
        if min_fitness == 0:
            return min_fitness

        # Select parents for crossover using tournament selection
        parents = []
        for _ in range(population_size // 2):
            tournament_size = min(5, population_size)
            tournament = random.sample(range(population_size), tournament_size)
            parent1 = tournament[0]
            for challenger in tournament:
                if fitness_values[challenger] < fitness_values[parent1]:
                    parent1 = challenger
            parent2 = random.choice(tournament)
            while parent2 == parent1:
                parent2 = random.choice(tournament)
            parents.append((parent1, parent2))

        # Perform crossover and mutation to create new generation
        new_population = []
        for parent1, parent2 in parents:
            child1, child2 = crossover(population[parent1], population[parent2])
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    # Find the best solution in the final population
    fitness_values = [fitness(chromosome, stone_weights) for chromosome in population]
    return min(fitness_values)

result = genetic_algorithm(weights)
print(result)
