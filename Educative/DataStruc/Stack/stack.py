'''stack data structure
'''

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items==[]
    def top_of_stack(self):#peek operation
        if not self.is_empty():
            return self.items[-1]
mystack=stack()
mystack.push('A')
print(mystack.get_stack())
mystack.push('B')
mystack.push('C')
mystack.push('D')
print(mystack.get_stack())
mystack.push('E')
print('After pushing E to stack',mystack.get_stack())
mystack.pop()
print('Pop E',mystack.get_stack())
print(mystack.is_empty())
print('stack',mystack.get_stack(),'\nTop of stack:',mystack.top_of_stack())
mystack.push(4)
print('stack',mystack.get_stack(),'\nTop of stack:',mystack.top_of_stack())
mystack.push('prashun_chauhan')
print('stack',mystack.get_stack(),'\nTop of stack:',mystack.top_of_stack())
