from node import Node

class LinkedList:
    def __init__(self, value=None):
        '''
        LinkedList class creater method
        input value is not necessary, since adding new values will set the head/first value
        '''
        self.head = Node(value)
    
    def getHead(self):
        '''
        Simple getter method that returns the head/first value in the LinkedList
        '''
        return self.head
    
    def addLeft(self, value):
        '''
        Add method - adding a specific value to the left side of the list
        left side - every new value that is going to be added will become the head/first value
        '''
        newNode = Node(value)
        newNode.setNextValue(self.head)
        self.head = newNode
    
    def addRight(self, value):
        '''
        Add method - adding a specific value to the right side of the list
        right side - every new value that is going to be added will become the tail/last value
        '''
        if self.head.getValue() is None:
            newNode = Node(value)
            newNode.setNextValue(self.head)
            self.head = newNode
        else:
            currentNode = self.getHead()
            while currentNode.getNextValue() is not None:
                currentNode = currentNode.getNextValue()
            currentNode.setNextValue(Node(value))
    
    def printList(self):
        '''
        All the values being printed to the console
        '''
        string = ''
        currentNode = self.getHead()
        while currentNode:
            if currentNode.getValue() is not None:
                string += str(currentNode.getValue()) + '\n'
            currentNode = currentNode.getNextValue()
        return string
    
    def addAnywhere(self, givenValue, value):
        '''
        Add method - adding a specific value to the list , can be in between, first, last spot
        '''
        newNode = Node(value)
        currentNode = self.getHead()
        while currentNode:
            next_node = currentNode.getNextValue()
            if currentNode.getValue() == givenValue:
                currentNode.setNextValue(newNode)
                newNode.setNextValue(next_node)
                currentNode = None
            else:
                currentNode = next_node
    
    def remove(self, valueToRemove):
        '''
        Remove method - removing a specific value from the list
        '''
        currentNode = self.getHead()
        if currentNode.getValue() == valueToRemove:
            self.head = currentNode.getNextValue()
        else:
            while currentNode:
                nextNode = currentNode.getNextValue()
                if nextNode.getValue() == valueToRemove:
                    currentNode.setNextValue(nextNode.getNextValue())
                    currentNode = None
                else:
                    currentNode = nextNode
    
    def swap(self, valueOne, valueTwo):
        '''
        Swap method - swapping values
        node1 becomes node2 - if both are not None or not the same
        '''
        if valueOne == valueTwo:
            print('Swap is not possible, both values are the same.')
            return
        
        nodeOne = self.getHead()
        prevOne = None
        while nodeOne and nodeOne.getValue() != valueOne:
            prevOne = nodeOne
            nodeOne = nodeOne.getNextValue()
        
        nodeTwo = self.getHead()
        prevTwo = None
        while nodeTwo and nodeTwo.getValue() != valueTwo:
            prevTwo = nodeTwo
            nodeTwo = nodeTwo.getNextValue()
        
        if nodeOne is None or nodeTwo is None:
            print('Swap is not possible, on or two nodes are null.')
            return
        
        if prevOne is None:
            self.head = nodeTwo
        else:
            prevOne.setNextValue(nodeTwo)

        if prevTwo is None:
            self.head = nodeOne
        else:
            prevTwo.setNextValue(nodeOne)
        
        temp = nodeOne.getNextValue()
        nodeOne.setNextValue(nodeTwo.getNextValue())
        nodeTwo.setNextValue(temp)
    

    def n_th_last(self, n):
        '''
        n-parameter (has to be an int:) is required, if not an exception is raised
        The returned value will be the n-th last element from the list
        if the list is empty None will be returned
        '''

        if isinstance(n, int):
            tail = self.getHead()
            wanted = None
            pointer = 1

            while tail:
                tail = tail.getNextValue()
                pointer += 1

                if pointer >= n + 1:
                    if wanted is None:
                        wanted = self.getHead()
                    else:
                        wanted = wanted.getNextValue()
            return wanted
        else:
            raise ValueError(f'Given value "{n}" is a type of "{type(n).__name__}". Integer expected but "{type(n).__name__}" given.')
    
    
    def get_middle(self):
        '''
        The returned value will be the middle element in the list
        if the list is empty None will be returned
        '''
        slow = self.getHead()
        fast = self.getHead()

        while fast:
            fast = fast.getNextValue()

            if fast:
                fast = fast.getNextValue()
                slow = slow.getNextValue()
        return slow
