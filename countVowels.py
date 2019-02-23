#Python 3.7.2
#A program that calcualtes total number of vowels

found = []
count = 0
vowels =['a','e','i','o','u']
print('Give me a word so I can count vowels, Type exit to exit:')
thatWord = input()
for letter in thatWord:
    if thatWord == 'exit':
        break
    elif letter in vowels:
        found.append(letter)
        count += 1
print(found)
print(count)
