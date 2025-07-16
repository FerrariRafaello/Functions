import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # tie-breaker to maintain insertion order among equal priorities

    def push(self, item, priority):
        # Negate priority for max-heap behavior with heapq (which is a min-heap by default)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # Returns the item with the highest priority
        return heapq.heappop(self._queue)[-1]


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def demo_priority_queue():
    q = PriorityQueue()
    q.push(Person("Marcos"), 28)
    q.push(Person("João"), 30)
    q.push(Person("Maria"), 15)

    print(q.pop())  # João (highest priority)
    print(q.pop())  # Marcos
    print(q.pop())  # Maria


def demo_bitwise_operations():
    n1 = 10  # binary 1010
    n2 = 6   # binary 0110

    print(f"n1 (bin): {bin(n1)}")
    print(f"n2 (bin): {bin(n2)}")

    # AND (&): bit set only if both bits are 1
    r_and = n1 & n2
    print(f"AND (&) result: {r_and} ({bin(r_and)})")

    # OR (|): bit set if any bit is 1
    r_or = n1 | n2
    print(f"OR (|) result: {r_or} ({bin(r_or)})")

    # XOR (^): bit set if bits are different
    r_xor = n1 ^ n2
    print(f"XOR (^) result: {r_xor} ({bin(r_xor)})")

    # NOT (~): bitwise negation (two's complement)
    r_not = ~n1
    print(f"NOT (~) result: {r_not} ({bin(r_not)})")

    # Left shift (<<): shifts bits to left, appends zeros
    r_lshift = n1 << 2
    print(f"Left Shift (<< 2): {r_lshift} ({bin(r_lshift)})")

    # Right shift (>>): shifts bits to right, truncates bits
    r_rshift = n1 >> 1
    print(f"Right Shift (>> 1): {r_rshift} ({bin(r_rshift)})")


if __name__ == "__main__":
    print("Priority Queue Demo:")
    demo_priority_queue()
    print("\nBitwise Operations Demo:")
    demo_bitwise_operations()
