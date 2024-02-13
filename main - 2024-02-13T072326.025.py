class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def backward_induction(node, is_player1_turn):
    if len(node.children) == 0:
        return 0  # Payoff for player 2 (if player 1 wins) or player 1 (if player 2 wins)

    if is_player1_turn:
        value = max(backward_induction(child, False) for child in node.children)
    else:
        value = min(backward_induction(child, True) for child in node.children)

    return value


# Construct the game tree
root = Node("Root")
node1 = Node("1/3")
node2 = Node("2/3")
node3 = Node("1")
node4 = Node("0")
node5 = Node("1/3")
node6 = Node("2/3")
node7 = Node("2")
node8 = Node("0")
node9 = Node("1")
node10 = Node("0")

root.add_child(node1)
root.add_child(node2)
node1.add_child(node3)
node1.add_child(node4)
node2.add_child(node5)
node2.add_child(node6)
node5.add_child(node7)
node5.add_child(node8)
node6.add_child(node9)
node6.add_child(node10)

# Find the subgame perfect equilibrium using backward induction
equilibrium_payoff = backward_induction(root, True)
print("Subgame perfect equilibrium payoff:", equilibrium_payoff)
