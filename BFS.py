
from queue import Queue

def BFS(labyrinth, start, speed, exit ):
    queue = Queue() #creates a queue that will store the nodes
    queue.put((start, 0)) # puts a tuple in the queue where "start" is starting node & "0" is distance from start to itself
    visited = set() #keeps track of all visited nodes
    visited.add(start) #adds the start node to visited nodes

    while not queue.empty():
        Node, distance = queue.get() #gets the first node and its distance from the queue
        if Node == exit: #if current node is the exit node, we calculate the time it took to reach it
            Time_to_Reach = distance / speed
            return Time_to_Reach
        for neighbour in labyrinth[Node]: #checks for each neighbour if it has been visited
            if neighbour not in visited:
                visited.add(neighbour) #adds the neighbour to visited nodes
                queue.put((neighbour, distance + 1))  #puts it into the queue with its distance from the starting node
    return -1



Labyrinth = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []} #layout of the maze - adjacent rooms


StartPosition = {"Wizard 1": "A", "Wizard 2": "B", "Wizard 3": "C"} #starting positions of the wizards, key = wizards and value = room
Speed = {"Wizard 1": 2, "Wizard 2": 3, "Wizard 3": 1} #their speeds, key = wizard and value = speed in corridors per second
EXIT = "E"

#compute the time it takes for the wizards to reach the exit
times = {}
for wizard, start in StartPosition.items():
    Time = BFS(Labyrinth, start, Speed[wizard], exit)
    times[wizard] = Time

#outputting the winning wizard
Winner = min(times, key=times.get)
print("The winner of the Triwizard Tournament is: ", Winner)

