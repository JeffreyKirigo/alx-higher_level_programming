#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) != str or not type(roman_string):
        return 0
    for k in range(len(roman_string)):
        if k + 1 < len(roman_string) and roman[roman_string[k]] <\
                roman[roman_string[k + 1]]:
            num -= roman[roman_string[k]]
        else:
            num += roman[roman_string[k]]
    return int(num)
