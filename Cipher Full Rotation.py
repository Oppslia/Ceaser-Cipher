cipherList = []
plainText = input("Enter a word ")
def rotator(pos): 
  sentence = ""
  for letter in plainText:
    num = ord(letter) + pos
    if letter.islower():
      if num > ord('z'): # only happens if it is a z!
          num -= 26
    elif letter.isupper():
      if num > ord("Z"):
        num -= 26 
    else:
      sentence += letter
      continue
    char = chr(num)
    sentence += char
  return sentence

for pos in range(1,27):
  cipherList.append(rotator(pos))

for x,y in zip(range(0, len(cipherList)), reversed(cipherList)):
  print(x,y)
