from sys import stdin,stdout
listjoin = []
listmain = []
for list_ in stdin:
  listjoin += list_.split()
for word1 in listjoin:
  for word2 in listjoin:
    if word1 != word2:
      word = word1+word2
      if word not in listmain:
        listmain.append(word)
listmain.sort()
for words in listmain:
  print(words)