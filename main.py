
class Stack:
    def __init__(self, brackets_collection):
        self.brackets_collection = brackets_collection

    def isEmpty(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self, stack_list):
        size_stack = len(stack_list)
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
    stack = Stack('()[]{}')
    stack.inp_string_brackets()



