import datetime
import hashlib


keyList = [line.rstrip('\n') for line in open('input.txt')]
hashList = [line.rstrip('\n') for line in open('hash_input.txt')]

passList = []

date = datetime.datetime.now()

def modify(item, passList):

        passList.append(item)
        passList.append(item.capitalize())

        for i in range (0,100):
            passList.append(item+str(i))
            passList.append(item.capitalize()+str(i))
            passList.append(item+str(i)+'!')
            passList.append(item.capitalize()+str(i)+'!')

        for i in range (1990,date.year):
            passList.append(item+str(i))
            passList.append(item.capitalize()+str(i))
            passList.append(item+str(i)+'!')
            passList.append(item.capitalize()+str(i)+'!')
            passList.append(item+str(i)+'.')
            passList.append(item.capitalize()+str(i)+'.')

        passList.append(item+'!')
        passList.append(item.capitalize()+'!')
        passList.append(item+'.')
        passList.append(item.capitalize()+'.')




def hacker(item):
    hackerPass = []
    if 'o' in item:
        hackerPass.append(item.replace('o','0'))
        if 'e' in item:
            hackerPass.append((item.replace('o','0')).replace('e','3'))
            hackerPass.append((item.replace('o','0')).replace('e','€'))
            if 'a' in item:
                hackerPass.append(((item.replace('o','0')).replace('e','3')).replace('a','@'))
                hackerPass.append(((item.replace('o','0')).replace('e','€')).replace('a','@'))
        if 'a' in item:
            hackerPass.append((item.replace('o','0')).replace('a','@'))
        if 's' in item:
            hackerPass.append((item.replace('o','0')).replace('s','$'))
        if 'i' in item:
            hackerPass.append((item.replace('o','0')).replace('i','1'))
    if 'e' in item:
        hackerPass.append(item.replace('e','3'))
        hackerPass.append(item.replace('e','€'))
    if 'a' in item:
        hackerPass.append(item.replace('a','@'))
        hackerPass.append(item.replace('a','4'))
    if 's' in item:
        hackerPass.append(item.replace('s','$'))
    if 'i' in item:
        hackerPass.append(item.replace('i','1'))

    return hackerPass




for item in keyList:
    modify(item,passList)

    for it in hacker(item):
        modify(it,passList)

print(passList)

for item in passList:
    hashedPass = hashlib.md5(item.encode('utf-8')).hexdigest()
    if (hashedPass == hashList[0]):
        print('\n')
        print ('The password is: '+item)

i = 0

with open('output.txt', 'w') as f:
    for item in passList:
        f.write("%s\n" % item)
        i = i + 1

print('\n')
print(str(i)+' passwords were tried')

with open('hash_output.txt', 'w') as g:
    for item in passList:
        g.write(item+hashlib.md5(item.encode('utf-8')).hexdigest())
        g.write('\n')
