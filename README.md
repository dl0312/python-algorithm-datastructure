## 선형 배열(Linear Arrays)
선형 배열은 데이터들이 선(line)처럼 일렬로 늘어선 형태를 말한다. 보통 프로그래밍에서 배열(array)라 하면 같은 타입의 데이터가 줄지어 늘어서 있는 것을 뜻합니다. 그러나 python에서는 서로 다른 종류의 데이터 또한 줄세울 수 있는 리스트(list)라는 데이터형이 있습니다.
```python
L = ['Bob', 'Cat', 'Spam', 'Superman']
```
배열(array)라는 말과 리스트(list)라는 말이 자주 등장하는데, 일단은 같은 것으로 생각해도 좋지만, 개념적인 구조, 즉 데이터를 늘어놓은 모양새를 말할 때에는 배열(array)를, python의 데이터형을 가리킬 때에는 리스트(list)라는 용어를 사용한다.

### 리스트(배열) 연산
#### 리스트 길이와 관계없이 빠르게 실행 결과를 보게되는 연산들 (O(1))
* 원소 덧붙이기 `.append()`
* 원소 하나를 꺼내기 `.pop()`
#### 리스트의 길이에 비례해서 실행 시간이 걸리는 연산들 (O(n), 리스트의 길이에 비례)
* 원소 삽입하기 `.insert()`
* 원소 삭제하기 `.del()`
#### 추가 다른 연산
* 원소 탐색하기 `.index()`

### 정렬(sort)과 탐색(search)

#### 정렬(sort)이란?
복수의 원소로 이루어진 데이터를 정해진 기준에 따라 새로 늘어놓는 작업이다. 정렬 알고리즘에는 여러 종류가 있다.
python의 리스트(list)를 이용한다면, 직접 정렬 알고리즘을 구현할 필요가 없다. 왜냐하면 이미 리스트(list)에 내장 정렬 기능이 있기 때문이다.
아래와 같은 두 방법이 대표적이다.
1. 파이썬 내장 함수 `sorted()`
2. 리스트에 쓸 수 있는 method `.sort()`
```python
L2 = sorted(L, reverse=True)
L2.sort(reverse=True)
```

#### 문자열로 이루어진 리스트의 정렬
정렬 순서는 사전 순서(알파벳 순서)를 따른다.
> 문자열의 길이 순서대로 정렬하고 싶다면? `lambda`를 사용한다.
 ```python
>>> L = ['abcd', 'xyz', 'spam']
>>> sorted(L, key=lambda x: len(x))
['xyz', 'abcd', 'spam']
```
`key`를 지정하는 또 다른 예시
```python
L = [{'name': 'John', 'score':83},{'name': 'Paul', 'score':92}]
L.sort(key=lambda x: x['score'], reverse=True) # L을 점수가 높은 순으로 정렬
```

#### 탐색(search)이란?
복수의 원소로 이루어진 데이터에서 특정 원소를 찾아내는 작업이다. 탐색에 다양한 방법이 있지만, 기본적인 두 가지를 알아보자.
#### 탐색 알고리즘 (1) - 선형 탐색(Linear Search) (O(n))
순차적으로 모든 요소들을 탐색하여 원하는 값을 찾아내는 방식이다. 배열의 길이에 비례하는 시간이 걸리기 때문에 최악의 경우 배열에 있는 모든 원소를 다 검사해야 할 수 있다.
```python
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1
```
#### 탐색 알고리즘 (2) - 이진 탐색(Binary Search) (O(nlogn))
탐색하려는 배열이 이미 정렬되어 있는 경우에만 적용할 수 있따. 배열의 가운데 원소와 찾으려 하는 값을 비교하여 탐색하는 알고리즘입니다.
```python
def binary_search(L, x):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            start = mid + 1
        else:
            end = mid -1
    return -1
```

### 재귀 알고리즘(recursive algorithms)
주어진 문제가 있을 때, 이것을 같은 종류의 보다 쉬운 문제의 답을 이용해서 풀 수 있는 성질을 이용해서, 같은 알고리즘을 반복적으로 적용함으로써 풀어내는 방법.

#### 재귀 알고리즘의 예시
* 피보나치 순열
```python
# 반복적 방법(iterative)
def solution(x):
    a = 0
    b = 1
    if x == 0:
        return a
    elif x == 1:
        return b
    else:
        for i in range(1,x):
            c = a + b
            a = b
            b = c
    return c
```
```python
# 재귀적 방법(recursive)
def solution(x):
    a = 0
    b = 1
    if x == 0:
        return a
    elif x == 1:
        return b
    return solution(x-1) + solution(x-2)
```
* 조합의 수 (n개의 서로 다른 원소에서 m개를 택하는 경우의 수) 구하기
* 하노이의 탑 (크기 순서로 쌓여 있는 원반을 한 막대에서 다른 막대로 옮기기)

재귀 알고리즘을 적용하면 사람이 생각하는 것과 동일한 방식으로 풀어 알고리즘을 간단하고 이해하기 쉽게 서술할 수 있다는 장점이 있지만, 대부분의 경우 재귀 알고리즘이 주어질 때 이것을 재귀적이지 않은 방법으로 동일하게 풀어내는 알고리즘이 존재하고, 보통은 순환문(loop)을 이용해서 정해진 연산을 반복해서 문제의 답을 구해서 이를 반복적(iterative) 알고리즘이라고 부르기도 한다. 그리고 반복적인 알고리즘이 재귀적인 알고리즘보다 문제풀이의 시간적 효율이 높다.

#### 재귀적 이진탐색
```python
def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)
```

## 알고리즘의 복잡도 (Complexity of Algorithm)

