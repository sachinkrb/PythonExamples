catNames=[]
while True:
    print('enter name of cat ' + str(len(catNames)+1))
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('the cat names are:')
for name in catNames:
    print(name)
          
