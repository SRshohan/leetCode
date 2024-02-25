def assignBikes(workers, bikes):
    def findDistance(workerLocation, bikesLocation):
        return abs(workerLocation[0] - bikesLocation[0]) + abs(workerLocation[1] - bikesLocation[1])

    all_triplets = []

    for workerIndex, workerLoc in enumerate(workers):
        for bikesIndex, bikesLoc in enumerate(bikes):
            distance = findDistance(workerLoc,bikesLoc)
            all_triplets.append((distance, workerIndex, bikesIndex))

    all_triplets.sort()

    bikesStatus =  [False] * len(bikes)
    workersStatus = [-1] * len(bikes)

    for distance, worker, bike in all_triplets:
        if workersStatus[worker] == -1 and  bikesStatus == False:
            bikesStatus[bike] = True
            workersStatus[worker] = bike


            if workersStatus.count(-1) == 0:
                break
    return workersStatus

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

print(assignBikes(workers, bikes))
# 1. Find distance using a distance function
# 2. Declare a list to store tuple of (distance, workers, bikes)
# 3. Enumerate through bikes and workers to get the (distance(findDistance), worker, bike)
# 4. Sort all triplets list
# 5. then go through each tuple
# 6. Bike status and worker status [false] and [-1]

