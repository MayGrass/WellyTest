# python 3.10.2


class Stack:
    class SinglyLinkedListNode:
        def __init__(self, data: int) -> None:
            self.data = data
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.stack_size = 0

    def push(self, data) -> None:
        data = self.SinglyLinkedListNode(data)
        # 如果head為空，代表代表插入的值為第一個Node
        if not self.head:
            self.head = data
        else:
            self.tail.next = data
        self.tail = data
        self.stack_size += 1

    def pop(self) -> None | str:
        if not self.stack_size:
            return "Stack is empty"
        # 如果size為1，代表只有一個Node，直接清空head
        elif self.stack_size == 1:
            pop_value = self.head.data
            self.head = None
        else:
            # 兩個Node以上，所以要找到最後一個Node
            current_node = self.head
            while current_node.next:
                self.tail = current_node
                current_node = current_node.next
            pop_value = self.tail.next.data
            self.tail.next = None
        self.stack_size -= 1
        print(pop_value)

    def size(self) -> None:
        print(self.stack_size)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.size()
