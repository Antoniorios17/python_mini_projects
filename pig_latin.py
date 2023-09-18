def pig_latin(text):
  say = ""
  # Separate the text into words
  words = [x.split(" ") for x in text]
  for word in words:
    # Create the pig latin word and add it to the list
    say= say + word
    # Turn the list back into a phrase
  return say
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

text="hello how are you"

words1 = text.split()
print(words1)