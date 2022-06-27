from stack import Stack

class Brackets:
    def __init__(self):
        # ( chr(40), ) chr(41), [ chr(91), ] chr(93), { chr(123), } chr(125)
        self.brackets_collection = f'{chr(40)}{chr(41)}{chr(91)}{chr(93)}{chr(123)}{chr(125)}'

    def inp_string_brackets(self):
        while True:
            string_brackets = input("Please, input string with brackets for testing: ")
            count_other_symbol = 0
            if string_brackets == '':
                print('No one symbol, try again!')
            else:
                for symbol in string_brackets:
                    if symbol not in self.brackets_collection:
                        count_other_symbol += 1
                if count_other_symbol == 0:
                    break
        list_brackets = list(string_brackets)
        return list_brackets

    def balance_check(self, result="Сбалансированно"):
        stack_brackets = Brackets()
        list_brackets = stack_brackets.inp_string_brackets()
        stack_object = Stack(list_brackets)
        stack_list = stack_object.stack
        while len(list_brackets) != 0:
            try:
                for symbol in list_brackets:
                    if symbol == chr(40):
                        list_brackets.remove(chr(41))
                        list_brackets.remove(symbol)
                    elif symbol == chr(91):
                        list_brackets.remove(chr(93))
                        list_brackets.remove(symbol)
                    elif symbol == chr(123):
                        list_brackets.remove(chr(125))
                        list_brackets.remove(symbol)
                    elif symbol == chr(41):
                        list_brackets.remove(chr(40))
                        list_brackets.remove(symbol)
                    elif symbol == chr(93):
                        list_brackets.remove(chr(91))
                        list_brackets.remove(symbol)
                    elif symbol == chr(125):
                        list_brackets.remove(chr(123))
                        list_brackets.remove(symbol)
            except ValueError:
                result = "Несбалансированно"
                break
        print(result)



if __name__ == '__main__':
    Brackets.balance_check(Brackets)