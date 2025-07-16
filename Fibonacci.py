class Fibonacci:
    def __init__(self, terms: int):
        if not isinstance(terms, int) or terms <= 0:
            raise ValueError("Number of terms must be a positive integer.")
        self.terms = terms
        self._count = 0
        self._a, self._b = 1, 1  # Starting values

    def __iter__(self):
        # Returns the iterator object (self)
        self._count = 0
        self._a, self._b = 1, 1
        return self

    def __next__(self):
        # Generates the next Fibonacci number
        if self._count >= self.terms:
            raise StopIteration
        if self._count < 2:
            # The first two numbers are 1, 1
            result = 1
        else:
            result = self._a + self._b
            self._a, self._b = self._b, result
        self._count += 1
        return result

    def get_sequence(self):
        # Return the entire Fibonacci sequence as a list
        return list(iter(self))


def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        fib = Fibonacci(n)
        print(f"First {n} Fibonacci terms:")
        for num in fib:
            print(num)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
