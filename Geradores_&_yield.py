class GeneratorExamples:
    @staticmethod
    def simple_generator():
        # Generator expression for iterating over each letter lazily
        gen = (char for char in "python")
        print(next(gen))  # outputs 'p'
        print(next(gen))  # outputs 'y'

    @staticmethod
    def generator_with_yield():
        # Generator function yielding numbers 0 to 4 lazily
        def gen_func():
            for i in range(5):
                yield i

        g = gen_func()
        print(next(g))  # outputs 0
        print(next(g))  # outputs 1

    @staticmethod
    def generator_with_multiple_yields():
        # Generator yielding a single value then a range lazily
        def gen_func():
            yield 1
            for i in range(2, 5):
                yield i

        g = gen_func()
        print(next(g))  # outputs 1
        print(next(g))  # outputs 2
        print(next(g))  # outputs 3
        print(next(g))  # outputs 4

    @staticmethod
    def generator_exhaustion():
        # Demonstrates StopIteration exception after generator ends
        def gen_func():
            yield 1
            yield 2

        g = gen_func()
        try:
            print(next(g))  # 1
            print(next(g))  # 2
            print(next(g))  # Raises StopIteration
        except StopIteration:
            print("Generator exhausted!")


if __name__ == "__main__":
    GeneratorExamples.simple_generator()
    GeneratorExamples.generator_with_yield()
    GeneratorExamples.generator_with_multiple_yields()
    GeneratorExamples.generator_exhaustion()
