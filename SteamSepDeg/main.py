from steamFriends import get_friends
from frontier import Node, QueueFrontier


def main():
    source = input("Input Steam 64bitID of a user: ")
    if not get_friends(source):
        print("This user has no friends or information is private")
        return

    target = input("Input Steam 64bitID of a user to find: ")

    path = shortest_path(source, target)

    if path is None:
        print("No path found")
    else:
        degrees = len(path)
        print(f"Degrees of separation: {degrees}")
        path = [(None, source)] + path
        for i in range(degrees):
            person1, person2 = path[i][1], path[i + 1][1]
            print(f"{i + 1}: {person1} is friends with {person2}")


def shortest_path(source, target):
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()

    frontier.add(start)
    explored = set()

    while True:
        if frontier.empty():
            return None

        node = frontier.remove()
        if node.state == target:
            actions = []
            cells = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            solution = []
            for i in range(len(actions)):
                solution.append((actions[i], cells[i]))
            return solution

        explored.add(node.state)

        friends = get_friends(node.state)
        if friends is not None:
            for friend in friends:
                if not frontier.contains_state(friend) and friend not in explored:
                    child = Node(state=friend, parent=node, action=None)
                    frontier.add(child)


if __name__ == "__main__":
    main()