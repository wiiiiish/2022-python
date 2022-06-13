class Node:
    """링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data # 현재 노드가 저장하고 있는 정보
        self.next = None # 다음 노드에 대한 레퍼런스
        self.prev = None # 이전 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    # 삽입 연산
    def insert_after(self, previous_node, data):
        """더블리 링크드 리스트 삽입 연산"""
        new_node = Node(data)

        # tail 노드 다음에 삽입하는 경우
        if previous_node is self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # 두 노드 사이에 삽입하는 경우
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    # 리스트의 가장 앞에 삽입
    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)

        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 리스트가 비어있지 않는 경우
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # 리스트의 끝에 새로운 데이터 추가하는 연산
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data) # 새로운 데이터를 저장하는 노드

        # 링크드 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어있지 않은 경우
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 접근 메소드
    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""

        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator

    # 탐색 메소드
    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    #__str__ 메소드
    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
my_list.prepend(11)
my_list.prepend(7)
my_list.prepend(5)
my_list.prepend(3)
my_list.prepend(2)

print(my_list) # 링크드 리스트 출력

# head, tail 노드가 제대로 설정됐는지 확인
print(my_list.head.data)
print(my_list.tail.data)