def solution(numbers):
    result = ''
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: x*3, reverse = True)
    result = str(int(''.join(numbers)))
    return result