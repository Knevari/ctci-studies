from LinkedList import LinkedList

class Solution:
  def loop_detection(self, ll: LinkedList):
    p1 = ll.head
    p2 = ll.head

    while p2 and p2.next != None:
      p1 = p1.next
      p2 = p2.next.next

      if p1 == p2:
        break
    
    if p2 == None or p2.next == None:
      return None

    p1 = ll.head

    while p1 != p2:
      p1 = p1.next
      p2 = p2.next

    return p1

def main():
  solution = Solution()

  l1 = LinkedList()
  l1.insert_many(1, 2, 3, 4, 5, 6, 7, 8)

  start_of_cycle = l1.head.next.next.next.next # 5
  l1.tail.next = start_of_cycle

  print(solution.loop_detection(l1).value) # 5

if __name__ == "__main__":
  main()