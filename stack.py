class Stack:
    def __init__(self, stack):
        self.stack = stack

    def is_empty(self, bool_res_list=False):
        if len(self.stack) == 0:
            bool_res_list = True
        return bool_res_list

    def push(self, new_symbol):
        while True:
            if len(new_symbol) != 1:
                print('You try add more than one simbol!')
                break
            else:
                self.stack.append(new_symbol)
                break

    def pop(self):
        del_end_symbol = self.stack.pop(-1)
        return del_end_symbol

    def peek(self):
        end_symbol = self.stack[-1]
        return end_symbol

    def size(self):
        size_stack = len(self.stack)
        return size_stack