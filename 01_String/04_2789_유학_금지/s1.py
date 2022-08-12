# 처음 방법
remove_word = list('CAMBRIDGE')

word = input()
result = ''
for test in word:
    if test in remove_word:
        result = result + test

print(result)

# 나중 방법
word = input()
result = word
for test in word:
    result = result.replace(test, '')

print(result)
