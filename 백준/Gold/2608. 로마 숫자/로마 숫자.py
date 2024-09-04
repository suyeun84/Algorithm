import sys

def solution():
    input = sys.stdin.readline

    roman_array = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    roman_dict = {roman: num for roman, num in roman_array}

    def num_to_str(num):
        result = ''
        for roman, value in roman_array:
            while num >= value:
                result += roman
                num -= value
        return result

    def str_to_num(roman):
        idx, total = 0, 0
        while idx < len(roman):
            if idx + 1 < len(roman) and roman[idx:idx + 2] in roman_dict:
                total += roman_dict[roman[idx:idx + 2]]
                idx += 2
            else:
                total += roman_dict[roman[idx]]
                idx += 1
        return total

    str1 = input().strip()
    str2 = input().strip()
    tot = str_to_num(str1) + str_to_num(str2)
    print(tot)
    print(num_to_str(tot))


if __name__ == '__main__':
    solution()
