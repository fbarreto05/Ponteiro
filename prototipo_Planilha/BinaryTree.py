class BinaryTree:
    class Node:
        def __init__(self, name, register, entry, out):
            self.name = name
            self.register = register
            self.entry = entry
            self.out = out
            self.leftChild = None
            self.rightChild = None

    def __init__(self):
        self.root = None

    def insert_Alf(self, name, register, entry, out):
        node = self.Node(name, register, entry, out)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current:
                if name < current.name:
                    if current.leftChild is None:
                        current.leftChild = node
                        break
                    current = current.leftChild
                else:
                    if current.rightChild is None:
                        current.rightChild = node
                        break
                    current = current.rightChild
    
    def insert_Reg(self, name, register, entry, out):
        node = self.Node(name, register, entry, out)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current:
                if register < current.register:
                    if current.leftChild is None:
                        current.leftChild = node
                        break
                    current = current.leftChild
                else:
                    if current.rightChild is None:
                        current.rightChild = node
                        break
                    current = current.rightChild


    def trasverse(self):
            return self.trasverseRec(self.root)

    def trasverseRec(self, node):
        if node:
            yield from self.trasverseRec(node.leftChild)    
            yield (node.name, node.register, node.entry, node.out)
            yield from self.trasverseRec(node.rightChild)
