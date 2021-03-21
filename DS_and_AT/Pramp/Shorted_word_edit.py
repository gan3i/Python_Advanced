from collections import deque
import string

def shortestWordEditPath(source, target, words):
  word_set= set(words)
  q = deque()
  q.append([source,0])
  
  visited = set()
  visited.add(source)
  
  while len(q):
    word, depth = q.popleft()
    
    if word == target:
      return depth
    for i in range(len(word)): 
      for c in string.ascii_lowercase:
        new_word = None
        if i == len(word) - 1:
          new_word = word[:i] + c
        else:
          new_word = word[:i] + c + word[i+1:]
          
        if new_word in word_set and new_word not in visited:
          q.append([new_word, depth + 1])
          visited.add(new_word)
          
  return -1


