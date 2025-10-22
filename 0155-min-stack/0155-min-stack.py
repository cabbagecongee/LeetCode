class MinStack(object):

    def __init__(self):
        self.head = None
    class Node:
        def __init__(self, value, prev_node, minimum):
            self.val = value
            self.prev = prev_node
            self.min = minimum

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = self.Node(val, None, val)
        else:
            min_val = min(self.head.min, val)
            new_node = self.Node(val, self.head, min_val)    
            self.head = new_node

    def pop(self):
        """
        :rtype: None
        """
        if self.head:
            self.head = self.head.prev
        

    def top(self):
        """
        :rtype: int
        """
        if self.head:
            return self.head.val
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.head:
            return self.head.min
        return None
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()