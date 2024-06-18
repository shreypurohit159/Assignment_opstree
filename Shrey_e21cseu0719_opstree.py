class Node:
    def __init__(start, digit):
        start.digit = digit
        start.next = None

class linkedlist:
    def __init__(start):
        start.head = None
    def insert(start, digit):
        new_node = Node(digit)
        if start.head is None:
            start.head = new_node
        else:
            #current = start.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(start):
        current = start.head
        digits = []
        while current:
            digits.append(str(current.digit))
            current = current.next
        print(''.join(digits))

    def _reverse(start):
        prev = None
        current = start.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        start.head = prev


    def multiply(self, other):
        self._reverse()
        other._reverse()
        node1, node2 = self.head, other.head
        result = linkedlist()
        result.insert(0)  # Initialize with 0
        position = 0
        while node2:
            temp_result = linkedlist()
            for _ in range(position):
                temp_result.insert(0)  # Add leading zeros
            carry = 0
            temp_node1 = node1
            while temp_node1:
                product = temp_node1.digit * node2.digit + carry
                carry = product // 10
                temp_result.insert(product % 10)
                temp_node1 = temp_node1.next
            if carry > 0:
                temp_result.insert(carry)
            result = result.add(temp_result)
            node2 = node2.next
            position += 1
        result._reverse()
        self._reverse()
        other._reverse()
        return result
    
    def _add_same_length(self, node1, node2):
        if node1 is None:
            return None, 0
        result_node, carry = self._add_same_length(node1.next, node2.next)
        total = node1.digit + node2.digit + carry
        new_node = Node(total % 10)
        new_node.next = result_node
        return new_node, total // 10

    def add(self, other):
        self._reverse()
        other._reverse()
        result_list = linkedlist()
        node1, node2 = self.head, other.head
        result_head, carry = self._add_same_length(node1, node2)
        result_list.head = result_head
        if carry > 0:
            new_node = Node(carry)
            new_node.next = result_list.head
            result_list.head = new_node
        result_list._reverse()
        self._reverse()
        other._reverse()
        return result_list

    def _subtract_same_length(self, node1, node2):
        if node1 is None:
            return None, 0
        result_node, borrow = self._subtract_same_length(node1.next, node2.next)
        diff = node1.digit - node2.digit - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        new_node = Node(diff)
        new_node.next = result_node
        return new_node, borrow

    def subtract(self, other):
        self._reverse()
        other._reverse()
        result_list = linkedlist()
        node1, node2 = self.head, other.head
        result_head, _ = self._subtract_same_length(node1, node2)
        result_list.head = result_head
        result_list._reverse()
        self._reverse()
        other._reverse()
        return result_list

def arithmetic_linkedlist(number):
    linked_list = linkedlist()
    for digits in str(number):
        linked_list.insert(int(digits))
        return linked_list
    
num1 = arithmetic_linkedlist(1234)
num2 = arithmetic_linkedlist(5678)

print("Number 1: ", end="")
num1.display()
print("Number 2: ", end="")
num2.display()

result = num1.add(num2)
print("Addition Result: ", end="")
result.display()

result = num1.subtract(num2)
print("Subtraction Result: ", end="")
result.display()

result = num1.multiply(num2)
print("Multiplication Result: ", end="")
result.display()


