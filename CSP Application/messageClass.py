class Message():
    def __init__(self, message, offset):
        self.message = message
        self.off = offset
        self.encrypted = self.__encode()
    
    def __encode(self):
        new_string = ''
        letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        for c in self.message:
            if c == ' ' or c == '.' or c == ',' or c == '?' or c == '!' or c == "'":
                new_string += c
            else:
                position = letters.index(c) + self.off
                if position > len(letters) - 1:
                    position -= len(letters) 
                new_string += letters[position]
        return new_string