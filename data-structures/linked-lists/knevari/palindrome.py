from LinkedList import LinkedList, Node

class Solution:
  def palindrome(self, ll: LinkedList):
    slow: Node = ll.head
    fast: Node = ll.head

    first_half = []

    while fast.next and fast.next.next:
      first_half.append(slow.value)
      slow = slow.next
      fast = fast.next.next

    if len(first_half) % 2 == 0:
      first_half.append(slow.value)
      slow = slow.next
    else:
      slow = slow.next

    while slow != None:
      if first_half[-1] != slow.value:
        return False
      slow = slow.next
      first_half.pop()

    return True

def main():
  solution = Solution()

  l1 = LinkedList()
  l1.insert_many(1, 2, 3, 4, 3, 2, 1) # True

  l2 = LinkedList()
  l2.insert_many(6, 2, 4, 3, 1, 2) # False

  l3 = LinkedList()
  l3.insert_many(1, 2, 3, 3, 2, 1) # True

  l4 = LinkedList()
  l4.insert_many('a', 'b', 'a') # True

  print(solution.palindrome(l1))
  print(solution.palindrome(l2))
  print(solution.palindrome(l3))
  print(solution.palindrome(l4))

if __name__ == "__main__":
  main()