import re


def real_numbers(numbers: list[str]) -> list[str]:
    result = []
    
    for number in numbers:
        if re.match('^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$', number):
            result.append('LEGAL')
        else:
            result.append('ILLEGAL')
    
    return result

