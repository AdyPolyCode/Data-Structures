class Node:
    def __init__(self, value):
        '''
        Node class creator method
        input value is needed to store a value in it, respectively create a Node
        '''
        self.value = value
        self.nextValue = None
    
    def getValue(self):
        '''
        Return a single value from the call

        # obj.getValue() -> value
        '''
        return self.value
    
    def getNextValue(self):
        '''
        Calling the next node value
        
        ### ### ### ### ###
        obj1 = Node(value)
        obj2 = Node(value)

        obj1.setNextValue(obj2)
        ### ### ### ### ###

        # obj1.getNextValue() -> obj2
        '''
        return self.nextValue
    
    def setNextValue(self, value):
        '''
        Setting a next (node) value to the given node

        obj1 = Node(value)
        obj2 = Node(value)

        # obj1.setNextValue(obj2)
        '''
        self.nextValue = value
