class Country:
    pass

class Russia(Country):
    def __init__(self):
        self.population = 0
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        return self.population

class Canada(Country):
    def __init__(self):
        self.population = 0
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        return self.population

class Germany(Country):
    def __init__(self):
        self.population = 0
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        return self.population
if __name__ == "__main__":
    russia = Russia()
    canada = Canada()
    germany = Germany()

    russia.setPopulation(146000000)
    canada.setPopulation(40000000)
    germany.setPopulation(84000000)

    print(russia.getPopulation())
    print(canada.getPopulation())
    print(germany.getPopulation())
