
class Stack:
    def __init__(self, stack):
        self.stack = list(stack)
        # ( chr(40), ) chr(41), [ chr(91), ] chr(93), { chr(123), } chr(125)
        self.brackets_collection = f'{chr(40)}{chr(41)}{chr(91)}{chr(93)}{chr(123)}{chr(125)}'

    def isEmpty(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        size_stack = len(self.stack)
        return size_stack

    def inp_string_brackets(self):
        while True:
            string_brackets = input("Please, input string with brackets for testing: ")
            count_simbol = 0
            for symbol in string_brackets:
                if symbol not in self.brackets_collection:
                    count_simbol += 1
            if count_simbol == 0:
                break
        return string_brackets

    def balance_check(self):
        pass



if __name__ == '__main__':
    stack = Stack('(({}))')
    # stack.inp_string_brackets()
    # stack.size()
