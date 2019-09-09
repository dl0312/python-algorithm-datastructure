class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    # 연결리스트 이어 붙이기
    def concat(self, L):
        lastNode = self.tail.prev
        firstNode = L.head.next
        lastNode.next = firstNode
        firstNode.prev = lastNode
        self.tail = L.tail
        self.nodeCount += L.nodeCount

    # 정방향 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    # 역방향 순회
    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    # 특정 위치 뒤에 원소 삽입
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    # 특정 위치 앞에 원소 삽입
    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    # 특정 위치에 원소 삽입
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # 특정 위치 뒤에 원소 삭제
    def popAfter(self, prev):
        delNode = prev.next
        next = delNode.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return delNode.data

    # 특정 위치 앞에 원소 삭제
    def popBefore(self, next):
        delNode = next.prev
        prev = delNode.prev
        next.prev = prev
        prev.next = next
        self.nodeCount -= 1
        return delNode.data

    # 특정 위치 원소 삭제
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # 특정 원소 얻어내기
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
            return curr
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
            return curr