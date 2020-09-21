class TreeNode():

    def __init__(self, value):
        self.value = value
        self.children = []
        self.path = []

    def add_child(self, value):
        newnode = TreeNode(value)
        newnode.path = self.path + [self.value]
        self.children.append(newnode)

def bfs(tree, goal):
    fringe = [tree]

    while len(fringe) > 0:
        print("Fringe: {}".format([x.value for x in fringe]))
        curr = fringe.pop(0)
        print("Current: ", curr.value, "\n")

        if curr.value == goal:
            curr.path.append(curr.value)
            return curr.path
        else:
            for child in curr.children:
                fringe.append(child)

    return None


if __name__ == "__main__":

    start = TreeNode('A')
    start.add_child('B')
    start.add_child('C')
    start.children[0].add_child('D')
    start.children[1].add_child('E')
    start.children[1].add_child('F')

    print(bfs(start, goal = 'F'))

