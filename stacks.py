


from dataclasses import dataclass

#push, top, pop, bottom, is_empty

@dataclass
class Stack: 

    items = []

    def push(self, item):
        self.items.append(item)
    
    def top(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()
    
    def bottom(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    

