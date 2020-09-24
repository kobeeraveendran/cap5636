from queue import PriorityQueue

def ucs(graph, start, goal):

    fringe = PriorityQueue()
    visited = set()

    fringe.put((0, (start, [start])))

    print("Fringe: {}:{}".format(fringe.queue[0][1], fringe.queue[0][0]))
    print("Closed: ", visited)
    print()

    while not fringe.empty():
        cost, (curr, path) = fringe.get()

        if curr in visited:
            continue

        print("Expanded node: {}:{}".format(curr, cost))

        if curr == goal:
            return path

        else:
            
            visited.add(curr)
            
            for child in graph[curr]:
                if child[0] not in visited:
                    fringe.put((cost+child[1], (child[0], path+[child[0]])))
            
            print("Fringe: { ", end = '')
            for item in fringe.queue:
                print("({}: {})".format(item[1][0], item[0]), end = ' ')
            print("}")
            print("Closed set: ", visited)
            print()

            #print("\nFringe again: ", fringe.queue)


if __name__ == "__main__":

    graph = {
        "Miami": [("Tatooine", 5), ("Rivendell", 1)], 
        "Tatooine": [("Hogwarts", 4), ("Rivendell", 5), ("Miami", 5)], 
        "Rivendell": [("Miami", 1), ("Tatooine", 5), ("Hogwarts", 7), ("Orlando", 10)], 
        "Hogwarts": [("Tatooine", 4), ("Rivendell", 7), ("Orlando", 3)], 
        "Orlando": [("Hogwarts", 3), ("Rivendell", 10)]
    }

    path = ucs(graph, "Miami", "Orlando")
    print("\n\nOptimal Path: ", end = '')
    for i, location in enumerate(path):
        print(location, end = ' ')
        if i != len(path) - 1:
            print('-> ', end = '')
    print()