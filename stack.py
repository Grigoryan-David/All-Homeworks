class Stack:
  def __init__(self):
      self.items_list = []  

  def is_empty(self):
      return self.items_list == []

  def push(self, item):
      self.items_list.insert(0, item)

  def pop(self):
      return self.items_list.pop(0)

  def print_stack(self):
      print(self.items_list)

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()