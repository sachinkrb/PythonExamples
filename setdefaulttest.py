import pprint
message = 'this is just a test for setdefault method'
count ={}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
# counts the total number of repeated characters and prints out key/value pair for
#all repeated characters as a dictionary. Setdefault() ensures default value of count to zero

pprint.pprint(count) #pretty print, cleaner print out

