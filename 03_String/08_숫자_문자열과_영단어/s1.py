def solution(s):
    answer = s
    number_alph = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, alph in enumerate(number_alph):
        answer = answer.replace(alph, str(num))

    return int(answer)
