from LinkedList import Node, LinkedList

class Solution:
  def intersection(self, n1: Node, n2: Node):
    n1_tail = n1
    n2_tail = n2

    if n1_tail == n2_tail:
      # They are the same list
      return True

    while n1_tail and n1_tail.next != None:
      n1_tail = n1_tail.next
    
    while n2_tail and n2_tail.next != None:
      n2_tail = n2_tail.next

    return n1_tail == n2_tail

def main():
  solution = Solution()

  l1 = LinkedList()
  l1.insert_many(1, 2, 3, 4)

  l2 = LinkedList()
  l2.insert_many(4, 3, 2, 1)

  print(solution.intersection(l1.head, l1.head))

if __name__ == "__main__":
  main()