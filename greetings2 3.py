word = input()
itr = 0
for i in range(len(word)):
  if word[i] == 'e':
    itr +=1
print('{}{}{}'.format("h",2*itr*'e','y'))
