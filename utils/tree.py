
# Abstract base class representing a tree structure
class Tree:

    # Abstract node class
    class Node:
        def __init__(self, parent = None, children = None, data = None):
            self.parent = parent
            self.children = children
            self.data = data

        # Return the data stored at this node
        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, d):
            self._data = d

        # Return Node representing node's parent (or None if node is root)
        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, p):
            self._parent = p if isinstance(p, self.__class__) or p is None else TypeError('parent must be a node')

        # Generate an iteration of Node representing node's children
        @property
        def children(self):
            return self._children

        @children.setter
        def children(self, c):
            self._children = [] if c is None else (c if isinstance(c, list) else TypeError('children must be a list'))

        # Return the number of children that Node node has
        def num_children(self):
            return len(self._children)

        # Return True if Node node represents the root of the tree
        def is_root(self):
            return self.parent is None

        # Return True if Node node doesn't have any children
        def is_leaf(self):
            return self.num_children() == 0

        # Return True if other Node represent the same data
        def __eq__(self, other):
            return self.data == other.data

        # Return True if other Node doesn't represent the same data
        def __ne__(self, other):
            return self.data != other.data

    def __init__(self):
        self.root = self.Node()

    # Return root Node of this tree
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r if isinstance(r, self.Node) else TypeError('root must be a node')

    def add_node(self, node):
        if node.parent in iter(self):
            node.parent.children.append(node)
            return

    def remove_node(self, node):
        if node in iter(self):
            node.parent.children.remove(node)

    # Return True if the tree is empty
    def is_empty(self):
        return len(self) == 0

    # Return depth of the node in this tree.
    def depth(self, node):
        if node.is_root():
            return 0
        return 1 + self.depth(node.parent())


    def _height(self, node):
        if node.is_leaf():
            return 0
        return 1 + max(self._height(child) for child in node.children())

    # Return depth of the node in this tree.
    def height(self, node=None):
        if node is None:
            node = self.root
        return self._height(node)

    # Return an iterable object of nodes a tree has
    def __iter__(self):
        self.queue = [self.root]
        return self

    # Return the next node object until no one is left
    def __next__(self):
        if len(self.queue) > 0:
            node = self.queue.pop(0)
            self.queue = node.children + self.queue
            return node
        raise StopIteration

    # Return the number of nodes a tree has
    def __len__(self):
        queue, count = [self.root], 0
        while len(queue) > 0:
            node = queue.pop(0)
            queue = node.children + queue
            count += 1
        return count

tree = Tree()
node = Tree.Node(tree.root)
tree.add_node(node)

for node in iter(tree):
    print(node.is_root())

print('\n')

for node in iter(tree):
    print(node.is_leaf())
