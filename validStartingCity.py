def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)

    for startCityIdx in range(numberOfCities):
        milesRemaining = 0

        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
            if milesRemaining < 0:
                continue

            currentCityIdx = currentCityIdx % numberOfCities

            fuelFromCurrentCity = fuel[currentCityIdx]
            distanceToNextCity = distances[currentCityIdx]
            milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity

        if milesRemaining >= 0:
            return startCityIdx

    return -1



distances = [5, 25, 15, 10, 15]
fuel = [1,2,1,0,3]
mpg = 10

print(validStartingCity(distances, fuel, mpg))
