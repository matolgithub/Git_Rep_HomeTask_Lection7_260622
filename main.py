
class Stack:
    def __init__(self, stack):
        self.stack = list(stack)
        # ( chr(40), ) chr(41), [ chr(91), ] chr(93), { chr(123), } chr(125)
        self.brackets_collection = f'{chr(40)}{chr(41)}{chr(91)}{chr(93)}{chr(123)}{chr(125)}'

    def isEmpty(self, bool_res_list=False):
        if len(self.stack) == 0:
            bool_res_list = True
        return bool_res_list

    def push(self, new_simbol):
        while True:
            if len(new_simbol) != 1:
                print('You try add more than one simbol!')
                break
            else:
                self.stack.append(new_simbol)
                break

    def pop(self):
        del_end_simbol = self.stack.pop(-1)
        return del_end_simbol

    def peek(self):
        end_simbol = self.stack[-1]
        return end_simbol

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
    stack = Stack('(({}))(({[]}))')
    # stack.isEmpty()
    # stack.inp_string_brackets()
    # stack.size()
    # stack.push('{')
    # stack.pop()
    stack.peek()
