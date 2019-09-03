## Linear Arrays
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