pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha(): #input =Rt
  word = original.lower() #word = rt
  first = word[0] #first = r
  new_word = word + first + pyg # new_word = rt + r + ay = rtray
  new_word = new_word[1:len(new_word)] # tray
  print (new_word)
else:
    print ('empty')