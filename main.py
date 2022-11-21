def is_vowel(c):
    return (
            c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
            or c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')


def pig_latin(s):
    length = len(s)
    index = -1
    for i in range(length):
        if is_vowel(s[i]):
            index = i
            break

    if index == -1:
        return '-1'

    return s[index:] + s[0:index] + 'ay'


if __name__ == '__main__':
    message = input('Enter a message: ')
    trs = pig_latin(message)
    if trs == '-1':
        print('No vowels found. Pig latin not possible')
    else:
        print(trs)
