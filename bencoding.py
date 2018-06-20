

class Decoding:
    def __init__(self, filename):
        self.final_list = []
        self.in_file = open(self.filename, "r")

    def decode_string(self, length):
        string_read = ""
        if not(length == 0):
            for count in range(length):
                string_read += self.in_file.read(1)
        return string_read.encode('ascii')

    def decode_int(self):
        int_ascii_read = ""
        while True:
            character = self.in_file.read(1)
            if character == 'e':
                break
            int_ascii_read += character
        return int(int_ascii_read)

    def decode(self):
        while True:
            character = self.in_file.read(1)  #read 1 byte a time
            if not character:  #end of file
                break
            if character.isdigit():
                self.final_list.append(self.decode_string(int(character)))
            if character == 'l':
                self.final_list.append(self.decode_list())
            if character == 'd':
                self.final_list.append(self.decode_dict())
            if character == 'i':
                self.final_list.append(self.decode_int())