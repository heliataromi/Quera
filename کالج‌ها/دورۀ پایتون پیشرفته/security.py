from re import fullmatch


class Security:

    def secure(self, info):
        split_info = info.split()
        for i in range(len(split_info)):
            inf = split_info[i]
            if self.is_social_account_info(inf):
                split_info[i] = inf[:inf.rindex('/') + 1] + self.encrypt(inf[inf.rindex('/') + 1:])
        return ' '.join(split_info)

    def is_social_account_info(self, param):
        pattern = r'^[A-Z][a-z]+:www.[a-z0-9\.]+\/\w+$'
        if fullmatch(pattern, param):
            return True
        return False

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
