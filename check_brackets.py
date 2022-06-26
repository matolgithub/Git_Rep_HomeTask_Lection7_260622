import main

class Brackets:
    def __init__(self):
        # ( chr(40), ) chr(41), [ chr(91), ] chr(93), { chr(123), } chr(125)
        self.brackets_collection = f'{chr(40)}{chr(41)}{chr(91)}{chr(93)}{chr(123)}{chr(125)}'

    def inp_string_brackets(self):
        while True:
            string_brackets = input("Please, input string with brackets for testing: ")
            count_other_simbol = 0
            for symbol in string_brackets:
                if symbol not in self.brackets_collection:
                    count_other_simbol += 1
            if count_other_simbol == 0:
                break
        return list(string_brackets)

    def balance_check(self):
        stack_brackets = Brackets()
        list_brackets = stack_brackets.inp_string_brackets()
        stack = main.Stack(list_brackets).isEmpty()
        print(stack)


if __name__ == '__main__':
    Brackets.balance_check(Brackets)