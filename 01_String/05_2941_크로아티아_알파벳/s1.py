# 정답 1
# 통과했으나 오답 (정답이 맞았다..)
word = input()
croatian_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# count에 word의 길이를 입력
count = len(word)

# 크로아티아 알파벳의 개수만큼 -1
for check in croatian_alph:
    count -= word.count(check)

# 'dz='에서 3-1로 2가 나오는 줄 알았으나 'z=' 에서 1을 더 빼기 때문에 정답이 맞다.
print(count)

# 정답 2
word = input()
croatian_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳을 길이 1 짜리 다른 걸로 바꿈
for check in croatian_alph:
    word = word.replace(check, '1')

print(len(word))