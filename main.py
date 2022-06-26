class Stack:
    def __init__(self, stack):
        self.stack = list(stack)

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


if __name__ == '__main__':
    stack = Stack('(({}))(({[]}))')
    stack.size()
