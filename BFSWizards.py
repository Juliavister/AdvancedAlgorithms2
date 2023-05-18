import matplotlib.pyplot as plt
from queue import Queue

def BFS(labyrinth, starts, speeds, exit):
    queue = Queue()  # creates a queue that will store the nodes
    for wizard, start in starts.items():
        queue.put((start, 0, wizard))  # puts a tuple in the queue with start node, distance, and wizard name
    visited = set()  # keeps track of all visited nodes

    wizards_time = {}  # dictionary to store the time taken for each wizard to reach the exit

    while not queue.empty():
        node, distance, wizard = queue.get()  # gets the first node, its distance, and the wizard name
        if node == exit:  # if current node is the exit node
            time = distance / speeds[wizard]
            if wizard not in wizards_time:  # store the time for the wizard if it's not already recorded
                wizards_time[wizard] = time

        if node not in visited:
            visited.add(node)  # adds the node to visited nodes
            for neighbour in labyrinth[node]:  # checks for each neighbour if it has been visited
                queue.put((neighbour, distance + 1, wizard))  # puts it into the queue with updated distance and wizard name

    return wizards_time

Labyrinth = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}  # layout of the maze - adjacent rooms

StartPosition = {"Wizard 1": "A", "Wizard 2": "B", "Wizard 3": "C"}  # starting positions of the wizards, key = wizards and value = room
Speed = {"Wizard 1": 2, "Wizard 2": 3, "Wizard 3": 1}  # their speeds, key = wizard and value = speed in corridors per second
EXIT = "E"

#Compute time it takes for wizards to reach the exit
wizards_time = BFS(Labyrinth, StartPosition, Speed, EXIT)

# Outputting the winning wizard
winner = min(wizards_time, key=wizards_time.get)
print("The winner of the Triwizard Tournament is:", winner)

# Visualize the results
wizards = list(wizards_time.keys())
times = list(wizards_time.values())

plt.bar(range(len(wizards)),times)
plt.xlabel("Wizards")
plt.ylabel("Time to Reach Exit (seconds)")
plt.title("Triwizard Tournament Results")

plt.xticks(range(len(wizards)), wizards)
plt.show()
