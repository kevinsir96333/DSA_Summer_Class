class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return 'Data: ' + str(self.data)


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None    ### 전체 LinkedList에 Tail을 추가함으로써 LinkedList의 끝이 어디인지 표시 

  def __str__(self):
    msg = ''
    current_node = self.head
    while current_node is not None:
      msg += str(current_node.data)
      if current_node.next is not None:
        msg += ' -> '
      current_node = current_node.next
    if len(msg) == 0:
      msg = 'Empty linked list'
    return msg

  def insert(self, data):
    new_node = Node(data)
    if self.tail is None:
      self.tail = new_node
      self.head = new_node
    else:
      last_node = self.tail ### last_node를 tail로 설정.
      last_node.next = new_node ### 그리고 last_node의 다음 노드를 새로운 노드로 설정.
      self.tail = new_node  ### 그리고 tail을 새로운 노드로 설정. 
      
      """
      이전에는 검색을 시도해서 마지막 노드를 찾아서 추가했지만, 이번에는 tail을 추가해서 마지막 노드를 찾지 않고 추가함.
      tail을 추가하여 검색과정을 생략함으로써 반복문을 사용하여 시간복잡도를 증가시킬 필요가 없다.
      대신 tail을 추가함에 따라 추가적인 메모리를 사용함에 따라 공간 복잡도가 증가할 수는 있다. 
      그럼에도 점근적 접근을 취하는 시간 복잡도에서는 이점이 있다.
      """

  def search(self, target):
    result = None
    current_node = self.head
    while current_node is not None:
      if current_node.data == target:
        result = current_node
        break
      current_node = current_node.next
    return result

  def delete(self, target):
    prev_node = None
    current_node = self.head
    while current_node is not None:
        if current_node.data == target:
            if current_node == self.head and current_node == self.tail: ### head와 tail이 같은 경우
                self.head = None      ### head와 tail을 각각 None으로 설정 
                self.tail = None
                break 
            elif current_node == self.head and current_node != self.tail: ### head와 tail이 다른 경우. 단, head = current_node인 경우 
                self.head = current_node.next   ### head를 다음 노드로 설정
                current_node.next = None    ### current_node의 다음 노드를 None으로 설정 // 연결을 끊어버림.
                break
            elif current_node != self.head and current_node == self.tail: ### head와 tail이 다른 경우
                prev_node.next = None
                self.tail = prev_node   ### tail을 이전 노드로 설정
                break
            else:
                prev_node.next = current_node.next
                current_node.next = None 
                break
        prev_node = current_node
        current_node = current_node.next
    
    """
      물론 current_node.next를 굳이 None으로 설정하지 않아도 해당 예제에서는 같은 결과를 출력하는 것으로 보인다. 
      다만, current_node.next를 None으로 설정함으로써 연결을 끊어버림으로써 메모리를 더욱 효율적으로 사용할 수 있다.
      특히 저차원의 단계로 갈수록 (물론 그 경우 파이썬 자체를 사용하기보다는 C++, JAVA등을 사용하거나 방언을 사용하거나 별도의 컴파일 과정을 거칠 수도 있지만 )  
      저렇게 남겨둔 연결이 메모리 누수로 이어질 수 있기 때문에 연결을 끊어버리는 것이 좋다.
      
    """

linked_list = LinkedList()
linked_list.insert(12)
linked_list.insert(99)
linked_list.insert(37)
linked_list.insert(24)
linked_list.insert(56)
print(linked_list)

result = linked_list.search(24)
print(result)
print(linked_list.search(100))

linked_list.delete(12)
print(linked_list)
linked_list.delete(37)
print(linked_list)
linked_list.delete(56)
print(linked_list)
linked_list.delete(100)
print(linked_list)