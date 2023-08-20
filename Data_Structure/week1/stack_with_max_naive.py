class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []  # 用來維護最大值的輔助堆疊

    def Push(self, a):
        self.__stack.append(a)
        if not self.__max_stack or a >= self.__max_stack[-1]:
            self.__max_stack.append(a)

    def Pop(self):
        assert len(self.__stack)
        if self.__stack[-1] == self.__max_stack[-1]:
            self.__max_stack.pop()
        self.__stack.pop()

    def Max(self):
        assert len(self.__stack)
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
