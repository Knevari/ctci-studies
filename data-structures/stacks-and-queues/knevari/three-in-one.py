class ThreeStacks:
  def __init__(self):
    self.__stacks = [0, 0, 0]

    self.__s1_next = 0
    self.__s2_next = 1
    self.__s3_next = 2

    self.__s1_top = -1
    self.__s2_top = -1
    self.__s3_top = -1

  def __increaseStackCapacity(self):
    self.__stacks.extend([0, 0, 0])

  def __push_to_first_stack(self, value):
    self.__stacks[self.__s1_next] = value
    self.__s1_top = self.__s1_next
    self.__s1_next += 3

    if len(self.__stacks) < self.__s1_next + 1:
      self.__increaseStackCapacity()

  def __push_to_second_stack(self, value):
    self.__stacks[self.__s2_next] = value
    self.__s2_top = self.__s2_next
    self.__s2_next += 3

    if len(self.__stacks) < self.__s2_next + 1:
      self.__increaseStackCapacity()

  def __push_to_third_stack(self, value):
    self.__stacks[self.__s3_next] = value
    self.__s3_top = self.__s3_next
    self.__s3_next += 3

    if len(self.__stacks) < self.__s3_next + 1:
      self.__increaseStackCapacity()

  def __pop_from_first_stack(self):
    if self.__s1_top == -1:
      return None

    item = self.__stacks[self.__s1_top]
    self.__s1_top -= 3
    self.__s1_next -= 3

    return item

  def __pop_from_second_stack(self):
    if self.__s2_top == -1:
      return None

    item = self.__stacks[self.__s2_top]
    self.__s2_top -= 3
    self.__s1_next -= 3
    
    return item

  def __pop_from_third_stack(self):
    if self.__s3_top == -1:
      return None

    item = self.__stacks[self.__s3_top]
    self.__s3_top -= 3
    self.__s1_next -= 3
    
    return item


  def __peek_from_first_stack(self):
    return self.__stacks[self.__s1_top]

  def __peek_from_second_stack(self):
    return self.__stacks[self.__s2_top]
  
  def __peek_from_third_stack(self):
    return self.__stacks[self.__s3_top]

  def push_to_stack(self, stack_idx, value):
    if stack_idx > 2:
      raise Exception
    
    if stack_idx == 0: self.__push_to_first_stack(value)
    elif stack_idx == 1: self.__push_to_second_stack(value)
    elif stack_idx == 2: self.__push_to_third_stack(value)

  def peek_from_stack(self, stack_idx):
    if stack_idx == 0: return self.__peek_from_first_stack()
    elif stack_idx == 1: return self.__peek_from_second_stack()
    elif stack_idx == 2: return self.__peek_from_third_stack()

  def pop_from_stack(self, stack_idx):
    if stack_idx == 0: return self.__pop_from_first_stack()
    elif stack_idx == 1: return self.__pop_from_second_stack()
    elif stack_idx == 2: return self.__pop_from_third_stack()


def main():
  stacks = ThreeStacks()

  # Push to first stack
  stacks.push_to_stack(0, 2)
  stacks.push_to_stack(0, 3)
  stacks.push_to_stack(0, 5)

  # Push to second stack
  stacks.push_to_stack(1, 1)
  stacks.push_to_stack(1, 1)
  stacks.push_to_stack(1, 2)

  # Push to third stack
  stacks.push_to_stack(2, 1)
  stacks.push_to_stack(2, 2)
  stacks.push_to_stack(2, 3)

  print(stacks.pop_from_stack(0)) # 5
  print(stacks.pop_from_stack(1)) # 2
  print(stacks.pop_from_stack(2)) # 3
  print(stacks.pop_from_stack(0)) # 3
  print(stacks.pop_from_stack(0)) # 2


if __name__ == "__main__":
  main()