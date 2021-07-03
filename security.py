class Security:

    def secure(self, info):
        pass #TODO

    def is_social_account_info(self, param):
        pass #TODO

    def encrypt(self, s):
        last_char = ''
        uniform_substring = ''
        encryption = ''
        for current_char in s:
            if current_char == last_char:
                number_of_chars = len(uniform_substring)
                uniform_substring += current_char
                ascii_code = ord(current_char)
                weight = ascii_code - 96
                encryption += str(weight * (number_of_chars + 1))
            else:
                last_char = current_char
                uniform_substring = current_char
                ascii_code = ord(current_char)
                weight = ascii_code - 96
                encryption += str(weight * 1)
        return encryption


f = Security()
print(f.encrypt('abcccdd'))
