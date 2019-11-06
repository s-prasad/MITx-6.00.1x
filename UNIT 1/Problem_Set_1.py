#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

#for item in (get_partitions(['a','b','c','d'])):
#     print(item)

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowsCopy = sorted(cows.items(), key = lambda kv:kv[1])
    ship = []

    while(len(cowsCopy) !=0):
        cowsToTransport = []
        shipWeight = 0
        
        for cow in reversed(cowsCopy):
            
            if (cow[1] + shipWeight <= limit):
                cowsToTransport.append(cow[0])
                shipWeight += cow[1]
                #print(shipWeight)
                cowsCopy.remove(cow)

        ship.append(cowsToTransport)

    print(ship)
    
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowsCopy = cows.items()
    cow_partitions = []
    shortest = None
    shortestSet = None

    for item in get_partitions(cowsCopy):
        cow_partitions.append(item)

    for sets in cow_partitions:
        if (shortest == None or len(sets)<shortest):
            setAccepted = True
            for set in sets:
                tripWeight = 0
                for cow in set:
                    tripWeight += cow[1]
                if tripWeight > limit:
                    setAccepted = False
            if (setAccepted):
                shortest = len(sets)
                shortestSet = sets

    print(shortestSet)
    
    
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10)
    end = time.time()
    print("Time to run greedy algorithm")
    print(end - start)

    start = time.time()
    brute_force_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10)
    end = time.time()
    print("Time to run brute force algorithm")
    print(end - start)    
