class Stack:
  def __init__(self, max_size = 5):
    self.__stack = []
    self.__size = 0
    self.__max_size = max_size

  def get_size(self):
    return self.__size
  
  def get_max_size(self):
    return self.__max_size

  def peek(self):
    if self.__size > 0:
      return self.__stack[-1]

    return None

  def push(self, value):
    self.__stack.append(value)
    self.__size += 1

  def pop(self):
    element = self.__stack.pop()
    self.__size -= 1
    return element

  def is_empty(self):
    return self.__size == 0

class StackOfPlates:
  def __init__(self):
    self.__stacks = [Stack()]
    self.__last_stack = 0

  def __get_stack(self, idx):
    return self.__stacks[idx]

  def __get_last_stack(self):
    return self.__get_stack(self.__last_stack)

  def __create_new_stack(self):
    self.__stacks.append(Stack())
    self.__last_stack += 1

  def __remove_last_stack(self):
    self.__stacks.pop()
    self.__last_stack -= 1

  def __has_exceeded_capacity(self):
    return self.__last_stack > 0

  def __create_stack_if_max(self):
    stack = self.__get_last_stack()
    if stack.get_size() == stack.get_max_size():
        self.__create_new_stack()

  def peek(self):
    stack = self.__get_last_stack()
    return stack.peek()

  def push(self, value):
    self.__create_stack_if_max()
    stack = self.__get_last_stack()
    stack.push(value)    

  def pop(self):
    stack = self.__get_last_stack()

    if stack.is_empty() and not self.__has_exceeded_capacity():
      return None

    if stack.is_empty():
      self.__remove_last_stack()
      
    stack = self.__get_last_stack()
    return stack.pop()

  def is_empty(self):
    stack = self.__get_last_stack()
    return stack.is_empty() and not self.__has_exceeded_capacity()


def main():
  stack = StackOfPlates()
  stack.push(2)
  stack.push(3)
  stack.push(7)
  stack.push(10)
  stack.push(20)

if __name__ == "__main__":
  main()
