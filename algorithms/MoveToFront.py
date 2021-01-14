from __future__ import print_function

SYMBOL_TABLE = list('0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,;$%^&*.!@#()-_?/:" \t\n[]')
s = list("'")
SYMBOL_TABLE=SYMBOL_TABLE+s
class MoveToFront:

    def code(self, text):
        transformed_array, pad = [], SYMBOL_TABLE[::]
        for char in text:
            index = pad.index(char)
            transformed_array.append(index)
            pad = [pad.pop(index)] + pad
        return transformed_array

    def decode(self, transformed_array):
        chars, pad = [], SYMBOL_TABLE[::]
        for index in transformed_array:
            char = pad[index]
            chars.append(char)
            pad = [pad.pop(index)] + pad
        return ''.join(chars)
