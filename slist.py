'''
단순연결리스트(Singly Linked List)
동적 메모리 할당을 이용해 노드들을 한 방햐응로 연결하여 리스트를 구현하는 자료구조

순차탐색(Sequential Search)
첫 노드부터 원하는 노드를 찾을 때까지 차례로 방문하는 방법
'''

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.link = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
