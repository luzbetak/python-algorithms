class Node(object):

    # a binary Trees tree has a left node (smaller values) and a right node (greater values)
    def __init__(self, data):
        self.data = data;
        self.left_child = None;
        self.right_child = None;

    def __str__(self):
        return str(self.data)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None;

    # this is the method we will call to find the k-th smallest item
    def find_smallest(self, k):
        return self.get_k_smallest(self.root, k)

    def get_k_smallest(self, node, k):

        # number of nodes in the left subtree
        # +1 because we count the root node of the subtree as well
        n = self.tree_size(node.left_child) + 1

        # this is when we find the kth smallest item
        if n == k:
            return node

        # if the number of nodes in the left subtree > k-th smallest item
        # it means the k-th smallest item is in the left subtree
        if n > k:
            return self.get_k_smallest(node.left_child, k)

        # if the number of nodes in the left subtree is smaller then the k-th
        # smallest item then we can discard the left subtree and consider the
        # right substree
        # NOW WE ARE NOT LOOKING FOR THE K-TH BUT THE K-Nth SMALLEST ITEM
        if n < k:
            return self.get_k_smallest(node.right_child, k - n)

        return None

    # calculate the size of a subtree with root node 'node'
    def tree_size(self, node):

        # this is the base case (when the node is a child of a leaf node so it is NULL)
        if node is None:
            return 0

        # recursively sum up the size of the left subtree + size of right subtree
        # size of tree = size left subtree + size of right subtree + 1 (because of the root)
        return self.tree_size(node.left_child) + self.tree_size(node.right_child) + 1

    # inserting items in the tree O(logN) running time
    def insert(self, data):

        # if the root node is NULL it means this is the first node we insert
        if not self.root:
            self.root = Node(data);
        else:
            # there are already nodes in the tree so we have to find the valid place for this node
            self.insert_node(data, self.root);

    # it has O(logN) running time if the tree is balanced -> it can reduce to O(N)
    # thats why AVL trees or red-black trees are needed
    def insert_node(self, data, node):

        # the data is smaller so we have to go to the left subtree
        if data < node.data:
            # the left child is not a NULL so we keep going
            if node.left_child:
                self.insert_node(data, node.left_child);
            # the left child is NULL so we can insert the data here
            else:
                node.left_child = Node(data);
        # the data is greater so we have to go to the right subtree
        else:
            # the right child is not a NULL so we keep going
            if node.right_child:
                self.insert_node(data, node.right_child);
            # the right child is NULL so we can insert the data here
            else:
                node.right_child = Node(data);

    # if the tree is balanced then it has O(logN) running time
    def remove_node(self, data, node):

        # base case for recursive function calls
        if not node:
            return node;

        # first we have to find the node to remove
        # left node -> containts smaller value
        # right node -> conatains greater value
        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child);
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child);
        # this is when we find the node we want to remove
        else:

            # the node is a leaf node: no children at all
            if not node.left_child and not node.right_child:
                print("Removing a leaf node...");
                del node;
                return None;

            # the node we want to remove has a single right child
            if not node.left_child:  # node !!!
                print("Removing a node with single right child...");
                temp_node = node.right_child;
                del node;
                return temp_node;
            # the node we want to remove has a single left child
            elif not node.right_child:  # node instead of self
                print("Removing a node with single left child...");
                temp_node = node.left_child;
                del node;
                return temp_node;

            # the node has both left and right children
            print("Removing node with two children....");
            temp_node = self.get_predecessor(node.left_child);  # self instead of elf  + get predecessor
            node.data = temp_node.data;
            node.left_child = self.remove_node(temp_node.data, node.left_child);

        # this is how we notify the parent and update the children accordingly
        return node;

    # get the previous node in the in-order traversal)
    def get_predecessor(self, node):

        # the predecessor the largest node in the left subtree
        # successor: the smallest node in the right subtree
        if node.right_child:
            return self.get_predecessor(node.right_child);

        return node;

    # of course if the root is a NULL: we can not remove nodes at all
    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root);

    # it has O(logN) running time complexity
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root);

    def get_min(self, node):

        # smallest item is the left most node's value
        if node.left_child:
            return self.get_min(node.left_child);

        return node.data;

    # it has O(logN) running time complexity
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root);

    def get_max(self, node):

        # largest item is the right most node's value
        if node.right_child:
            return self.get_max(node.right_child);

        return node.data;

    # considering all the nodes in the tree IF there are items (so root node is not NULL)
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root);

    # considering all the items in O(N) running time
    # it yields the natural order (numerical ordering or alphabetical ordering)
    def traverse_in_order(self, node):

        # visit the left subtree
        if node.left_child:
            self.traverse_in_order(node.left_child);

        # then the root node of the subtree
        print("%s " % node.data);

        # then finally the right subtree recursively
        if node.right_child:
            self.traverse_in_order(node.right_child);


if __name__ == "__main__":
    bst = BinarySearchTree();

    bst.insert(100)
    bst.insert(13)
    bst.insert(50)
    bst.insert(14)

    print(bst.find_smallest(4))
