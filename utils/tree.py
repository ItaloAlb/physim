from utils.pointer import *


# Abstract base class representing a tree structure
class Tree:

    # Abstract node class
    class Node:

        data = ptr()

        def __init__(self, **kwargs):
            self.parent, self.data, self.children, self.tag = kwargs.get('parent', None), \
                                                              kwargs.get('data', None), \
                                                              kwargs.get('children', None), \
                                                              kwargs.get('tag', None)


        # # Return the data stored at this node
        # @property
        # def data(self):
        #     return self._data
        #
        # @data.setter
        # def data(self, d):
        #     if not(isinstance(d, list) or d is None):
        #         raise TypeError('data must be a list')
        #     self._data = [] if d is None else d

        # Return Node representing node's parent (or None if node is root)
        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, p):
            if not(isinstance(p, self.__class__) or p is None):
                raise TypeError('parent must be a node')
            self._parent = p

        # Generate an iteration of Node representing node's children
        @property
        def children(self):
            return self._children

        @children.setter
        def children(self, c):
            if not(isinstance(c, list) or c is None):
                raise TypeError('children must be a list')
            self._children = [] if c is None else c

        # Return the number of children that Node node has
        def num_children(self):
            return len(self._children)

        # Return True if Node node represents the root of the tree
        @property
        def is_root(self):
            return self.parent is None

        # Return True if Node node doesn't have any children
        @property
        def is_leaf(self):
            return self.num_children() == 0

        # Return True if other Node represent the same data
        def __eq__(self, other):
            return self.data == other.data

        # Return True if other Node doesn't represent the same data
        def __ne__(self, other):
            return self.data != other.data

    def __init__(self, **kwargs):
        self.root = Tree.Node(
            data=kwargs.get('data', None),
            tag=kwargs.get('tag', 'root')
        )

    # Return root Node of this tree
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        if not isinstance(r, self.Node):
            raise TypeError('root must be a node')
        self._root = r

    def add_node(self, *nodes):
        for node in nodes:
            if node.parent in iter(self):
                node.parent.children.append(node)

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
        return 1 + self.depth(node.parent)


    def _height(self, node):
        if node.is_leaf():
            return 0
        return 1 + max(self._height(child) for child in node.children())

    # Return depth of the node in this tree.
    def height(self, node=None):
        if node is None:
            node = self.root
        return self._height(node)

    @property
    def __leaf__(self):
        leaf = []
        for node in iter(self):
            if node.is_leaf:
                leaf.append(node)
        return leaf


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
        if self.root is None:
            return 0
        queue, count = [self.root], 0
        while len(queue) > 0:
            node = queue.pop(0)
            queue = node.children + queue
            count += 1
        return count

    def __str__(self):
        _str = ""
        return _str


class Octree(Tree):
    class Space(Tree.Node):
        def __init__(self, **kwargs):

            self.parent, self.center, self.width, self.data, self.children, self.tag = kwargs.get('parent', None), \
                                                                                       kwargs.get('center', None), \
                                                                                       kwargs.get('width', None), \
                                                                                       kwargs.get('data', None), \
                                                                                       kwargs.get('children', None), \
                                                                                       kwargs.get('tag', None)

            super().__init__(
                parent=self.parent,
                data=self.data,
                children=self.children,
                tag=self.tag
            )


        @property
        def center(self):
            return self._center

        @center.setter
        def center(self, c):
            self._center = c

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, w):
            self._width = w

    def __init__(self, **kwargs):
        super().__init__()
        self.root = Octree.Space(
            center=kwargs.get('center', (0, 0, 0)),
            width=kwargs.get('width', 1),
            data=kwargs.get('data', None),
            tag=kwargs.get('tag', 'root')
        )

    def subdivide(self):
        if self.is_empty():
            raise SubdivideEmptyTreeError
        for leaf in self.__leaf__:
            c, w = leaf.center, leaf.width / 2
            nwf, nef, swf, sef = Octree.Space(parent=leaf, center=(c[0] - w, c[1] + w, c[2] - w), width=w, tag="nwf"), \
                                 Octree.Space(parent=leaf, center=(c[0] + w, c[1] + w, c[2] - w), width=w, tag="nef"), \
                                 Octree.Space(parent=leaf, center=(c[0] - w, c[1] - w, c[2] - w), width=w, tag="swf"), \
                                 Octree.Space(parent=leaf, center=(c[0] + w, c[1] - w, c[2] - w), width=w, tag="sef")

            nwb, neb, swb, seb = Octree.Space(parent=leaf, center=(c[0] - w, c[1] + w, c[2] + w), width=w, tag="nwb"), \
                                 Octree.Space(parent=leaf, center=(c[0] + w, c[1] + w, c[2] + w), width=w, tag="neb"), \
                                 Octree.Space(parent=leaf, center=(c[0] - w, c[1] - w, c[2] + w), width=w, tag="swb"), \
                                 Octree.Space(parent=leaf, center=(c[0] + w, c[1] - w, c[2] + w), width=w, tag="seb")

            self.add_node(nwf, nef, swf, sef, nwb, neb, swb, seb)

    # Create a data reference on root's data to leaf's data based on a space partitioning criteria
    def relocate(self):

        pass

class SubdivideEmptyTreeError(Exception):
    """Raised when trying to subdivide an empty tree"""
    pass

# tree = Tree()
octree = Octree()
# octree.subdivide()
# for node in octree.__leaf__:
#     print("center: ", node.center, "   \t width: ", node.width, "\t tag: ", node.tag)