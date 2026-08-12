class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.prev= None 
        self.next= None 

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # hashmap 
        self.cache={} 
        self.head = Node(0,0) # dummy head 
        self.tail = Node(0,0) # dummy tail 

        self.head.next= self.tail
        self.tail.prev = self.head 
    
    def remove_node(self, node): 
        
        prev_node = node.prev
        next_node = node.next 

        # skip current node 
        prev_node.next = next_node 
        next_node.prev = prev_node 
        
    def add_to_front(self, node): 
        first_node= self.head.next 

        self.head.next = node 
        node.prev = self.head

        node.next= first_node
        first_node.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # If key is not present, return -1
        if key not in self.cache:
            return -1

        # Get the node from hashmap
        node = self.cache[key]

        # Since this key was just used,
        # move it to the front as most recently used
        self.remove_node(node)
        self.add_to_front(node)

        # Return the stored value
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # If key already exists, remove its old node first
        # We will insert the updated node at the front
        if key in self.cache:
            old_node = self.cache[key]
            self.remove_node(old_node)

        # Create a new node with updated key and value
        new_node = Node(key, value)

        # Save it in hashmap for O(1) lookup
        self.cache[key] = new_node

        # Add it to front because put also counts as recent use
        self.add_to_front(new_node)

        # If we exceeded capacity, remove least recently used node
        if len(self.cache) > self.capacity:
            # Least recently used node is right before dummy tail
            lru_node = self.tail.prev

            # Remove LRU node from linked list
            self.remove_node(lru_node)

            # Remove LRU key from hashmap
            del self.cache[lru_node.key]