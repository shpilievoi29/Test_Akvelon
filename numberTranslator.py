"""
implementation of a class that accepts a string version of numbers

"""


class NumberFormatter:
    def __init__(self, input_numbers):
        self.input_numbers = input_numbers

    def parseInt(self):
        if self.input_numbers == "" or type(self.input_numbers) != str\
            or type(self.input_numbers) == int and 2 <= len(self.input_numbers) <= 2 ** 32 - 1:

            """
            checking if a string is empty or not a string type or float type
            """
            result = "you entered wrong format"

        else:
            result = 0
            if self.input_numbers[0] == '-':
                start_idx = 1
                is_negative = True
            elif self.input_numbers[0] == '+':
                start_idx = 1
                is_negative = False
            else:
                start_idx = 0
                is_negative = False

            for i in range(start_idx, len(self.input_numbers)):
                place = 10 ** (len(self.input_numbers) - (i + 1))
                digit = ord(self.input_numbers[i]) - ord('0')
                result += place * digit

            if is_negative:
                return -1 * result

        return result
