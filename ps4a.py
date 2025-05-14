# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1  = Node(8, Node(2, Node(1), Node(6)), Node(10)) #TODO
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))) #TODO
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))) #TODO

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if tree is None:
        return -1
    left = find_tree_height(tree.left)
    right = find_tree_height(tree.right)
    return 1 + max(left, right)

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func.
    '''
    if tree is None:
        return True

    left = tree.left
    right = tree.right

    if left:
        if not compare_func(left.value, tree.value):
            return False
        if not is_heap(left, compare_func):
            return False

    if right:
        if not compare_func(right.value, tree.value):
            return False
        if not is_heap(right, compare_func):
            return False

    return True

# Max heap comparator
def max_heap_compare(child_value, parent_value):
    return child_value <= parent_value

# Min heap comparator
def min_heap_compare(child_value, parent_value):
    return child_value >= parent_value


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    # print(tree1)
    # print(tree2)
    # print(tree3)
    print(find_tree_height(tree1))
    # print(tree1.left.__dict__)
    # print(len(tree1.left.__dict__))
    max_heap_tree = Node(10,
                     Node(9, Node(7), Node(6)),
                     Node(8))
    print("Is max heap:", is_heap(max_heap_tree, max_heap_compare))
    min_heap_tree = Node(1,
                     Node(3, Node(4), Node(6)),
                     Node(5))
    print("Is min heap:", is_heap(min_heap_tree, min_heap_compare))