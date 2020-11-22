class Stack():
    def __init__(self):
        self.elements = []
        self.top = -1

    def push(self, element):
        self.elements.append(element)
        self.top += 1
        #print(f'push: {self.top}: {self.elements}')

    def pop(self):
        if self.top == -1:
            return None
        element = self.elements[self.top]
        self.elements.remove(element)
        self.top -= 1

        return element

    def peek(self):
        if self.top == -1:
            return None
        return self.elements[self.top]

    def __str__(self):
        return f'{self.elements}'

    def __repr__(self):
        return self.__str__()
