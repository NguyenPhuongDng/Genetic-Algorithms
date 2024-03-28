import random
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(route, cities):
    distance = 0
    for i in range(len(route)-1):
        distance += euclidean_distance(cities[route[i]], cities[route[i+1]])
    distance += euclidean_distance(cities[route[-1]], cities[route[0]])  # return to the starting city
    return distance

def generate_initial_population(n, cities):
    population = []
    for _ in range(n):
        route = list(range(len(cities)))
        random.shuffle(route)
        population.append(route)
    return population

def selection(population, cities):
    population.sort(key=lambda x: total_distance(x, cities))
    return population[:len(population)//2]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1)-1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

def mutation(route):
    index1, index2 = random.sample(range(len(route)), 2)
    route[index1], route[index2] = route[index2], route[index1]
    return route

def genetic_algorithm(cities, population_size, generations):
    population = generate_initial_population(population_size, cities)
    for _ in range(generations):
        population = selection(population, cities)
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_route = min(population, key=lambda x: total_distance(x, cities))
    best_distance = total_distance(best_route, cities)
    return best_distance, best_route

if __name__ == "__main__":
    n = int(input("input number of cities: "))
    cities_data = []
    for i in range(n):
        city = tuple(int(x) for x in input().split())
        cities_data.append(city)

    population_size = len(cities_data)*10
    generations = population_size*10
    
    best_distance, best_route = genetic_algorithm(cities_data, population_size, generations)
    print("Best route:", best_route)
    print("Best distance:", best_distance)
