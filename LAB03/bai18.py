class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def bubble_sort_linked_list(head):
    if not head:
        return head
    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(result)

if __name__ == "__main__":
    head_node = Node(5, Node(1, Node(4, Node(2, Node(8)))))
    sorted_head = bubble_sort_linked_list(head_node)
    print_linked_list(sorted_head)