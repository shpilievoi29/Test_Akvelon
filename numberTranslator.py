"""
implementation of a class that accepts a string version of numbers

"""


class NumberFormatter:
    def __init__(self, input_numbers):
        self.input_numbers = input_numbers

    def parseInt(self):
        if self.input_numbers == "" or type(self.input_numbers) != str or type(
                self.input_numbers) == float:
            """
            checking if a string is empty or not a string type or float type
            """
            result = "you entered wrong format"

        else:
            result = int(self.input_numbers)
            """
            translator of valid data
            """
        return result