#### 시간 복잡도 (Time Complexity)
문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계
#### 공간 복잡도 (Space Complexity)
문제의 크기광 이를 해결하는 데 필요한 메모리 공간 사이의 관계
#### 평균 시간 복잡도 (Average Time Complexity)
임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
#### 최악 시간 복잡도 (Worst-case Time Complexity)
가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간

#### Big-O 표기법(Notation)
점근 표기법(asymptotic notation)의 하나로 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현하며 알고리즘의 복잡도를 표현할 때 흔히 쓰인다.
> `O(1)`, `O(logn)`, `O(nlogn)`, `O(n)`, `O(n^2)`

##### 삽입정렬(insertion sort)
Best case: `O(n)`
Worst case: `O(n^2)`
##### 병합정렬(merge sort)
Average case: `O(nlogn)`
##### 배낭문제(Knapsack Problem)
풀이 방법에 따라 `O(2^n)` 혹은 `O(n)`

## 연결 리스트(Linked Lists)
데이터 원소들을 순서를 지어 늘어놓는다는 점에서 연결 리스트 (linked list) 는 선형 배열 (linear array) 과 비슷한 면이 있지만, 데이터 원소들을 늘어놓는 방식에서 이 두 가지는 큰 차이가 있다. 구체적으로, 선형 배열이 "번호가 붙여진 칸에 원소들을 채워넣는" 방식이라고 한다면, 연결 리스트는 "각 원소들을 줄줄이 엮어서" 관리하는 방식이다. 그렇다면 선형 배열에 비해 연결 리스트가 가지는 이점은 무엇일까?

연결 리스트에서는 원소들이 링크(link)라 부르는 고리로 연결되어 있으므로, 가운데에서 끊어서 하나를 삭제하거나, 다른 원소를 삽입하는 것이 선형 배열의 경우보다 빠르게 처리할 수 있다. 따라서 원소의 삽입/삭제가 빈번히 일어나는 응용에서는 연결리스트가 많이 사용된다. 컴퓨터 시스템을 구성하는 중요한 요소인 운영체제(OS)의 내부에서도 이러한 연결리스트가 여러 곳에서 이용되고 있다.

물론 단점도 있다. 삽입과 삭제가 용이한 만큼 선형 배열에 비해서 데이터 구조 표현에 소요되는 저장 공간(메모리)가 크다. 링크도 메모리에 저장되어 있어야 하기 때문에, 연결 리스트를 표현하기 위해서는 동일한 데이터 원소들을 담기 위해 사용하는 메모리 요구량이 더 크다. 가장 큰 단점은 'k번째 원소'를 찾아가는 데에 선형 배열의 경우보다 시간이 오래 걸리다는 점이다. 선형 배열에서는 데이터 원소들이 번호가 붙여진 칸들에 들어 있으므로 그 번호를 이용하여 한 번에 특정 번째 원소를 찾아갈 수 있지만, 연결 리스트에서는 단지 원소들이 고리로 연결된 모습을 하고 있기 때문에 특정 번째 원소를 접근하기 위해서는 앞에서부터 하나씩 링크를 따라가면서 찾아가야한다.

연결 리스트가 힘을 발휘하는 경우는 리스트를 따라서 하나 하나 원소들을 대상으로 어떤 작업을 하다가, 그 위치에 새로운 데이터 원소를 삽입하거나, 그 위치에 있는 데이터 원소를 삭제하는 경우이다.
(ex. 스마트폰에서의 앱 전환 및 삭제)
* 원소의 삽입 (insertion)
* 원소의 삭제 (deletion)
* 두 리스트 합치기 (concatenation)
> [Linked List Traverse](./problems/linked_list_traverse.py)
> [Linked List Node Deletion](./problems/linked_list_node_deletion.py)
> [Linked List with dummy head](./problems/linked_list_with_dummy_head.py)

## 양방향 연결 리스트(Doubly Linked Lists)
기존의 연결 리스트를 한 쪽으로만 연결하지 않고 양쪽으로 연결하자, 앞으로도 (다음 Node) 뒤로도 (이전 Node) 진행이 가능하다.
양방향 연결 리스트의 구현을 위해서는 `prev`를 추가하는, `Node` 구조의 확장이 필요하다. 이전에 `head`에 더미 노드를 두었던 것처럼 `tail`에도 더미 노드를 추가하여, 데이터를 담고 있는 `Node`들이 모두 같은 모양을 갖도록 한다.

```python
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
``` 

## 스택 (Stacks)

자료를 보관할 수 있는 선형 구조로 넣을 때에는 한 쪽 끝에서 밀어 넣어야하고, 꺼낼 때에는 같은 쪽에서 꺼내야한다. 후입선출 (LIFO - Last-in First-Out)의 구조

### 스택에서 발생하는 오류
* 더이상 뺄 수 없는 스택에서 pop을 할 때 (stack underflow)
* 더이상 채울 수 없는 스택에서 push를 할 때 (stack overflow)

### 연산의 정의
* `size()`: 현재 스택에 들어 있는 데이터 원소의 수를 구함
* `isEmpty()`: 현재 스택이 비어 있는지를 판단 (`size() == 0?`)
* `push(x)`: 데이터 원소 `x` 를 스택에 추가
* `pop()`: 스택에 가장 나중에 저장된 데이터 원소를 제거 (또한, 반환)
* `peek()`: 스택에 가장 나중에 저장된 데이터 원소를 참조 (반환), 그러나 제거하지는 않음

```python
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList


class ArrayStack:

	def __init__(self):
		self.data = []

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def peek(self):
		return self.data[-1]


class LinkedListStack:

	def __init__(self):
		self.data = DoublyLinkedList()

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data
```