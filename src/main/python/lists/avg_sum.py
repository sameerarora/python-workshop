from lists.binary_search_tree import Node, insert


def average_sum(root):
    queue = [root]
    averages = []

    while (queue):
        sum = 0
        stop = len(queue)
        for _ in range(0, stop):
            pop = queue.pop()
            sum += pop.value
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)

        averages += [sum / stop]
    return averages


if __name__ == '__main__':
    root = Node(1)

    insert(root, 4)
    insert(root, 3)
    insert(root, 7)
    insert(root, -2)
    insert(root, 2)
    insert(root, 9)

    print(average_sum(root))

