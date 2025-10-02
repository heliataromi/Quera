from re import fullmatch


class Security:

    def secure(self, info: str) -> str:
        split_info = info.split()
        for i in range(len(split_info)):
            if self.is_social_account_info(split_info[i]):
                split_info[i] = split_info[i][:split_info[i].rindex('/') + 1] + self.encrypt(split_info[i][split_info[i].rindex('/') + 1:])
        return ' '.join(split_info)

    def is_social_account_info(self, param: str) -> bool:
        pattern = r'^[A-Z][a-z]+:www.[a-z0-9\.]+\/\w+$'
        if fullmatch(pattern, param):
            return True
        return False

    def encrypt(self, s: str) -> int:
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

