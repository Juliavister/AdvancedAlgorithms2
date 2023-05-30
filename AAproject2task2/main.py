def dfs(graph, current, visited, tables, seated):
    visited.add(current)
    if not tables: # keep track of the seated guests
        tables.append(set())
    for neighbor in graph[current]:
        if neighbor not in visited:
            # check if any neighbor already seated at a table
            seated_with = None
            for table in tables: #check if a guest already has a seat at a table
                if neighbor in table:
                    seated_with = table #guest is seated with someone at that table
                    break
            # if neighbor not seated and not already at a table, add to current table
            if seated_with is None and neighbor not in seated: # is not seated, is not assigned to a table
                seated.add(neighbor) # add to the set of seated guests
                seated_table = False
                for table in tables:
                    if not any(n in table for n in graph[neighbor]): # check if the guest is at the table and disliked by the current guest
                        table.add(neighbor) # add guest to current table
                        dfs(graph, neighbor, visited, tables, seated)
                        seated_table = True # current guest has been succesfully seated
                        break
                # if all tables are full, start new table
                if not seated_table:
                    tables.append(set([neighbor])) #creates a new set containing only the current guest
                    dfs(graph, neighbor, visited, tables, seated)
    unvisited_nodes = graph.keys() - visited #in graph.keys() we have all the guests
    if unvisited_nodes:
        dfs(graph, next(iter(unvisited_nodes)), visited, tables, seated)



# example input
guests = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Henry", "Isabel", "Jack", "Kelly"]
dislikes = [("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Dave"), ("Eve", "Frank"), ("Frank", "Grace"), ("Grace", "Henry"), ("Henry", "Isabel"), ("Isabel", "Jack"), ("Jack", "Kelly"), ("Kelly", "Alice")]




# create graph of dislikes
graph = {guest: set() for guest in guests}
for dislike in dislikes:
    graph[dislike[0]].add(dislike[1])
    graph[dislike[1]].add(dislike[0])

# set up sitting scheme
visited = set()
tables = []
assigned_tables = set()
dfs(graph, guests[0], visited, tables, assigned_tables)

# print result
for i, table in enumerate(tables):
    print(f"Table {i+1}: {', '.join(sorted(table))}")

